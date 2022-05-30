import tkinter as tk
from tkinter import messagebox

from PIL import ImageTk


def love():
    love_root = tk.Toplevel(root)
    love_root.title('嘻嘻！')
    love_root.geometry("300x100")
    tk.Label(love_root, text="我也是哦", font=24).pack()
    tk.Button(love_root, text="确定", command=stop).pack()


def stop():
    root.quit()


def no():
    messagebox.showwarning(title="哦，no",message="再想想吧")


root = tk.Tk()
root.title("你喜欢我嘛")
root.geometry('385x440+250+220')

tk.Label(root, text='hey,小姐姐', font=('微软雅黑', 14), fg='red', ).grid(row=0, column=0)
# N S W E上下左右
tk.Label(root, text='喜欢我吗？', font=('微软雅黑', 30), ).grid(row=1, column=1, sticky=tk.E)
bm = ImageTk.PhotoImage(file='./1.png')
tk.Label(root, image=bm).grid(row=2, columnspan=2)
tk.Button(root, text='喜欢', width=15, height=2, command=love).grid(row=3, column=0, sticky=tk.W)
tk.Button(root, text='不喜欢', width=5, height=1, command=no).grid(row=3, column=1, sticky=tk.E)

root.mainloop()
