# ptt-search [![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A simple Python script to fetch PTT post from the command line.

## Usage

1. To install all dependencies, simply run:

```
$ pip install -r requirements.txt
```

2. Fetch posts

```
$ python ptt-search.py -b 'gossiping' -c '新聞' -p 5 -z 10
```

## Options

```
Usage: ptt-search.py [options]

Options:
  -h, --help        show this help message and exit
  -b <board name>   search posts in a board (required)
  -c <category>     search posts in a certain category
  -k <keyword>      search posts with keyword
  -p <page amount>  search posts for how many pages
  -z <push amount>  search posts with push more than an amount
```
