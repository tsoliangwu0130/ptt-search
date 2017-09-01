import requests
from bs4 import BeautifulSoup
from optparse import OptionParser

# option parser
parser = OptionParser()
parser.add_option("-b",
                  "--boardname",
                  dest="boardname",
                  help="Board name to search",
                  metavar="BOARD")
(options, args) = parser.parse_args()

PTT_BASE_URL = 'https://www.ptt.cc/bbs/'

res = requests.get(PTT_BASE_URL + options.boardname)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())
