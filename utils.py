from optparse import OptionParser


def get_options():
    parser = OptionParser()
    parser.add_option("-b",
                      dest="board",
                      help="search posts in a board (required)",
                      metavar="<board name>")
    parser.add_option("-c",
                      dest="category",
                      help="search posts in a certain category",
                      default='',
                      metavar="<category>")
    parser.add_option("-k",
                      dest="keyword",
                      help="search posts with keyword",
                      default='',
                      metavar="<keyword>")
    parser.add_option("--pages",
                      dest="pages",
                      help="search posts for how many pages",
                      default=1,
                      metavar="<pages>")
    parser.add_option("--push",
                      dest="push",
                      help="search posts with push more than an amount",
                      metavar="<push amount>")
    (options, args) = parser.parse_args()
    return options


def format_push(post):
    raw_push = post.find('div', {'class': 'nrec'}).text.strip()
    if not raw_push:
        push = 'NA'
    elif len(raw_push) < 2 and raw_push != '爆':
        push = ' ' + raw_push
    else:
        push = raw_push
    return push
