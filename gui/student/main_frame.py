from tkinter import ttk
import tkinter as tk

from gui.student.Modify import ModifyPage
from gui.student.const import Center
from gui.student.query import QueryPage
from gui.student.del_frame import DelFrame


class MainFrame(ttk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master)
        self.root = master
        self.root.title("信息管理系统")
        self.label_add = None
        self.label_query = None
        self.create_main_page()

    def create_main_page(self):
        ttk.Label(self, text="信息管理系统", font=('繁体', 30)).grid(row=0, column=1, pady=20)
        self.label_add = ttk.Label(self, text="添加信息", font=('简体', 15), width=30, anchor='center',
                                   background='green')
        self.label_add.grid(row=1, column=1, pady=10, ipady=25)

        label_del = ttk.Label(self, text="删除信息", font=('简体', 15), width=30, anchor='center', background='green')
        label_del.grid(row=2, column=1, pady=10, ipady=25)

        label_modify = ttk.Label(self, text="修改信息", font=('简体', 15), width=30, anchor='center',
                                 background='green')
        label_modify.grid(row=3, column=1, pady=10, ipady=25)

        ttk.Label(self, text="退出", font=('简体', 15), width=30, anchor='center', background='gray') \
            .grid(row=4, column=1, pady=10, ipady=25)
        self.label_query = ttk.Label(self, text="查询信息", font=('简体', 15), width=6, anchor='center',
                                     background='cyan',
                                     wraplength=40)
        self.label_query.grid(row=1, column=0, rowspan=4, ipady=130, padx=44)
        ttk.Label(self, text="显示所有信息", font=('简体', 15), width=6, anchor='center', background='cyan',
                  wraplength=40) \
            .grid(row=1, column=2, rowspan=4, ipady=130, padx=44)

        self.label_query.bind("<Button-1>", self.show_query_page)
        label_del.bind("<Button-1>", self.show_del_page)
        label_modify.bind("<Button-1>", self.show_modify_page)

    def show_query_page(self, event):
        QueryPage()

    def show_del_page(self, event):
        DelFrame(self.root)

    def show_modify_page(self, event):
        ModifyPage(self.root)


if __name__ == '__main__':
    window = tk.Tk()
    Center.show_center(window)
    MainFrame(window)
    window.mainloop()
