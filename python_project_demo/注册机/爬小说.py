import requests
from pyquery import PyQuery as pq

with open("剑来.txt", "w", encoding="utf-8") as r:
    for i in range(1, 7534):  # 7534
        resp = requests.get("http://www.jianlaixiaoshuo.com/book/{}.html".format(i))
        resp.encoding = resp.apparent_encoding
        # print(resp.text)

        doc = pq(resp.text)

        title = doc('#BookCon>h1').text()
        content = doc('#BookCon').text()

        content = content.replace("←返回列表→下一页", "")
        content = content.replace("←返回列表→下一章", "")
        content = content.replace("（雪中的番外将会在微信公众平台，欢迎关注我的微信号：fenghuo1985）", "")
        content = content.replace("cpa336_r();", "")
        content = content.replace("♂！", "")
        content = content.replace("cpa336_l();", "")

        r.write("{}\n".format(content))


