from urllib.request import urlopen

url = "https://docs.unity.cn/cn/2020.2/ScriptReference/index.html"
resp = urlopen(url)

with open(" mybaidu.html", mode="w", encoding="UTF-8") as f:
    f.write(resp.read().decode("utf-8"))
print("over!")
