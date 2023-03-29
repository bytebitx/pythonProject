import tkinter as tk

from gui.student.add import AddFrame
from gui.student.const import Center
from gui.student.main_frame import MainFrame


class PageMain:
    def __init__(self):
        window = tk.Tk()
        Center.show_center(window)

        self.root = window
        self.root.title("学生信息管理系统")
        self.page_add = AddFrame(self.root)
        self.page_main = MainFrame(self.root)
        self.create_main_page()
        window.mainloop()

    def create_main_page(self):
        self.show_main(None)
        self.page_add.btn_back.bind("<Button-1>", self.add_back)
        self.page_main.label_add.bind("<Button-1>", self.show_add)

    def show_main(self, event):
        self.page_add.pack_forget()
        self.page_main.pack()

    def show_add(self, event):
        self.page_add.pack()
        self.page_main.pack_forget()

    def add_back(self, event):
        print("add_back")
        self.show_main(event)
