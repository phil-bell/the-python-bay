[![title](https://img.shields.io/pypi/v/the-python-bay.svg)](https://pypi.org/project/the-python-bay)
[![title](https://img.shields.io/pypi/pyversions/the-python-bay.svg)](https://pypi.org/project/the-python-bay)


# the-python-bay

Python library for searching thepiratebay.org

## Install

    pip install the-python-bay

## Usage

```
from the_python_bay import tpb

results = tpb.search("ubuntu")
```

This will return the a list of instances of the `Torrent` class.

So you can then access the data like so:
```
for torrent in results:
    print(f"{torrent.name} - {torrent.magnet}")
```