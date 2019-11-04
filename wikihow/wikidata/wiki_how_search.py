import bs4
import requests


def _get_html(url):
    headers = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0"}
    r = requests.get(url, headers=headers)
    html = r.text.encode("utf8")
    return html


def search(search_term):
    search_url = "http://www.wikihow.com/wikiHowTo?search="
    search_term_query = search_term.replace(" ", "+")
    search_url += search_term_query
    html = _get_html(search_url)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    list_ = []
    links = soup.findAll('a', attrs={'class': "result_link"})
    for link in links:
        url = link.get('href')
        list_.append(url)
    return list_[0]
