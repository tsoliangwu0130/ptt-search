import requests
from bs4 import BeautifulSoup
from optparse import OptionParser

PTT_BASE_URL = 'https://www.ptt.cc'

# option parser
parser = OptionParser()
parser.add_option("-b",
                  "--boardname",
                  dest="boardname",
                  help="Board name to search",
                  metavar="BOARD")
(options, args) = parser.parse_args()

html_doc = requests.get('{}/bbs/{}'.format(PTT_BASE_URL, options.boardname))
soup = BeautifulSoup(html_doc.text, 'html.parser')

post_list = []
for post in soup.find_all('div', {'class': 'title'}):
    title = post.text
    link = post.find('a')['href']
    post_list.append({'title': title, 'link': PTT_BASE_URL + link})

print(post_list)
