from tkinter import ttk
import tkinter as tk

from gui.student.const import COLLEGE


class AddFrame(ttk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master)
        self.root = master
        self.root.title("添加学生信息")
        # 这儿创建frame是在AddFrame这个Frame上面再加一个frame
        # 如果创建控件使用self.frm，那么再使用AddFrame这个frame的对象的pack_forget()方法时
        # 就只隐藏了AddFrame这个frame，而没有隐藏self.frm这个frame；这个时候节目任然会显示创建的控件
        # self.frm = ttk.Frame(master)
        # self.frm.pack()

        self.btn_back = None
        self.sex = tk.IntVar()
        self.sex.set(0)
        self.collegeVar = tk.StringVar()
        self.collegeVar.set(COLLEGE[0])
        self.create_add_page()

    def create_add_page(self):
        ttk.Label(self, text="添加信息", font=('繁体', 30)).grid(row=0, column=1, columnspan=3, pady=15)
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

        btn_frm = ttk.Frame(self)
        btn_frm.grid(row=7, column=2, columnspan=3)
        self.btn_back = ttk.Button(btn_frm, text="返回")
        self.btn_back.pack(side=tk.LEFT, anchor=tk.W)
        self.btn_save = ttk.Button(btn_frm, text="保存")
        self.btn_save.pack(side=tk.RIGHT, anchor=tk.E, padx=50)

    def selectCollege(self, event):
        print(self.collegeVar.get())
