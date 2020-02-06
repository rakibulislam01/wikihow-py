import datetime
import json
import os
import re
import urllib.request

from bs4 import BeautifulSoup

from contribute.models import Content


def get_text_wiki(lil):
    """
    Get content from wikihow_skill page and format it.
    :param lil: html tag content.
    :return: format content.
    """
    global ordinal
    content = [lil.getText().split('\n')]
    final_text_wiki = []

    for i in content:
        pattern4 = re.compile(r"WH.(\w+\.)(\w+).*|googletag.(\w+\.)(\w+).*|//.*|^if.*|var img = document.getElementById.*|defer.*|(\[\d*\])")
        p = len(i)
        text4 = []
        for j in range(p):
            text = re.sub(pattern4, "", i[j])
            text4.append(text)

        _text = list(filter(None, text4))
        del _text[0]
        ordinal = " ".join(_text)
        final_text_wiki.append(_text)
    return ordinal


def get_image_wiki(lil):
    """
    Get image link form content and serialize that content.
    :param lil: html tag content.
    :return: Image link each step.
    """
    global ordinal
    regex1 = re.compile(r"https://www.wikihow.com/images/.*")
    content_lis1 = lil.find_all("video", attrs={"data-poster": regex1})
    content_lis2 = lil.find_all("img", attrs={"data-src": regex1})
    content = []

    if content_lis2:
        for li in content_lis2:
            content.append(li.get("data-src"))
            ordinal = " ".join(content)
    else:
        for li in content_lis1:
            content.append(li.get("data-poster"))
            ordinal = " ".join(content)

    return ordinal


def get_step_num_wiki(lil):
    """
    Get step number from wikihow_skill website.
    :param lil: html tag content.
    :return: step number
    """
    global ordinal
    regex1 = re.compile(r"step_num")
    content_lis1 = lil.find_all("div", attrs={"class": regex1})
    content = []
    for li in content_lis1:
        content.append(li.get("aria-label"))
        ordinal = " ".join(content)

    # print(content)
    return ordinal


def wiki_how_content(str_, user_text):
    """
    It's the main function call form view file.
    :param str_: url link. Which is search form wikihow_skill search function.
    :param user_text: user input.
    :return:
    """
    global new_dic, link_preview_dict, method
    start_time = datetime.datetime.now()
    url = str_

    page = urllib.request.urlopen(url)  # connect to website
    soup = BeautifulSoup(page, "html.parser")

    regex = re.compile("^hasimage")

    # print("".join([i.getText() for i in soup.find_all("div", attrs={"class": "altblock"})]))
    l = [i.getText() for i in soup.find_all("div", attrs={"class": "altblock"})]
    content_lis = soup.find_all("li", attrs={"class": regex})
    content = []
    content_dic = []
    method1 = 0
    para = 0
    status = 1
    for li in content_lis:

        step = get_step_num_wiki(li)

        link_preview_dict = {
            "step": step,
            "description": get_text_wiki(li),
            "image": get_image_wiki(li),
        }
        if para != 0:
            if step == "Step 1":
                method = l[method1].rstrip()
                if method == "Method 1":
                    status = 0
                method1 += 1
                new_dic = {"Part": content}
                content_dic.append(new_dic)
                content = []

        content.append(link_preview_dict)
        para += 1

    method = l[method1].rstrip()
    method1 += 1
    new_dic = {"Part": content}
    content_dic.append(new_dic)

    # Calculate time difference.
    end_time = datetime.datetime.now()
    difference_time = end_time - start_time
    s_time = difference_time.total_seconds()
    url_ = url.replace("https://www.wikihow.com/", "")
    folder_path = "/home/rakibul/PycharmProjects/willy_debug_8010/media/"

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    if content_dic:
        with open(folder_path + user_text + '.json', 'w') as outfile:
            json.dump(content_dic, outfile, indent=4, sort_keys=True)

        try:
            first_text = content_dic[0]['Part'][0]['step'] + ' ' + content_dic[0]['Part'][0]['description'] + '    ' + \
                         content_dic[0]['Part'][1]['step'] + ' ' + content_dic[0]['Part'][1]['description'] + '    ' + \
                         content_dic[0]['Part'][2]['step'] + ' ' + content_dic[0]['Part'][2]['description']
        except:
            first_text = content_dic[0]['Part'][0]['step'] + ' ' + content_dic[0]['Part'][0]['description'] + '    ' + \
                         content_dic[0]['Part'][1]['step'] + ' ' + content_dic[0]['Part'][1]['description']

        data_content = Content.objects.create(url_text=url_, user_text=user_text, scrape_time=s_time, url=url, steps=first_text, json_file=user_text + ".json")
        data_content.save()

        return first_text
    else:
        content_dic = None
        first_text = None
        return first_text
    # return content_dic

# wiki_how_content("https://www.wikihow.com/Become-a-Psychotherapist")
