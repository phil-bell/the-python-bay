import json
import requests

class tpb:
    def __init__(self):
        self.base_url = "https://apibay.org/"

    def format_args(self, search_term):
        return search_term

    @classmethod
    def search(cls, search_term):
        return json.loads(requests.get(f"{cls.base_url}{cls.format_args(search_term)}"))

