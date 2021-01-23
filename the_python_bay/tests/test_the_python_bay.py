import json
from ..main import ThePythonBay as tpb


class TestThePythonBay:
    def test_the_python_bay_search(self):
        results = tpb.search("ubuntu")
        assert len(results) > 1

    def test_the_python_bay_search_dict(self):
        results = tpb.search_dict("ubuntu")
        assert len(results) > 1
        first_dict = results[0]
        assert "magnet" in first_dict.keys()

    def test_the_python_bay_top_movies(self):
        top_movies = tpb.top_movies()
        assert len(top_movies) == 100


class TestTorrent:
    def test_magnet(self):
        torrent = tpb.search("ubuntu")[0]
        assert "magnet" in torrent.magnet

    def test_name(self):
        torrent = tpb.search("ubuntu")[0]
        assert "ubuntu" in torrent.name.lower()
