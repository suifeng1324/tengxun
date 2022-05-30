# author:yangleiw
# createdate:2022/5/21

import re
import tkinter as tk
import webbrowser
# import win32api
import requests

def dy():
    url = 'http://www.qmye.cn/'
    responed = requests.get(url)
    # responed.encoding = 'UTF-8'
    responed.encoding = responed.apparent_encoding  # 自动识别编码，防止乱码
    responeds = responed.text
    # 使用正则获取地址
    reg = re.compile('value="(.*?)"?url=')
    print(reg)
    res = re.findall(reg, responeds)

    url_one = res[0] + "url=" + ""
    url_two = res[1] + "url=" + ""
    url_three = res[2] + "url=" + ""

    reg = re.compile('value="(.*?)"?v=')
    res = re.findall(reg, responeds)
    url_four = res[0] + "v=" + ""
    print(url_one, url_two, url_three, url_four)
    # 设计界面GUI

    root = tk.Tk()
    root.geometry("500x220")
    root.title("杨磊制作VIP电影播放")
    lable1 = tk.Label(root, text='播放接口：')
    lable1.grid(row=0, column=0)
    # value的值会传给variable，variable=var
    var = tk.StringVar()
    var.set('empty')
    radio1 = tk.Radiobutton(root, text="vip专用解析1", variable=var, value=url_one)
    radio1.grid(row=0, column=1)
    radio2 = tk.Radiobutton(root, text="优酷腾讯通道", variable=var, value=url_two)
    radio2.grid(row=1, column=1)
    radio3 = tk.Radiobutton(root, text="电视剧解析1", variable=var, value=url_three)
    radio3.grid(row=2, column=1)
    radio4 = tk.Radiobutton(root, text="Blibi站解析1", variable=var, value=url_four)
    radio4.grid(row=3, column=1)
    lable2 = tk.Label(root, text='播放链接：')
    lable2.grid(row=4, column=0)
    text1 = tk.Entry(root, text="", width=50)
    text1.grid(row=4, column=1)


    def bf():  # 播放
        webbrowser.open(var.get() + text1.get())


    button1 = tk.Button(root, text="播放", width=8, command=bf)
    button1.grid(row=5, column=1)


    def qc():  # 清除
        text1.delete(0, "end")


    button2 = tk.Button(root, text="清除", width=8, command=qc)
    button2.grid(row=6, column=1)

    # button2 = tk.Button(root, text="",width=8)
    # button2.grid(row=5, column=1)

    # 菜单
    menubar = tk.Menu(root)  # 实例化菜单
    helpmenu = tk.Menu(menubar, tearoff=0)  # 在菜单上生成子菜单
    menubar.add_cascade(label='帮助(H)', menu=helpmenu)  # 增加一个主菜单选项


    def helpmsg():
        print("hello")


    helpmenu.add_command(label='帮助文档', command=helpmsg)
    helpmenu.add_command(label='作者信息')
    root.config(menu=menubar)

    root.mainloop()  # 一直刷新窗口，否则一开就关闭了

dy()

# 打包环境为EXE
# pip install pyinstaller
# pip install
# pyinstaller -F -w *.py