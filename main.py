from datetime import datetime
from time import sleep
from app.pechinchou import PechinchouThief
from pytz import timezone
from app.settings import PECHINCHOU_API_HOME
from app.helpers import get_amazon_id
from app.rabbitmq import RabbitMQPublisher


if __name__ == "__main__":
    most_recent_date = datetime(2022, 11, 30, tzinfo=timezone('America/Sao_Paulo'))
    while True:
        print('getting items')
        items = PechinchouThief.get_items(PECHINCHOU_API_HOME)
        
        amazon_pids = []
        magalu_urls = []

        for item in items:
            if item.created_at > most_recent_date:
                most_recent_date = item.created_at
                
                if 'amazon.com' in item.long_url:
                    pid = get_amazon_id(item.long_url)
                    amazon_pids.append(pid)

                if 'magazineluiza.com' in item.long_url or 'magazinevoce.com' in item.long_url:
                    magalu_urls.append(item.long_url)
        
        if magalu_urls:
            print('New Magalu Item(s)')
            publisher = RabbitMQPublisher(queue_name="magalu-items")
            publisher.publish_pids({ "magalu-items": magalu_urls })
        
        if amazon_pids:
            print('New Amazon Item(s)')
            publisher = RabbitMQPublisher(queue_name="amazon-colly")
            publisher.publish_pids({ "amazon-colly": amazon_pids })

        sleep(30)
