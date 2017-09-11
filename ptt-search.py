import requests
from bs4 import BeautifulSoup

from utils import format_date, format_push, get_options, is_greater

# constant variables
PTT_BASE_URL = 'https://www.ptt.cc'
PTT_OVER_18_URL = PTT_BASE_URL + '/ask/over18'


# fetch posts from ptt
def fetch_post(options, url):
    result_cnt = 0
    page_cnt = 0
    page_limit = 10
    post_list = []
    cur_url = url

    while True:
        try:
            page_cnt += 1
            # request and parse current page
            reqs = requests.session()
            html_doc = reqs.get(cur_url)
            soup = BeautifulSoup(html_doc.text, 'html.parser')

            # post payload if there is over18 check
            if soup.find('div', {'class': 'over18-notice'}):
                payload = {
                    'from': cur_url,
                    'yes': 'yes'
                }
                reqs.post(PTT_OVER_18_URL, data=payload)
                html_doc = reqs.get(cur_url)
                soup = BeautifulSoup(html_doc.text, 'html.parser')

            prev_url = soup.find('div', {'class': 'btn-group-paging'}).findChildren()[1]['href']

            # fetch posts from current page
            for post in soup.find_all('div', {'class': 'r-ent'}):
                post_title = post.find('div', {'class': 'title'})
                title = post_title.text
                link = 'URL not found' if not post_title.find('a') else PTT_BASE_URL + post_title.find('a')['href']
                push = format_push(post)
                if options.category in title and options.keyword in title and is_greater(push, options.push_num):
                    date = format_date(post)
                    author = post.find('div', {'class': 'author'}).text
                    post_list.append({'date': date,
                                      'push': push,
                                      'author': author.strip(),
                                      'title': title.strip(),
                                      'link': link.strip()})
                    result_cnt += 1
                    if result_cnt >= int(options.result_num):
                        return post_list
            cur_url = PTT_BASE_URL + prev_url
            if page_cnt == page_limit:
                print('Found only {} results in {} pages'.format(len(post_list), page_limit))
                ans = input('Do you want keep searching (y/n)?')
                if ans == 'y':
                    page_limit += 10
                else:
                    return post_list
        except:
            print('Ok, something went wrong :(')
            exit()


# print fetched posts and links
def print_post(post_list):
    if post_list:
        sorted_list = sorted(post_list, key=lambda x: x['date'])
        for post in sorted_list:
            print('{} {} <{}> {} ({})'.format(post['date'], post['push'], post['author'], post['title'], post['link']))
        print('\n' + 'Found {} posts.'.format(len(sorted_list)))
    else:
        print('Result not found.')


if __name__ == "__main__":
    options = get_options()
    entry_url = '{}/bbs/{}'.format(PTT_BASE_URL, options.board)

    post_list = fetch_post(options, entry_url)
    print_post(post_list)
