import requests

url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"

headers = {
    'Cookie': 'BIDUPSID=6479CBF9EC50F730E9701FC28E041593; PSTM=1625534087; __yjs_duid=1_fda9a329d89b86ad9f076dceab74387d1625549156544; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; MCITY=-%3A; APPGUIDE_10_0_2=1; BAIDUID=BCC4CDF594543E90B41374153BD94625:FG=1; BDUSS=S03LXdxZk9pY0l6OXdsblQ2Vms5WUs5MlFXYXQ0LTlNbDJha2FRdmxBZHJrYkppSVFBQUFBJCQAAAAAAAAAAAEAAAClazJXAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGsEi2JrBItiW; BDUSS_BFESS=S03LXdxZk9pY0l6OXdsblQ2Vms5WUs5MlFXYXQ0LTlNbDJha2FRdmxBZHJrYkppSVFBQUFBJCQAAAAAAAAAAAEAAAClazJXAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGsEi2JrBItiW; BAIDUID_BFESS=BCC4CDF594543E90B41374153BD94625:FG=1; BA_HECTOR=8la581a50184a5ah251h8mced15; ZFY=oGypW0Gn:AmrVKYymqhwRen03EEZ2rSFu6hWINgy06uE:C; BDRCVFR[Qs-Y_7gNldt]=OjjlczwSj8nXy4Grjf8mvqV; delPer=0; PSINO=5; ZD_ENTRY=baidu; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=36425_36460_36455_31254_36423_36165_35979_36055_36235_26350_36468_36312_36447; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1653105506,1653115941,1653234734,1653309089; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1653309089; ab_sr=1.0.1_ZThhNTMyMmI1NTM0ZWEzYjUxNDAxZmUxMTY3NTRmNWQ3ZjlhYmE4YjU2NWUwYjRhYmUxNTUxYjExZDVhMzcxNDE4N2U3NjlkY2VhMjI3MGRkOTdkOWQ3NTc3MDNjMmNhMGI1N2U5NDEyNmFhMDg2ZmIzYTgyMDE2ZTczZmVjODBmMTNiYWRlOTViMTkwMjVhYzgyMmFhNWU4YjNjOTJjOTI3MTFmMGM3ZWRhYTY2MDA3YTIxNGU1MTliM2RiNTYx',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

data = {
    'from': 'en',
    'to': 'zh',
    'query': 'enter',
    'transtype': 'translang',
    'simple_means_flag': '3',
    'sign': '571025.808352',
    'token': '143cb03f796000fa7ff3b1ea18b8e7ee',
    'domain': 'common',
}

resp = requests(url, data=data, headers=headers)
print(resp.text)
