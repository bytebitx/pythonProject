import tkinter as tk
from tkinter import ttk

from gui.student.const import Center


class QueryPage:
    def __init__(self):
        window = tk.Tk()
        Center.show_center(window)

        self.root = window
        self.root.title("查询学生信息")
        self.page_input = InputNoFrame(self.root)
        self.page_detail = DetailFrame(self.root)
        self.create_main_page()
        window.mainloop()

    def create_main_page(self):
        ttk.Label(self.root, text="查询信息", font=('宋体', 30), background='red').pack(pady=30)
        self.page_input.pack()
        self.page_detail.pack_forget()

        btn_frm = ttk.Frame(self.root)
        btn_frm.pack(side=tk.BOTTOM, pady=50)
        ttk.Button(btn_frm, text="返回", command=self.go_back).pack(side=tk.LEFT, padx=50)
        ttk.Button(btn_frm, text="查询", command=self.query_info).pack(side=tk.LEFT, padx=50)

    def query_info(self):
        self.page_input.pack_forget()
        self.page_detail.pack()

    def go_back(self):
        self.root.destroy()


class InputNoFrame(ttk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master)
        # self.entry = None
        self.root = master
        # self.frm = ttk.Frame(self.root)
        # self.frm.pack()
        self.create_input_page()

    def create_input_page(self):
        ttk.Label(self, text="请输入您要查询的学生编号：").pack()
        ttk.Entry(self).pack()
        # self.entry.pack()


class DetailFrame(ttk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master)
        self.root = master
        # self.frm = ttk.Frame(self.root)
        # self.frm.pack()
        self.create_detail_page()

    def create_detail_page(self):
        tk.Text(self, background='white').pack()


if __name__ == '__main__':
    QueryPage()
