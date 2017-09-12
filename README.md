# ptt-search [![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A simple Python script to fetch PTT post from the command line.

## Usage

1. To install all dependencies, simply run:

```
$ pip install -r requirements.txt
```

2. Fetch posts

```
$ python ptt-search.py -b 'gossiping' -k '新聞 iPhone 蘋果'
```

## Options

```
Usage: ptt-search.py [options]

Options:
  -h, --help         show this help message and exit
  -b <board name>    search posts in a board (required)
  -k <keywords>      search posts with keywords (separate keywords with space)
  -n <rsult amount>  search how many posts
  -z <push amount>   search posts with push more than an amount
```
