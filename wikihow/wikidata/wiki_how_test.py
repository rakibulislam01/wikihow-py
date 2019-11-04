import datetime
import re
import urllib.request

from bs4 import BeautifulSoup

from .models import Content


def wiki_how_content(str_, user_text):
    global final_text, url, page
    start_time = datetime.datetime.now()
    url = str_

    page = urllib.request.urlopen(url)  # connect to website
    soup = BeautifulSoup(page, 'html.parser')

    regex = re.compile('^steps')

    content_lis = soup.find_all('div', attrs={'class': regex})
    # print(content_lis)
    content = []
    for li in content_lis:
        content.append(li.getText().split('\n'))

    final_text = []

    for i in content:
        pattern4 = re.compile(r'WH.(\w+\.)(\w+).*|googletag.(\w+\.)(\w+).*|//.*|^if.*')

        p = len(i)
        text4 = []

        for j in range(p):
            text = re.sub(pattern4, '', i[j])
            text4.append(text)

        _text = list(filter(None, text4))
        final_text.append(_text)

    end_time = datetime.datetime.now()
    difference_time = end_time - start_time
    s_time = difference_time.total_seconds()

    url_ = url.replace('https://www.wikihow.com/', '')

    if final_text:
        data_content = Content.objects.create(url_text=url_, user_text=user_text, content=final_text,
                                              scrape_time=s_time, url=url)
        data_content.save()
        return final_text, url_
    else:
        final_text = None
        return final_text, url_
