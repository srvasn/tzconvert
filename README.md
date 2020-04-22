[![PyPI version](https://badge.fury.io/py/tzconvert.svg)](https://badge.fury.io/py/tzconvert)

# tzconvert

tzconvert is a simple library for converting a naive, timezone unaware
datetime object to it's smarter, timezone aware version.

### Installation

Installation is straightforward.

`pip install tzconvert`

#### Installing from sources

- Clone this git repository.

- cd into the project folder.

- run `python setup.py install`

### Usage


```python
>>> import tzconvert
>>> import datetime

>>> naive_datetime = datetime.datetime.utcnow()

>>> naive_datetime
datetime.datetime(2020, 4, 21, 22, 36, 27, 945535)

>>> adjusted_datetime = tzconvert.adjust_datetime(naive_datetime, "Venice")

>>> adjusted_datetime
datetime.datetime(2020, 4, 22, 0, 36, 27, 945535, tzinfo=tzoffset('GMT', 7200))
```

**NOTES** : 

- *adjust_datetime()* returns `None` on failure.
- *adjust_datetime()* takes an optional argument `debug`, set it to True
  to display debug messages on stdout.


PR's are more than welcome.