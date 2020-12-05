[![](https://img.shields.io/pypi/v/the-python-bay.svg)](https://pypi.org/project/the-python-bay)
[![](https://img.shields.io/pypi/pyversions/the-python-bay.svg)](https://pypi.org/project/the-python-bay)

- [Install](#install)
- [Basic Usage](#basic-usage)
- [Full docs](#full-docs)
    - [search](#search)
    - [top_movies](#top_movies)
    - [top_tv](#top_tv)
    - [Torrent](#torrent)


# the-python-bay

Python library for searching thepiratebay.org

## Install

```bash
pip install the-python-bay
```
## Basic Usage

```python
from the_python_bay import tpb

results = tpb.search("ubuntu")
```

This will return the a list of instances of the `Torrent` class.

So you can then access the data like so:
```python
for torrent in results:
    print(f"{torrent.name} - {torrent.magnet}")
```

## Full Docs
### search
This can be used to search thepiratebay.org, it will return a list of instances of the `Torrent` class.
```python
from the_python_bay import tpb
results = tpb.search("ubuntu")
```

### top_movies
Can be used to return the current top 100 movies on thepiratebay.org
```python
from the_python_bay import tpb
results = tpb.top_movies()
```

### top_tv
Can be used to return the current top 100 tv on thepiratebay.org
```python
from the_python_bay import tpb
results = tpb.top_tv()
```

### Torrent
The `Torrent` class is the format the torrents are returned in, it has the following attributes:
- `name`     the torrents name
- `magent`   the torrents magnet link
- `seeders`  number of seeders the torrent has
- `username` the username of the torrents uploader
- `status`   the users prominence status

Torrent also has the property `to_dict` that can he used to return the dict of the the object. It can be used more generally:
```python
from the_python_bay import tpb
results = tpb.search_dict("ubuntu")

```
Or it can be used on a specific `Torrent` object like so:
```python
from the_python_bay import tpb
results = tpb.search("ubuntu")
for torrent in results:
    print(torrent.to_dict)
```
Or even more directly:
```python
torrent = Torrent(data)
torrent.to_dict
```