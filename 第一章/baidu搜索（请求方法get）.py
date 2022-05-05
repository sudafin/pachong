import requests

myinput = input("you like star who is")
url = f'https://www.baidu.com/s?ie=UTF-8&wd={myinput}'
dic = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/97.0.4692.99 Safari/537.36"
}
res = requests.get(url, headers=dic)
print(res.text)
with open("mybaidu.html", mode="w", encoding="utf-8") as f:
    f.write(res.text)
res.close()