def format_push(post):
    raw_push = post.find('div', {'class': 'nrec'}).text.strip()
    if not raw_push:
        push = 'NA'
    elif len(raw_push) < 2 and raw_push != '爆':
        push = ' ' + raw_push
    else:
        push = raw_push
    return push
