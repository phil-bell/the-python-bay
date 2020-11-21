import json
import urllib
import requests

class ThePythonBay:
    def __init__(self):
        self.api_url = "https://apibay.org/q.php?q="  

    @classmethod
    def search(cls, search_term):
        tpb = cls()
        req = requests.get(f"{tpb.api_url}{urllib.parse.quote(search_term)}")
        print(req)
        print(req.json())
        return req.json()
