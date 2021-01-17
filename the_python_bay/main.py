import urllib
import requests
from bs4 import BeautifulSoup
from typing import Collection, List


class Torrent:
    def __init__(self, data) -> None:
        self._magnet = ""
        for key, value in data.items():
            setattr(self, key, value)
        self.trackers = "&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2F9.rarbg.me%3A2850%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2920%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce"
        self.magnet = data["info_hash"]

    @property
    def magnet(self) -> str:
        return self._magnet

    @magnet.setter
    def magnet(self, value) -> None:
        if "magnet:?xt=urn:btih:" not in value:
            self._magnet = f"magnet:?xt=urn:btih:{value}&dn={urllib.parse.quote(self.name)}{self.trackers}"
        else:
            self._magnet = value

    @property
    def to_dict(self):
        return {**self.__dict__, **{"magnet": self.magnet}}

class TheFallbackBay:
    def __init__(self) -> None:
        self.site_url = "https://thepiratebay10.org/"
        self.search_url = "search/"
        self.sfw_filter = "/1/99/100,200,300,400,600"

    @classmethod
    def search_dict(cls, search_term: str, sfw=False) -> list:
        tpb = cls()
        res = requests.get(
            f"{tpb.site_url}{tpb.search_url}{urllib.parse.quote(search_term)}{tpb.sfw_filter if sfw else ''}"
        )
        soup = BeautifulSoup(res.content, "html.parser")
        rows = soup.find_all("tr")
        torrents = []
        for row in rows[1:]:
            cols = [*row.children]
            if len(cols) > 3:
                torrents += [{
                    "name": cols[3].div.a.string,
                    "magnet": cols[3].a["href"],
                    "seeders": cols[5].string,
                    "username": cols[3].font.a and cols[3].font.a.string,
                    "status": cols[3].a.img and cols[3].a.img.get("title", None)
                }]
        return torrents

    @classmethod
    def search(cls, search_term: str, sfw=False) -> list:
        tpb = cls()
        res = requests.get(
            f"{tpb.site_url}{tpb.search_url}{urllib.parse.quote(search_term)}{tpb.sfw_filter if sfw else ''}"
        )
        soup = BeautifulSoup(res.content, "html.parser")
        rows = soup.find_all("tr")
        torrents = []
        for row in rows[1:]:
            cols = [*row.children]
            if len(cols) > 3:
                torrents += [Torrent({
                    "name": cols[3].div.a.string,
                    "magnet": cols[3].a["href"],
                    "seeders": cols[5].string,
                    "username": cols[3].font.a and cols[3].font.a.string,
                    "status": cols[3].a.img and cols[3].a.img.get("title", None)
                })]
        return torrents

class ThePythonBay:
    def __init__(self) -> None:
        self.api_url = "https://apibay.org/"
        self.search_url = "q.php?q="
        self.sfw_filter = "&cat=100,200,300,400,600"
        self._response = {}

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value):
        self._response = value

    @property
    def fallback(self):
        torrents = self.response.json()
        return self.repsonse.status != 200 or not torrents or torrents[0]["seeders"] == 0


    @classmethod
    def search(cls, search_term: str, sfw=False) -> List[Torrent]:
        tpb = cls()
        tpb.response = requests.get(
            f"{tpb.api_url}{tpb.search_url}{urllib.parse.quote(search_term)}{tpb.sfw_filter if sfw else ''}"
        )
        if tpb.fallback:
            return TheFallbackBay.search(search_term)
        return [Torrent(torrent) for torrent in tpb.response.json()]

    @classmethod
    def search_dict(cls, search_term: str, sfw=False) -> list:
        tpb = cls()
        tpb.response = requests.get(
            f"{tpb.api_url}{tpb.search_url}{urllib.parse.quote(search_term)}{tpb.sfw_filter if sfw else ''}"
        )
        if tpb.fallback:
            return TheFallbackBay.search(search_term)
        return [Torrent(torrent).to_dict for torrent in tpb.response]

    @classmethod
    def top_movies(cls) -> List[Torrent]:
        tpb = cls()
        tpb.response = requests.get(f"{tpb.api_url}precompiled/data_top100_201.json")
        return [Torrent(torrent) for torrent in tpb.response]

    @classmethod
    def top_tv(cls) -> List[Torrent]:
        tpb = cls()
        tpb.response = requests.get(f"{tpb.api_url}precompiled/data_top100_205.json")
        return [Torrent(torrent) for torrent in tpb.response]

