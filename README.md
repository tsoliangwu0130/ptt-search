# ptt-search [![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A simple Python script to fetch PTT post from the command line.

## Usage

1. To install all dependencies, simply run:

```
$ pip install -r requirements.txt
```

2. Fetch posts

```
$ python ptt-search.py -b 'gossiping' -c '新聞'
```

## Options

```
Options:
    -h, --help       show this help message and exit
    -b <board name>  board name
    -c <category>    post category
    -k <keyword>     post keyword
    -p <pages>       number of pages
```
