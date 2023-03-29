import tkinter as tk
import ttkbootstrap as ttk

from gui.student.const import Center
from gui.student.main import PageMain


class PageLogin(ttk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master)
        self.root = master
        self.root.title("用户登录")
        self.frm = tk.Frame(self.root)
        self.frm.pack()

        self.accountVar = tk.StringVar()
        self.pwdVar = tk.StringVar()
        self.create_login_page()

    def create_login_page(self):
        ttk.Label(self.frm, text="用 户 登 录", font=('繁体', 30)).pack(anchor='center', pady=30)
        ttk.Label(self.frm, text="账号", font=('简体', 15)).pack(anchor='w', pady=5)
        ttk.Entry(self.frm, textvariable=self.accountVar, width=40).pack(pady=5)
        ttk.Frame(self.frm).pack(pady=30)
        ttk.Label(self.frm, text="密码", font=('简体', 15)).pack(anchor='w')
        ttk.Entry(self.frm, show="*", textvariable=self.pwdVar, width=40).pack(pady=5)
        login_btn = ttk.Button(self.frm, text="登录")
        login_btn.pack(pady=30)
        login_btn.bind("<Button-1>", self.login)
        login_btn.bind("<Return>", self.login)

    def login(self, event):
        self.root.destroy()
        PageMain()


if __name__ == '__main__':
    root = ttk.Window(themename="superhero")
    Center.show_center(root)
    PageLogin(root)
    root.mainloop()
