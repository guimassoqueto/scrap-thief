from re import search

def get_amazon_id(url: str) -> str:
    result = search(r"/([A-Z0-9]{10})/", url)
    try:
      _id = result.group(1)
      return _id
    except:
       return None
    