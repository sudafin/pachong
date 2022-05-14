import requests
url = "https://www.pearvideo.com/video_1761804"
contID = url.split('_')[1]   # 得到1761735
videoUid = f"https://www.pearvideo.com/videoStatus.jsp?contId={contID}&mrd=0.3354076859432229"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39",
    "Referer": "https://www.pearvideo.com/video_1761804"
}
resp = requests.get(videoUid, headers=headers)
dic = resp.json()
srUL = dic['videoInfo']['videos']['srcUrl']  # 按从大集合到小集合找到要的那个元素
system = dic['systemTime']
srUL = srUL.replace(system, f"cont-{contID}")
with open("a.mp4",mode="wb") as f:
    f.write(requests.get(srUL).content)

# 如何批量下载？

