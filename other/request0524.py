import requests
from bs4 import BeautifulSoup

url="https://www.ptt.cc/bbs/LoL/index.html"

def get_all_href(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    results = soup.select("div.title")
    for item in results:
        a_item = item.select_one("a")
        title = item.text
        if a_item:
            print(title, 'https://www.ptt.cc'+ a_item.get('href'))

get_all_href(url)