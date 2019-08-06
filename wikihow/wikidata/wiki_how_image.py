import datetime
import re
import urllib.request

from bs4 import BeautifulSoup


def get_text_wiki(lil):
    global ordinal
    content = [lil.getText().split('\n')]
    # print(content)
    final_text_wiki = []

    for i in content:
        pattern4 = re.compile(r'WH.(\w+\.)(\w+).*|googletag.(\w+\.)(\w+).*|//.*|^if.*')
        p = len(i)
        text4 = []
        for j in range(p):
            text = re.sub(pattern4, '', i[j])
            text4.append(text)

        _text = list(filter(None, text4))
        # print('particular text================', _text)
        ordinal = ' '.join(_text)
        final_text_wiki.append(_text)
    # print(final_text_wiki)
    # ordinal = ' '.join([ordinal_number_converter(w) for w in nltk.word_tokenize(text_value)])
    return ordinal


def get_image_wiki(lil):
    global ordinal
    regex1 = re.compile(r'https://www.wikihow.com/images/.*')
    content_lis1 = lil.find_all('img', attrs={'data-src': regex1})
    content = []
    for li in content_lis1:
        content.append(li.get('data-src'))
        ordinal = ' '.join(content)

    # print(content)
    return ordinal


def get_step_num_wiki(lil):
    global ordinal
    regex1 = re.compile(r'step_num')
    content_lis1 = lil.find_all('div', attrs={'class': regex1})
    content = []
    for li in content_lis1:
        content.append(li.get('aria-label'))
        ordinal = ' '.join(content)

    # print(content)
    return ordinal


def wiki_how_content(str_):
    # global link_preview_dict
    global new_dic, link_preview_dict
    start_time = datetime.datetime.now()
    url = str_

    page = urllib.request.urlopen(url)  # connect to website
    soup = BeautifulSoup(page, 'html.parser')

    regex = re.compile('^hasimage')

    # print(''.join([i.getText() for i in soup.find_all('div', attrs={'class': 'altblock'})]))
    l = [i.getText() for i in soup.find_all('div', attrs={'class': 'altblock'})]
    print(l)
    content_lis = soup.find_all('li', attrs={'class': regex})
    content = []
    content_dic = []
    method = 0
    for li in content_lis:
        step = get_step_num_wiki(li)
        if step == 'Step 1':
            method = method + 1
        # print(method)
        # print('li=======================', li)
        link_preview_dict = {
            'step': step,
            'description': get_text_wiki(li),
            'image': get_image_wiki(li),
        }
        content.append(link_preview_dict)
        # print(link_preview_dict)
        new_dic = {method: link_preview_dict}
        content_dic.append(new_dic)

    end_time = datetime.datetime.now()
    difference_time = end_time - start_time
    s_time = difference_time.total_seconds()
    print(s_time)
    return content_dic

# wiki_how_content('https://www.wikihow.com/Become-a-Psychotherapist')
