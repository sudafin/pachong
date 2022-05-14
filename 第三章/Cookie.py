import requests

# 拿到cookie的数据
url = "https://passport.17k.com/ck/user/login"
session = requests.session()
data = {
    "loginName": "18826377454",
    "password": "a1148199284"
}
resp = session.post(url, data=data)

# 拿书架的数据

newUrl = "https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919"

newResp = session.get(newUrl)
print(newResp.json())

# 也可以在header里面将已经登录好的cookie数据添加进去
