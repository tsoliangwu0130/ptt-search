import math
from optparse import OptionParser


def get_options():
    parser = OptionParser()
    parser.add_option('-b',
                      dest='board',
                      help='search posts in a board (required)',
                      metavar='<board name>')
    parser.add_option('-c',
                      dest='category',
                      help='search posts in a certain category',
                      default='',
                      metavar='<category>')
    parser.add_option('-k',
                      dest='keyword',
                      help='search posts with keyword',
                      default='',
                      metavar='<keyword>')
    parser.add_option('-p',
                      dest='pages',
                      help='search posts for how many pages',
                      default=1,
                      metavar='<page amount>')
    parser.add_option('-z',
                      dest='push',
                      help='search posts with push more than an amount',
                      metavar='<push amount>')
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


def is_greater(cur_push, push_amount):
    if not push_amount:
        return True
    elif cur_push == '爆':
        return math.inf >= int(push_amount)
    elif cur_push == 'NA':
        return 0 >= int(push_amount)
    elif cur_push.startswith('X'):
        return -math.inf >= int(push_amount)
    else:
        return int(cur_push) >= int(push_amount)
