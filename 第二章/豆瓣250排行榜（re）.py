import csv

import requests
import re

# 提取url的源代码
url = "https://movie.douban.com/top250"
headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHT"
}
res = requests.get(url=url, headers=headers)
resText = res.text
# 使用re来获取内容 预加载正则
obj = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?'
                 r'<span class="rating_num" property="v:average">(?P<rating>.*?)</span>.*?<span>('
                 r'?P<stars>.*?)</span>', re.S)
# ‘’不要使用""，原文已经有""
f = open("mydata.csv", mode="w", encoding="UTF-8")
csvWriter = csv.writer(f)
content = obj.finditer(resText)
for i in content:
    # print(i.group("name"))
    # print(i.group("year").strip())  # year前面有文字，所以存在空白，所以使用strip来消除空格带来的空白
    # print(i.group("rating"))
    # print(i.group("stars"))
    dic = i.groupdict()  # 创建一个字典
    dic['year'] = dic['year'].strip()  # 切割里面year的数据
    csvWriter.writerow(dic.values())  # 将dic的值写入到csv文件里
f.close()
res.close()
print("over!")
