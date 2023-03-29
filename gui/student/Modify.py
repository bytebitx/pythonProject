import tkinter as tk
from tkinter import ttk

from gui.student.const import Center, COLLEGE


class ModifyPage(ttk.Frame):

    def __init__(self, master: tk.Tk):
        super().__init__(master)
        self.root = master
        self.top_level = tk.Toplevel(self.root)
        self.top_level.title("修改学生信息")
        Center.show_top_center(self.top_level)
        self.btn_back = None
        self.modifyFrame = ModifyFrame(self.top_level)
        self.inputFrame = InputFrame(self.top_level)
        self.create_modify_page()

    def create_modify_page(self):
        self.modifyFrame.pack_forget()
        self.inputFrame.pack()

        self.inputFrame.btn_back.bind("<Button-1>", self.go_back)
        self.inputFrame.btn_sure.bind("<Button-1>", self.sure)

    def go_back(self, event):
        print("go_back")
        self.top_level.destroy()

    def sure(self, event):
        self.modifyFrame.pack()
        self.inputFrame.pack_forget()


class InputFrame(ttk.Frame):

    def __init__(self, topLevel: tk.Toplevel):
        super().__init__(topLevel)
        self.btn_sure = None
        self.btn_back = None
        self.topLevel = topLevel
        self.create_modify_page()

    def create_modify_page(self):
        ttk.Label(self, text="修改信息", font=('宋体', 30)).pack(pady=50)
        ttk.Label(self, text="请输入您要修改的学生编号：").pack()
        ttk.Entry(self).pack(pady=10)
        btn_frm = ttk.Frame(self)
        btn_frm.pack(side=tk.BOTTOM, fill=tk.X)
        self.btn_back = ttk.Button(btn_frm, text="返回")
        self.btn_back.pack(side=tk.LEFT)
        self.btn_sure = ttk.Button(btn_frm, text="确定")
        self.btn_sure.pack(side=tk.RIGHT)


class ModifyFrame(ttk.Frame):
    def __init__(self, master: tk.Toplevel):
        super().__init__(master)
        self.root = master
        self.btn_back = None
        self.sex = tk.IntVar()
        self.sex.set(0)
        self.collegeVar = tk.StringVar()
        self.collegeVar.set(COLLEGE[0])
        self.create_modify_page()

    def create_modify_page(self):
        ttk.Label(self, text="修改信息", font=('繁体', 30)).grid(row=0, column=2, pady=15)
        ttk.Label(self, text="编号", font=('宋体', 15)).grid(row=1, column=1)
        ttk.Entry(self, font=('宋体', 15), width=30).grid(row=1, column=2)
        ttk.Label(self, text="姓名", font=('宋体', 15)).grid(row=2, column=1, pady=15, padx=5)
        ttk.Entry(self, font=('宋体', 15), width=30).grid(row=2, column=2)
        ttk.Label(self, text="性别", font=('宋体', 15)).grid(row=3, column=1)
        sex_frm = ttk.Frame(self)
        sex_frm.grid(row=3, column=2, sticky=tk.W)
        ttk.Radiobutton(sex_frm, text="男", value=0, variable=self.sex).pack(side=tk.LEFT)
        ttk.Radiobutton(sex_frm, text="女", value=1, variable=self.sex).pack(side=tk.RIGHT, padx=30)
        ttk.Label(self, text="年龄", font=('宋体', 15)).grid(row=4, column=1, pady=15, padx=5)
        ttk.Entry(self, font=('宋体', 15), width=30).grid(row=4, column=2)
        ttk.Label(self, text="学院", font=('宋体', 15)).grid(row=5, column=1)
        # ttk.Style().configure('TCombobox', foreground='red', font=('黑体', 30), background="blue", width=30)
        college_cbox = ttk.Combobox(self, values=COLLEGE, textvariable=self.collegeVar)
        college_cbox.current(0)
        college_cbox.bind('<<ComboboxSelected>>', self.selectCollege)
        college_cbox.grid(row=5, column=2)

        ttk.Label(self, text="专业", font=('宋体', 15)).grid(row=6, column=1, pady=15, padx=5)
        ttk.Entry(self, font=('宋体', 15), width=30).grid(row=6, column=2)

        ttk.Button(self, text="确定修改", command=self.saveInfo).grid(row=7, column=2)

    def selectCollege(self, event):
        print(self.collegeVar.get())

    def saveInfo(self):
        print("save info")
        self.root.destroy()

