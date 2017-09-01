import requests
from bs4 import BeautifulSoup
from optparse import OptionParser

PTT_BASE_URL = 'https://www.ptt.cc'

# option parser
parser = OptionParser()
parser.add_option("-b",
                  dest="board",
                  help="board name to search",
                  metavar="<board name>")
parser.add_option("-q",
                  dest="query",
                  help="query for post title",
                  metavar="<query>")
(options, args) = parser.parse_args()

html_doc = requests.get('{}/bbs/{}'.format(PTT_BASE_URL, options.board))
soup = BeautifulSoup(html_doc.text, 'html.parser')

post_list = []
for post in soup.find_all('div', {'class': 'title'}):
    title = post.text
    link = post.find('a')['href']
    if options.query in title:
        post_list.append({'title': title, 'link': PTT_BASE_URL + link})

for post in post_list:
    print(post['title'])
    print(post['link'])
