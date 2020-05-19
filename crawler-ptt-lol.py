# import requests
# from bs4 import BeautifulSoup

# article_href = []

# # 請求.取得LOL看板連結
# r = requests.get("https://www.ptt.cc/bbs/LoL/index.html")
# # bs4分析.儲存網頁內容
# soup = BeautifulSoup(r.text,"html.parser")
# # 因為文章包在<div class="title">裡面
# # 選擇網頁內所有是div,且class為title的段落
# results = soup.select("div.title")
# # 印出搜尋結果(results為清單list)
# print(results)

# # 把results清單內的段落用迴圈一個個帶入item
# for item in results:
#     # 篩選出每個段落<a herf>內的超連結 
#     item_href = item.select_one("a").get("href")
#     article_href.append(item_href)
# # 印出結果(同頁所有文章的超連結)
# print(article_href)

# # 做翻頁功能
# # 找出<div class="btn-group">內所有a開頭的段落
# btn = soup.select('div.btn-group > a')
# # 找出btn清單內[上頁]的超連結(3)
# up_page_href = btn[3]['href']
# # 將ptt域名和上頁的超連結組合在一起
# next_page_url = 'https://www.ptt.cc' + up_page_href
# # 印出結果(上頁的完整超連結)
# print(next_page_url)

# # 用for迴圈定義要抓幾頁(預設4頁)
# url="https://www.ptt.cc/bbs/LoL/index.html"
# for page in range(1,4):
#     r = requests.get(url)
#     soup = BeautifulSoup(r.text,"html.parser")
#     btn = soup.select('div.btn-group > a')
#     up_page_href = btn[3]['href']
#     next_page_url = 'https://www.ptt.cc' + up_page_href
#     url = next_page_url
#     print(url)


import requests
from bs4 import BeautifulSoup
url="https://www.ptt.cc/bbs/LoL/index.html"

pages = input('請輸入頁數：')

def get_all_href(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    results = soup.select("div.title")
    for item in results:
        a_item = item.select_one("a")
        title = item.text
        if a_item:
            print(title, 'https://www.ptt.cc'+ a_item.get('href'))
        
for page in range(1,pages):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    btn = soup.select('div.btn-group > a')
    up_page_href = btn[3]['href']
    next_page_url = 'https://www.ptt.cc' + up_page_href
    url = next_page_url
    get_all_href(url = url)
