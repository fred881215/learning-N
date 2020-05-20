# 導入 requests
import requests

# 導入 urllib
import urllib

# 導入 BeautifulSoup
from bs4 import BeautifulSoup

# 原始 HTML 程式碼
html_doc = """
<html><head><title>Hello World</title></head>
<body><h2>Test Header</h2>
<p>This is a test.</p>
<a id="link1" href="/my_link1">Link 1</a>
<a id="link2" href="/my_link2">Link 2</a>
<p>Hello, <b class="boldtext">Bold Text</b></p>
</body></html>
"""

# 以 Beautiful Soup 解析 HTML 程式碼
soup = BeautifulSoup(html_doc, 'html.parser')

# 輸出排版後的 HTML 程式碼
print(soup.prettify())

# 網頁標題 HTML 標籤
title_tag = soup.title
print(title_tag)

# 網頁的標題文字
print(title_tag.string)

# 所有的超連結
a_tags = soup.find_all('a')
for tag in a_tags:
  # 輸出超連結的文字
  print(tag.string)

for tag in a_tags:
  # 輸出超連結網址
  print(tag.get('href'))

# 搜尋所有超連結與粗體字
tags = soup.find_all(["a", "b"])
print(tags)

# 限制搜尋結果數量
tags = soup.find_all(["a", "b"], limit=2)
print(tags)

# 只抓出第一個符合條件的節點
a_tag = soup.find("a")
print(a_tag)

# 預設會以遞迴搜尋
soup.html.find_all("title")

# 不使用遞迴搜尋，僅尋找次一層的子節點
soup.html.find_all("title", recursive=False)

# 根據 id 搜尋
link2_tag = soup.find(id='link2')
print(link2_tag)

# 搜尋 href 屬性為 /my_link1 的 a 節點
a_tag = soup.find_all("a", href="/my_link1")
print(a_tag)

