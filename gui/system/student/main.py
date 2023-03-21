import tkinter as tk
from tkinter import ttk, Tk, messagebox

from gui.system.student import const


class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.createMainPage()

    def createMainPage(self):
        self.title = ttk.Label(text="信息管理系统", font=("宋体", 30))
        self.title.grid(row=0, column=1)

        self.query = ttk.Label(text="查询信息", font=("宋体", 15), background='cyan',
                               wraplength=2, width=5, anchor='center')
        self.query.grid(row=1, column=0, padx=40, rowspan=7, ipady=100, pady=20)
        self.query.bind("<Button-1>", self.queryInfo)

        self.add = ttk.Label(text="添加信息", font=("宋体", 15), background='green', width=30, anchor='center')
        self.add.grid(row=1, column=1, ipady=20, rowspan=2, pady=20)
        self.add.bind("<Button-1>", self.addInfo)

        self.delete = ttk.Label(text="删除信息", font=("宋体", 15), background='green', width=30, anchor='center')
        self.delete.grid(row=3, column=1, ipady=20, rowspan=2)
        self.delete.bind("<Button-1>", self.deleteInfo)

        self.modify = ttk.Label(text="修改信息", font=("宋体", 15), background='green', width=30, anchor='center')
        self.modify.grid(row=5, column=1, ipady=20, rowspan=2, pady=20)
        self.modify.bind("<Button-1>", self.modifyInfo)

        self.quite = tk.Button(text="退出", font=("宋体", 15), background='gray',
                               width=30, anchor='center', command=self.quiteSys)
        self.quite.grid(row=7, column=1, ipady=20, rowspan=2)

        self.show = ttk.Label(text="显示所有信息", font=("宋体", 15), background='cyan',
                              wraplength=2, width=5, anchor='center')
        self.show.grid(row=1, column=2, padx=40, rowspan=7, ipady=80)
        self.show.bind("<Button-1>", self.queryAll)

    def queryInfo(self, event):
        messagebox.showinfo("title", "query info")
        pass

    def addInfo(self, event):
        messagebox.showinfo("title", "add info")
        pass

    def deleteInfo(self, event):
        messagebox.showinfo("title", "delete info")
        pass

    def modifyInfo(self, event):
        messagebox.showinfo("title", "modify info")
        pass

    def quiteSys(self):
        messagebox.showinfo("title", "quiteSys")
        root.destroy()
        pass

    def queryAll(self, event):
        messagebox.showinfo("title", "query all")
        pass


if __name__ == '__main__':
    root = Tk()
    root.title('学生信息管理系统')
    root.geometry('600x500')
    root.resizable(False, False)
    app = Application(master=root)
    # 需要加上这两句，否则背景颜色不生效
    style = ttk.Style()
    style.theme_use('classic')
    root.mainloop()
