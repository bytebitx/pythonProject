import tkinter as tk
from tkinter import ttk

from gui.student.const import Center


class DelFrame(ttk.Frame):

    def __init__(self, master: tk.Tk):
        super().__init__(master)
        self.root = master
        self.top_level = tk.Toplevel(self.root)
        self.top_level.title("删除学生信息")
        Center.show_center(self.top_level)
        self.btn_back = None
        self.create_del_page()

    def create_del_page(self):
        ttk.Label(self.top_level, text="删除信息", font=('宋体', 30)).pack(pady=30)
        ttk.Label(self.top_level, text="请输入您要删除的学生编号：").pack()
        ttk.Entry(self.top_level).pack()
        btn_frm = ttk.Frame(self.top_level)
        btn_frm.pack(side=tk.BOTTOM, pady=50)
        ttk.Button(btn_frm, text="返回", command=self.go_back).pack(side=tk.LEFT, padx=50)
        ttk.Button(btn_frm, text="删除", command=self.sure).pack(side=tk.LEFT, padx=50)

    def go_back(self):
        self.top_level.destroy()

    def sure(self):
        self.top_level.destroy()
