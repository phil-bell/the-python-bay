import json
import requests

class tpb:
    def __init__(self):
        self.api_url = "https://apibay.org"  

    def format_args(self, search_term):
        return search_term

    @classmethod
    def search(cls, search_term):
        return json.loads(requests.get(f"{cls.api_url}{cls.format_args(search_term)}"))

