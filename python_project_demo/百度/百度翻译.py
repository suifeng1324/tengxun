"""
@Author :       yangleiw
@File   :       .py
@Time   :       2022年05月22日 23:12
@Desc   :
"""
# -*- coding: utf-8 -*-

# This code shows an example of text translation from English to Simplified-Chinese.
# This code runs on Python 2.7.x and Python 3.x.
# You may install `requests` to run this code: pip install requests
# Please refer to `https://api.fanyi.baidu.com/doc/21` for complete api document
import json
import tkinter as tk

import requests


def access_token():
    url = "https://aip.baidubce.com/oauth/2.0/token"
    headers = {
        "Content-Type": "application/json;charset=utf-8"
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": "wPXXMe6WY3ERKmSc72U6q6kw",
        "client_secret": "yZGUNhiP2j3wLZuI7ZbrIobyRDLt1y3P",
    }

    r = requests.post(url, params=data, headers=headers).text
    res = json.loads(r)
    print(res["access_token"])
    return res["access_token"]


def info():
    token = access_token()
    url = 'https://aip.baidubce.com/rpc/2.0/mt/texttrans/v1?access_token=' + token

    q = text_str_var.get();  # example: hello
    # For list of language codes, please refer to `https://ai.baidu.com/ai-doc/MT/4kqryjku9#语种列表`
    from_lang = source_str_var.get();  # example: en
    to_lang = target_str_var.get();  # example: zh

    # Build request
    headers = {'Content-Type': 'application/json'}
    payload = {'q': q, 'from': from_lang, 'to': to_lang}

    # Send request
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()
    d = r.text
    res = json.loads(d)
    print(res, type(res))
    res1 = res["result"]["trans_result"][0]["dst"]
    print("before:", res1)
    tk.Label(login_frame, text=res1).grid(row=4, column=2)

    # return res1
    # Show response
    # print(json.dumps(result, indent=4, ensure_ascii=False))


root = tk.Tk()
# login_page = LoginPage(root)
root.title('yangleiw制作翻译 3.0')
root.geometry("500x200")

source_str_var = tk.StringVar()
target_str_var = tk.StringVar()
text_str_var = tk.StringVar()
res_str_var = tk.StringVar()



login_frame = tk.Frame()  # 相当于一页纸
login_frame.pack()

tk.Label(login_frame).grid(row=0, column=0)  # 用空白label布局挤下框架

tk.Label(login_frame, text="源端（example: en）：").grid(row=1, column=1)
tk.Entry(login_frame, textvariable=source_str_var).grid(row=1, column=2)
tk.Label(login_frame, text="目标端（example: zh）：").grid(row=2, column=1)
tk.Entry(login_frame, textvariable=target_str_var).grid(row=2, column=2)
tk.Label(login_frame, text="待翻译(example: hello)：").grid(row=3, column=1)
tk.Entry(login_frame, textvariable=text_str_var).grid(row=3, column=2)

tk.Button(login_frame, text="查询", command=info).grid(row=5, column=1)

tk.Label(login_frame, text="翻译：").grid(row=4, column=1)

tk.Button(login_frame, text="重置").grid(row=5, column=2)
root.mainloop()  # 一直刷新窗口，否则一开就关闭了
