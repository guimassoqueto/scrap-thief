from datetime import datetime
from time import sleep
from app.pechinchou import PechinchouThief
from pytz import timezone
from app.settings import PECHINCHOU_API_HOME, RABBITMQ_SEND_QUEUE
from app.helpers import get_amazon_id
from app.rabbitmq import RabbitMQPublisher


if __name__ == "__main__":
    #most_recent_date = datetime.now(tz=timezone('America/Sao_Paulo'))
    most_recent_date = datetime(2022, 11, 30, tzinfo=timezone('America/Sao_Paulo'))
    while True:
        print('getting items')
        items = PechinchouThief.get_items(PECHINCHOU_API_HOME)
        pids = []
        for item in items:
            if item.created_at > most_recent_date and 'amazon.com' in item.long_url:
                most_recent_date = item.created_at
                pid = get_amazon_id(item.long_url)
                if pid: pids.append(pid)
        if pids:
            print(pids)
            publisher = RabbitMQPublisher()
            publisher.publish_pids({RABBITMQ_SEND_QUEUE: pids})
            
        sleep(30)