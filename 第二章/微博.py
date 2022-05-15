import time

import requests
import re


def Spider_weibo(number, _uid):
    for _page in range(number + 1):
        if _page >= 1:
            url = f"https://weibo.com/ajax/statuses/mymblog?uid={_uid}&page={_page}&feature=0"
            header = {
                "cookie": "SINAGLOBAL=9911472744493.422.1633357276245; UOR=,,www.baidu.com; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5OVCbA4Qb.7dyhmHqiDEuB5JpX5KMhUgL.Foqfe0-cehMNeh22dJLoI0qLxKBLBonL1h.LxK-L1-eL1KeLxK.L1KzLBo2LxKML1-2L1hBLxKnLBo2L1hqLxKnL1h-L1K5t; PC_TOKEN=a8672ea6b0; ALF=1684145602; SSOLoginState=1652609601; SCF=AhoZz0nGVTd5U8luAadBGBrprnQJpJMCE5wcKd8R5hcuBAwKi0I1fKShg8rLbk4dniu0_5D2ivjOEJY9hhTDwb0.; SUB=_2A25PhKITDeRhGeBL6FcX8CnLyz2IHXVs85TbrDV8PUNbmtAfLWn4kW9NRwv9AA5VVpJz9XVYHuJEZkqeZfNrJuHN; XSRF-TOKEN=xNRurhqU5GnZy5Q4y6KAM_P0; _s_tentry=weibo.com; Apache=5333158291038.376.1652609612912; ULV=1652609612949:52:6:1:5333158291038.376.1652609612912:1652543339517; WBPSESS=d6rd5Cp7E3_icjTnxpdvreUFMPhvUCIoZkbwGWGO-sFakLG7LRgt2pjcs71kMNC634dvIEFTjLh9oeXeb9QzLe0Kmbd75oEga148eqgFjUhAQHLEspzVQeAIO3N_s2IuK5gHKo6gkXn1VbPBU9VJjA==",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
                "referer": "https://weibo.com/liuyifeiofficial"
            }
            resp = requests.get(url, headers=header)
            dic = resp.json()
            list_dic = {}
            list_dic_value = 0
            for dicResp1_value in range(100):
                try:
                    dicResp1 = dic['data']['list'][dicResp1_value]
                    if dicResp1.get('pic_infos') is None:
                        dicResp1_value = dicResp1_value + 1
                    else:
                        list_dic[list_dic_value] = dicResp1['pic_infos']
                        list_dic_value = list_dic_value + 1
                except Exception as e:
                    break
            # 用正则表达式写出
            obj = re.compile(r"'mw2000': {'url': (?P<url>.*?), .*?}", re.S)
            for k in list_dic:
                content = obj.finditer(str(list_dic[k]))  #字节码转为string
                for t in content:
                    img_rep = requests.get(t.group("url").strip("''"), headers=header)
                    img_name = t.group("url").strip("''").split("/")[4]
                    with open("img2//" + img_name, mode='wb') as f:
                        f.write(img_rep.content)
                        print("over")
                        time.sleep(2)
                    # print(t.group("url").strip("''"))  strip是去除 split是切割


if __name__ == '__main__':
    var1 = input("请输入该人物的uid")
    var2 = input("请输入该人物要爬的页数")
    uid = int(var1)  # 将string转为int
    page = int(var2)
    Spider_weibo(page, uid)  # 输入要爬的页数和该人物的uid eg：刘亦菲为 3261134763
    print("all over")
