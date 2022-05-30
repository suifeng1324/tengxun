import re

import requests

# 使用正则表达式 替换 (.*?)": "(.*)  替换 "$1": "$2",
"""
市面上免费的IP
http://www.66ip.cn/1.html
http://www.ip3366.net/free/?stype=1&page=1
http://www.kuaidaili.com/free/inha/1/1
http://www.xicidaili.com/nn/1
http://www.ip3366.net/?stype=1&page=1
http://www.iphai.com/
http://www.data5u.com/free/gngn/index.shtml
"""
for i in range(1, 5):

    url = "https://free.kuaidaili.com/free/inha/{}".format(i)
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "channelid=0; sid=1653123610628714; _gcl_au=1.1.1720013535.1653125029; _ga=GA1.2.1625103030.1653125029; _gid=GA1.2.1924985422.1653125029; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1653125029,1653140676; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1653141282",
        "Host": "free.kuaidaili.com",
        "sec-ch-ua": "' Not A;Brand';v='99', 'Chromium';v='101', 'Google Chrome';v='101'",
        "sec-ch-ua-platform": "Windows",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
    }

    responeds = requests.get(url, headers=headers).text
    # print(responeds)
    """
    <td data-title="IP">120.220.220.95</td>
    <td data-title="PORT">8085</td>
    """
    reg = re.compile('<td data-title="IP">(.*?)</td>')
    ips = re.findall(reg, responeds)
    # ips = re.findall('<td data-title="IP">(\d+\.\d+\.\d+\.\d+)</td>', responeds, re.S) # re另一个写法
    ports = re.findall('<td data-title="PORT">(\d+)</td>', responeds, re.S)
    # print(ips, ports)
    # 将ip和端口绑定
    for ip in zip(ips, ports):
        # 使用ip请求百度，判断IP是否可用
        proxies = {
            "http": "http://" + ip[0] + ":" + ip[1],  # http://ip:port
            "https": "https://" + ip[0] + ":" + ip[1],
        }
        try:
            res = requests.get("http://www.baidu.com", proxies=proxies, timeout=3)
            print(ip, "true")
            # 保存可用使用的ip
            with open("ip.text", mode="a+") as f:
                f.write(":".join(ip) + '\n')
        except Exception as e:
            print(ip, "false")
