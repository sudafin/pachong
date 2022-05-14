import requests

from bs4 import BeautifulSoup

import time

import cfscrape

scrape = cfscrape.create_scraper(delay=10)
url = "https://www.pexels.com/zh-cn/search/%E5%B9%BF%E5%B7%9E/"
resp = scrape.get(url)

main_page = BeautifulSoup(resp.text, "html.parser")
alist = main_page.find("div", class_="photos").find_all("a", class_='js-photo-link photo-item__link')
# print(alist)
i = 1
for i in alist:
    blist = i.find_all("img", class_='photo-item__img')   # 找到关键的相同词
    for j in blist:
        clist = j.get('data-big-src')  # 找到类型直接提取值
        img_rep = requests.get(clist)
        img_name = clist.split("/")[4]+".jpg"  # 切割。按空白，从1开始；按标志，从n个标准到n+1的标志之间切割，n大于等于1
        with open("img//"+img_name, mode='wb') as f:
            f.write(img_rep.content)
        print("over")
        print(clist)
        time.sleep(2)

print("all over")
resp.close()
