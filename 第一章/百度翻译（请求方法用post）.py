# 有form data

import requests
url = " https://fanyi.baidu.com/sug"
s = input("你要翻译的单词\n")
mydata = {
    "kw": s
}
resp = requests.post(url, data=mydata)
print(resp.json())
resp.close()