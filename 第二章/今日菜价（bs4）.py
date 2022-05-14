from bs4 import BeautifulSoup

import requests

import re

url = "http://www.dongbao120.com/jinrizhujia/"
resp = requests.get(url)

# 1、把页面源代码交给BeautifulSoup进行处理，生成bs对象
page = BeautifulSoup(resp.text, "html.parser")
# 2、从bs对象中查找数据
# find(标签，属性=值)
# find_all(标签，属性=值)

List_data = []
t1body = page.find("table", class_="jinrizhujia")
# 拿到除了第一行的数据的每行数据
trs = t1body.find_all("tr")[1:]
for i in trs:
    tds = i.find_all("td")  # 拿到每一行每一列的数据
    name1 = tds[0].text  # 拿到标记的内容 html内容
    name2 = tds[1].text
    name3 = tds[2].text
    name4 = tds[3].text
    name5 = tds[4].text
# 上面完成但这里会出现大量空格需要
    List_data.append(name1)
    List_data.append(name2)
    List_data.append(name3)
    List_data.append(name4)
    List_data.append(name5)
obj1 = re.compile(r"\w+", re.S)
for k in List_data:
    res = k
    rese1 = obj1.finditer(res)
    for i in rese1:
        print(i.group().strip('\n'))
