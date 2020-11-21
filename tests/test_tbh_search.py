import pytest
from the_python_bay import tpb

class TestThePythonBay:

    def test_the_python_bay_search(self):
        results = tpb.search("ubuntu")
        assert len(results) > 1
