import requests
import csv
from bs4 import BeautifulSoup

class ppt_spider():
    start_urls = ['https://www.ptt.cc/bbs/hotboards.html']

    def __init__(self, start_urls):
        self.h_number = 0
        self.c_number = 0
        self.header = []
        self.start_urls = start_urls
    def start_requests(self):
        header = ['firstpage', 'username', 'classname', 'category_pages', 'category_title', 'category_url', 'a_title', 'a_author', 'a_date', 'note_url', 'note',]
        with open ('ptt.csv','a',encoding='utf-8') as f:
            csv_write = csv.DictWriter(f, fieldnames=header ,delimiter = ';')
            csv_write.writeheader()
            f.close()

        for url in self.start_urls:
            request_url = requests.get(url)
            self.home_page(request_url)

    def home_page(self, response):
        soup = BeautifulSoup(response.text,'lxml')
        posts1 = soup.find_all('a', class_= 'board')
        for p in posts1:
            self.h_number = self.h_number + 1
            username = p.find('div', class_= 'board-name').text
            # print(name)
            category_pages = p.select('span')[0].text
            # print(pages)
            classname = p.select('div.board-class')[0].text
            # print(classname)
            category_title = p.select('div.board-title')[0].text
            # print(title)
            category_url = 'https://www.ptt.cc' + p['href']
            # print(self.h_number, ' : ' , url)
            request_url = requests.get(
                url = category_url,
                cookies = {'over18': 'yes'}  # ptt18歲的認證
            )
            meta1 = {
                "firstpage" : str(response.url),
                "username" : str(username),
                "classname" : str(classname),
                "category_pages" : str(category_pages),
                "category_title" : str(category_title),
                "category_url" : str(category_url)
            }
            self.category_page(request_url, meta1)
    def category_page(self, response, meta1):
            self.c_number = self.c_number + 1
            soup = BeautifulSoup(response.text,'lxml')
            r_ent = soup.select('div.r-ent')[0].text
            a_url = soup.select('div.title > a')[0]['href']
            a_title = soup.select('div.title')[0].text.replace('\n','').replace('\t','')
            if '刪除' in a_title:
                a_url = a_title
                note = a_title
            else :
                note = ''

            a_author = soup.select('div.author')[0].text
            # print(a_author)
            a_date = soup.select('div.date')[0].text
            # print(a_date)
            note_url = 'https://www.ptt.cc/' + a_url

            # print(a_title)
            # print(self.c_number , ' : ' ,'https://www.ptt.cc/' + a_url)
            meta2 = {
                "a_title" : str(a_title),
                "a_author" : str(a_author),
                "a_date" : str(a_date),
                "note_url" : str(note_url),
                "note" : str(note)
            }
            meta_12 = dict(meta1.items() | meta2.items())
            request_url = requests.get(
                url = note_url,
                cookies = {'over18': 'yes'}  # ptt18歲的認證
            )
            self.note(request_url, meta_12)
    def note(self, response, meta_12):
        soup = BeautifulSoup(response.text,'lxml')
        checkpage = soup.title.text
        if '404 Not Found' in checkpage:
            pass
        else:
            meta_12["note"] = soup.select('#main-content')[0].text.split('※ 發信站')[0].replace('\n',' ')

        header = ['firstpage', 'username', 'classname', 'category_pages', 'category_title', 'category_url', 'a_title', 'a_author', 'a_date', 'note_url', 'note']
        with open ('ptt.csv','a',encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=header, delimiter = ';')

            meta_12 = {key: value for key, value in meta_12.items()if key in header}
            writer.writerow(meta_12)


a = ppt_spider()
a.start_requests()