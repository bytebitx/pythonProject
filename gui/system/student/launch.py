from tkinter import Tk, ttk

from gui.system.student.login import Application

if __name__ == '__main__':
    window = Tk()
    window.title('学生信息管理系统')
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
