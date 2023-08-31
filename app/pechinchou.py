from pydantic import ValidationError
from typing import List
from app.pydantic_models import Item
from requests import get
from json import loads

class PechinchouThief:
    @staticmethod
    def get_items(url: str) -> List[Item]:
        response = get(url)
        data = loads(response.content)
        products = data['results']

        items: List[Item] = []

        for product in products:
            try:
                item = Item.model_validate(product)
                items.append(item)
            except ValidationError as e:
                print(e)
                continue
            
        return items