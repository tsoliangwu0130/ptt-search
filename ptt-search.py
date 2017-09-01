import requests
from bs4 import BeautifulSoup
from optparse import OptionParser

# constant variables
PTT_BASE_URL = 'https://www.ptt.cc'

# option parser
parser = OptionParser()
parser.add_option("-b",
                  dest="board",
                  help="board name",
                  metavar="<board name>")
parser.add_option("-c",
                  dest="category",
                  help="post category",
                  default='',
                  metavar="<category>")
parser.add_option("-k",
                  dest="keyword",
                  help="post keyword",
                  default='',
                  metavar="<keyword>")
parser.add_option("-p",
                  dest="pages",
                  help="number of pages",
                  default=1,
                  metavar="<pages>")
(options, args) = parser.parse_args()

# intial variables
cur_url = '{}/bbs/{}'.format(PTT_BASE_URL, options.board)
page = 1
post_list = []

while page <= int(options.pages):
    # request and parse current page
    html_doc = requests.get(cur_url)
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    prev_url = soup.find('div', {'class': 'btn-group-paging'}).findChildren()[1]['href']

    # fetch posts from current page
    for post in soup.find_all('div', {'class': 'title'}):
        title = post.text
        link = 'URL not found.' if not post.find('a') else post.find('a')['href']
        if options.category in title and options.keyword in title:
            post_list.append({'title': title, 'link': PTT_BASE_URL + link})
    cur_url = PTT_BASE_URL + prev_url
    page += 1

# print fetched posts and links
for idx, post in enumerate(post_list):
    print(post['title'])
    print(post['link'])
