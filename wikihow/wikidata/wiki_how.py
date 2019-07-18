import datetime
import re
import urllib.request

from bs4 import BeautifulSoup

from .models import Content
from .wiki_how_search import search


def wiki_how_content(str_, user_text):
    global final_text, url, page
    start_time = datetime.datetime.now()
    url = str_
    # url_l = "https://www.wikihow.com/" + str_
    # url = url_l.lower()
    # try:
    #     page = urllib.request.urlopen(url)  # connect to website
    # except:
    #     item = search(str_)
    #     url = item.lower()
    #     page = urllib.request.urlopen(url)

    page = urllib.request.urlopen(url)  # connect to website
    soup = BeautifulSoup(page, 'html.parser')

    regex = re.compile('^steps')

    content_lis = soup.find_all('div', attrs={'class': regex})
    content = []
    for li in content_lis:
        content.append(li.getText().split('\n'))

    final_text = []

    for i in content:

        pattern = re.compile(r'WH.(\w+\.)(\w+).*')
        pattern2 = re.compile(r'googletag.(\w+\.)(\w+).*')
        pattern3 = re.compile(r'//.*')
        pattern4 = re.compile(r'^if.*')

        p = len(i)
        text1 = []
        text2 = []
        text3 = []
        text4 = []

        for j in range(p):
            text = re.sub(pattern, '', i[j])
            text1.append(text)
            text = re.sub(pattern2, '', text1[j])
            text2.append(text)
            text = re.sub(pattern3, '', text2[j])
            text3.append(text)
            text = re.sub(pattern4, '', text3[j])
            text4.append(text)

        _text = list(filter(None, text4))
        final_text.append(_text)

    end_time = datetime.datetime.now()
    difference_time = end_time - start_time
    s_time = difference_time.total_seconds()

    url_ = url.replace('https://www.wikihow.com/', '')

    if final_text:
        data_content = Content.objects.create(url_text=url_, user_text=user_text, content=final_text, scrape_time=s_time, url=url)
        data_content.save()
        return final_text, url_
    else:
        final_text = None
        return final_text, url_

# str_url = "Fill-a-Propane-Tank"
# print("Time      :", timeit.Timer('f(str_url)', 'from __main__ import str_url,wiki_how_content as f').timeit(1))
