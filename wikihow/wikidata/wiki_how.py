import datetime
import re
import timeit
import urllib.request

from bs4 import BeautifulSoup
from .models import Content


# str_url = "Fill-a-Propane-Tank"


def wiki_how_content(str_):
    global final_text
    start_time = datetime.datetime.now()

    # url = "https://www.wikihow.com/Fill-a-Propane-Tank"
    url = "https://www.wikihow.com/" + str_
    page = urllib.request.urlopen(url)  # conntect to website
    try:
        page = urllib.request.urlopen(url)
    except ConnectionError as e:
        print("An error occured.")

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
        # print(_text)
        final_text.append(_text)
        # print(final_text)
    end_time = datetime.datetime.now()
    difference_time = end_time - start_time
    print(difference_time.total_seconds())
    data_content = Content.objects.create(url_text=str_, content=final_text, scrape_time=difference_time)
    data_content.save()
    return final_text

# print("Time      :", timeit.Timer('f(str_url)', 'from __main__ import str_url,wiki_how_content as f').timeit(1))
