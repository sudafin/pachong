from lxml import etree
import requests

url = "https://guangdong.zbj.com/search/f/?kw=unity"
rep = requests.get(url)
html = etree.HTML(rep.text)

divs = html.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div")
# /html/body/div[6]/div/div/div[2]/div[5]/div[1]/div[1]/div/div/a[1]/div[1]/p/text()
# /html/body/div[6]/div/div/div[2]/div[5]/div[1]/div[2]/div/div/a[2]/div[2]/div[2]/p
# ./是相对路径其前面是divs已经写好的路径
for i in divs:
    price = i.xpath("./div/div/a[2]/div[2]/div[1]/span[1]/text()")[0].strip("¥")  # 先得到元素再切割
    company = i.xpath("./div/div/a[1]/div[1]/p/text()")[1].strip("\n")
    title = "Unity".join(i.xpath("./div/div/a[2]/div[2]/div[2]/p/text()"))  # 用unity来连接字符
    print(title+'\n'+company+'\t'+price+'元\n')