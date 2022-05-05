import requests

import re

import csv

url = "https://www.ibttt.net"
resp = requests.get(url)  # 去掉安全验证
resp.encoding = "utf-8"  # 根据网页自身的编码决定，默认utf-8

obj1 = re.compile(r'<div class="item cl">.*?</span>(?P<html>.*?)<b><font color="#FF6600">.*?(?P<movieName>.*?)<i>',
                  re.S)
obj2 = re.compile(r'".*?(?P<bt>.*?)"', re.S)
obj3 = re.compile(r'<div class="sl cl">.*? href="(?P<realBt>.*?)"', re.S)
List_newBt = []  # 本质是一个列表['10086', '10001']
List_newName = []
content1 = obj1.finditer(resp.text)
for i in content1:
    List_newName.append(i.group('movieName'))
    html = i.group('html')
    content2 = obj2.finditer(html)
    for j in content2:
        List_newBt.append(j.group().strip('""'))
f = open("btData.text", mode='w', encoding='utf-8')
i = 0
for t in List_newBt:
    resp_url = requests.get(t)
    content3 = obj3.finditer(resp_url.text)
    for k in content3:
        # print(List_newName[i])
        # print(k.group('realBt'))
        f.write(List_newName[i]+"\n"+k.group('realBt')+"\n")
        i = i + 1
    resp_url.close()
f.close()
resp.close()
print("over")
