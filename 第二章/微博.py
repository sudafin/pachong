import requests
import re

url = "https://weibo.com/ajax/statuses/mymblog?uid=3261134763&page=2&feature=0"
header = {
    "cookie": "SINAGLOBAL=9911472744493.422.1633357276245; UOR=,,www.baidu.com; wb_view_log=1280*8011.75; PC_TOKEN=422d45d86a; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5OVCbA4Qb.7dyhmHqiDEuB5JpX5KMhUgL.Foqfe0-cehMNeh22dJLoI0qLxKBLBonL1h.LxK-L1-eL1KeLxK.L1KzLBo2LxKML1-2L1hBLxKnLBo2L1hqLxKnL1h-L1K5t; ALF=1684047380; SSOLoginState=1652511381; SCF=AhoZz0nGVTd5U8luAadBGBrprnQJpJMCE5wcKd8R5hcusGy8oDBoHNpo45-HtpX7yugh628gpxjFO8M4whud-V4.; SUB=_2A25PeyLIDeRhGeBL6FcX8CnLyz2IHXVs8RMArDV8PUNbmtB-LVThkW9NRwv9ABrsahg730JSl2IroMGgL8TlCHHk; XSRF-TOKEN=W37Kon10rjZu7EdgSvw9MlWf; _s_tentry=weibo.com; Apache=246581314387.575.1652511406184; ULV=1652511406196:50:4:3:246581314387.575.1652511406184:1652496857665; WBPSESS=d6rd5Cp7E3_icjTnxpdvreUFMPhvUCIoZkbwGWGO-sFakLG7LRgt2pjcs71kMNC634dvIEFTjLh9oeXeb9QzLeAIz_5QPhNNFbmLH3Z1q4v-Dp8kw8SK8wKxlrf47v2I_kp3ufAvQ-5wkwGknwryyQ==",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
    "referer": "https://weibo.com/liuyifeiofficial"
}
resp = requests.get(url, headers=header)
dic = resp.json()
list_dic = {}
j = 0
for i in range(100):
    try:
        dicResp1 = dic['data']['list'][i]
        if dicResp1.get('pic_infos') is None:
            i = i + 1
        else:
            list_dic[j] = dicResp1['pic_infos']
            j = j + 1
    except:
        break
# 用正则表达式写出
obj = re.compile(r"'mw2000': {'url': (?P<url>.*?), .*?}", re.S)
for k in list_dic:
    content = obj.finditer(str(list_dic[k]))
    for t in content:
        print(t.group("url").strip("''"))  # strip是去除 split是切割
