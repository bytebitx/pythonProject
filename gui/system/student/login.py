import tkinter as tk
from tkinter import ttk, Tk, messagebox

from gui.system.student import const
from gui.system.student.main import Application as MainUI


class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_login_page()

    def create_login_page(self):
        self.lb_1 = ttk.Label(self.master, text="用 户 登 录", font=("宋体", 30))
        self.lb_1.place(relx=0.35, rely=0.05)

        self.lb_account = ttk.Label(self.master, text="账号", font=("宋体", 15))
        self.lb_account.place(relx=0.05, rely=0.3)

        self.entry_input_account = ttk.Entry(self.master)
        self.entry_input_account.focus()
        self.entry_input_account.place(relx=0.05, rely=0.4)

        self.lb_pwd = ttk.Label(self.master, text="密码", font=("宋体", 15))
        self.lb_pwd.place(relx=0.05, rely=0.5)

        self.lb_pwd = ttk.Label(self.master, text="密码不能为空", font=("宋体", 10), foreground='red')
        self.lb_pwd.place_forget()

        self.entry_input_pwd = ttk.Entry(self.master, show='*')
        self.entry_input_pwd.place(relx=0.05, rely=0.6)

        self.btn = tk.Button(self.master, text="登 录", font=("仿宋", 20), command=self.login)
        self.btn.place(relx=0.35, rely=0.75, relwidth=0.3)
        self.btn.bind("<Return>", self.login)

    def login(self):
        self.lb_pwd.place_forget()
        input_account = self.entry_input_account.get()
        input_pwd = self.entry_input_pwd.get()
        if str(input_account) == '':
            messagebox.showerror("输入错误", "请输入账号")
        elif str(input_pwd) == '':
            self.lb_pwd.place(relx=0.45, rely=0.62)
            messagebox.showerror("输入错误", "请输入密码")
        elif str(input_account) != const.USER_NAME:
            messagebox.showerror("输入错误", "输入的账号错误")
        elif str(input_pwd) != const.USER_PWD:
            messagebox.showerror("输入错误", "输入的密码错误")
        else:
            messagebox.showinfo("窗口", "登录成功")
            self.destroy()
            MainUI(self.master)

        pass
