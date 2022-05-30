"""
@Author :       yangleiw
@File   :       demo.py
@Time   :       2022年05月22日 15:57
@Desc   :
"""
import tkinter as tk

username = "yangleiw"
password = "123123"


class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title('信息管理系统 3.0')
        self.root.geometry("300x200")

        self.username_str_var = tk.StringVar()
        self.password_str_var = tk.StringVar()

        self.login_frame = tk.Frame()  # 相当于一页纸
        self.login_frame.pack()

        tk.Label(self.login_frame).grid(row=0, column=0)  # 用空白label布局挤下框架

        tk.Label(self.login_frame, text="账号：").grid(row=1, column=1)
        tk.Entry(self.login_frame, textvariable=self.username_str_var).grid(row=1, column=2)
        tk.Label(self.login_frame, text="密码：").grid(row=2, column=1)
        tk.Entry(self.login_frame, textvariable=self.password_str_var).grid(row=2, column=2)
        tk.Button(self.login_frame, text="登录", command=self.login).grid(row=3, column=1)
        tk.Button(self.login_frame, text="忘记密码").grid(row=3, column=2)

        # 点击登录按钮，获取用户信息，然后进行校验，成功后跳转

    def login(self):
        # print("用户名： ", username_str_var.get())
        # print("密码： ", password_str_var.get())
        if username == self.username_str_var.get() and self.password_str_var.get() == password:
            print("success")
            self.login_frame.destroy()  # 把登录的纸撕掉
            MainPage(self.root)
        else:
            print("fail")


class MainPage:
    def __init__(self, root):
        self.root = root
        self.root.title('信息管理界面 3.0')
        self.root.geometry("600x400")

        self.info_frame = tk.Frame()  # 相当于一页纸
        self.info_frame.pack()
        #
        # self.about_frame = AboutFrame(self.root)
        # self.about_frame.pack

        # 菜单栏
        menu = tk.Menu(self.info_frame)
        menu.add_command(label='录入', command=self.insert)
        menu.add_command(label='查询', command=self.find)
        menu.add_command(label='删除', command=self.delete)
        menu.add_command(label='修改', command=self.update)
        menu.add_command(label='关于', command=self.about)
        self.root['menu'] = menu
        #
        # tk.Label(self.login_frame).grid(row=0, column=0)  # 用空白label布局挤下框架
        #
        # tk.Label(self.login_frame, text="账号：").grid(row=1, column=1)
        # tk.Entry(self.login_frame, textvariable=self.username_str_var).grid(row=1, column=2)
        # tk.Label(self.login_frame, text="密码：").grid(row=2, column=1)
        # tk.Entry(self.login_frame, textvariable=self.password_str_var).grid(row=2, column=2)
        # tk.Button(self.login_frame, text="登录", command=self.login).grid(row=3, column=1)
        # tk.Button(self.login_frame, text="忘记密码").grid(row=3, column=2)

        # 点击登录按钮，获取用户信息，然后进行校验，成功后跳转

    def insert(self):
        pass

    def find(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass

    def about(self):
        print("about")
        self.info_frame.destroy()  # 把登录的纸撕掉
        AboutFrame(self.root)

class AboutFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root)
        tk.Label(self, height=30).grid(row=0, column=0)
        tk.Label(self, text="版权所属-yangleiw").grid(row=1, column=0)
        tk.Label(self, text="2022/05/22").grid(row=2, column=0)


root = tk.Tk()
# login_page = LoginPage(root)
main_page = MainPage(root)
root.mainloop()
