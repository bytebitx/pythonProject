import tkinter as tk
from tkinter import ttk, Tk, messagebox

from gui.system.student.add import Application as Add_UI


class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_main_page()

    def create_main_page(self):
        # 这两行非常重要，没有这两行会导致登录页面也会显示在该页面下面且可见
        self.page = ttk.Frame(self.master)
        self.page.grid(ipady=60) # 可以不要ipady=60，写上是为了铺满整个窗口

        self.title = ttk.Label(self.page, text="信息管理系统", font=("宋体", 30))
        self.title.grid(row=0, column=1)

        self.query = ttk.Label(self.page, text="查询信息", font=("宋体", 15), background='cyan',
                               wraplength=2, width=5, anchor='center')
        self.query.grid(row=1, column=0, padx=40, rowspan=7, ipady=100, pady=20)
        self.query.bind("<Button-1>", self.queryInfo)

        self.add = ttk.Label(self.page, text="添加信息", font=("宋体", 15), background='green', width=30, anchor='center')
        self.add.grid(row=1, column=1, ipady=20, rowspan=2, pady=20)
        self.add.bind("<Button-1>", self.addInfo)

        self.delete = ttk.Label(self.page, text="删除信息", font=("宋体", 15), background='green', width=30, anchor='center')
        self.delete.grid(row=3, column=1, ipady=20, rowspan=2)
        self.delete.bind("<Button-1>", self.deleteInfo)

        self.modify = ttk.Label(self.page, text="修改信息", font=("宋体", 15), background='green', width=30, anchor='center')
        self.modify.grid(row=5, column=1, ipady=20, rowspan=2, pady=20)
        self.modify.bind("<Button-1>", self.modifyInfo)

        self.quite = tk.Button(self.page, text="退出", font=("宋体", 15), background='gray',
                               width=30, anchor='center', command=self.quiteSys)
        self.quite.grid(row=7, column=1, ipady=20, rowspan=2)

        self.show = ttk.Label(self.page, text="显示所有信息", font=("宋体", 15), background='cyan',
                              wraplength=2, width=5, anchor='center')
        self.show.grid(row=1, column=2, padx=40, rowspan=7, ipady=80)
        self.show.bind("<Button-1>", self.queryAll)

    def queryInfo(self, event):
        messagebox.showinfo("title", "query info")
        pass

    def addInfo(self, event):
        messagebox.showinfo("title", "add info")
        self.master.destroy()
        Add_UI.create_window()
        pass

    def deleteInfo(self, event):
        messagebox.showinfo("title", "delete info")
        pass

    def modifyInfo(self, event):
        messagebox.showinfo("title", "modify info")
        pass

    def quiteSys(self):
        messagebox.showinfo("title", "quiteSys")
        self.master.destroy()
        pass

    def queryAll(self, event):
        messagebox.showinfo("title", "query all")
        pass