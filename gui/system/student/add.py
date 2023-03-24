import tkinter as tk
from tkinter import ttk


class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_add_page()
        self.sexVar = tk.StringVar()
        self.sexVar = "男"

    def create_add_page(self):
        self.title = ttk.Label(self.master, text="添加信息", font=("宋体", 30))
        self.title.pack()

        self.no_frame = tk.Frame(self.master)
        self.no_frame.pack(pady=20)

        self.no = ttk.Label(self.no_frame, text="编号", font=("宋体", 15))
        self.no.pack(side=tk.LEFT)

        self.no_entry = ttk.Entry(self.no_frame, font=("宋体", 15))
        self.no_entry.pack(side=tk.LEFT, padx=15)

        self.name_frame = tk.Frame(self.master)
        self.name_frame.pack()

        self.name = ttk.Label(self.name_frame, text="姓名", font=("宋体", 15))
        self.name.pack(side=tk.LEFT)

        self.name_entry = ttk.Entry(self.name_frame, font=("宋体", 15))
        self.name_entry.pack(side=tk.LEFT, padx=15)

        self.sex_frame = tk.Frame(self.master)
        self.sex_frame.pack()

        self.sex = ttk.Label(self.sex_frame, text="性别", font=("宋体", 15), anchor='center')
        self.sex.pack(side=tk.LEFT)

        self.sex_male_radiobtn = ttk.Radiobutton(self.sex_frame, text="男", value=0)
        self.sex_male_radiobtn.pack(side=tk.LEFT, padx=50)
        self.sex_female_radiobtn = ttk.Radiobutton(self.sex_frame, text="女", value=1)
        self.sex_female_radiobtn.pack(side=tk.LEFT, padx=50)

    @staticmethod
    def create_window():
        window = tk.Tk()
        window.title('添加信息')
        w = 600
        h = 500
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        x = (width - w) / 2
        y = (height - h) / 2
        window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        window.attributes("-alpha", 1)
        window.resizable(False, False)
        Application(master=window)
        # 需要加上这两句，否则背景颜色不生效
        style = ttk.Style()
        style.theme_use('classic')
        window.mainloop()
