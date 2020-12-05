import urllib
import requests
from typing import List


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
        self._magnet = f"magnet:?xt=urn:btih:{value}&dn={urllib.parse.quote(self.name)}{self.trackers}"

    @property
    def to_dict(self):
        return {**self.__dict__, **{"magnet": self.magnet}}


class ThePythonBay:
    def __init__(self) -> None:
        self.api_url = "https://apibay.org/"
        self.search_url = "q.php?q="
        self.sfw_filter = "&cat=100,200,300,400,600"

    @classmethod
    def search(cls, search_term: str, sfw=False) -> List[Torrent]:
        tpb = cls()
        res = requests.get(
            f"{tpb.api_url}{tpb.search_url}{urllib.parse.quote(search_term)}{tpb.sfw_filter if sfw else ''}"
        )
        return [Torrent(torrent) for torrent in res.json()]

    @classmethod
    def search_dict(cls, search_term: str, sfw=False) -> list:
        tpb = cls()
        res = requests.get(
            f"{tpb.api_url}{tpb.search_url}{urllib.parse.quote(search_term)}{tpb.sfw_filter if sfw else ''}"
        )
        return [Torrent(torrent).to_dict for torrent in res.json()]

    @classmethod
    def top_movies(cls) -> List[Torrent]:
        tpb = cls()
        res = requests.get(f"{tpb.api_url}precompiled/data_top100_201.json")
        return [Torrent(torrent) for torrent in res.json()]

    @classmethod
    def top_tv(cls) -> List[Torrent]:
        tpb = cls()
        res = requests.get(f"{tpb.api_url}precompiled/data_top100_205.json")
        return [Torrent(torrent) for torrent in res.json()]
