import tkinter
from tkinter import ttk, Tk, messagebox


class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.lb = None
        self.pack()
        self.login()

    def test(self, event):
        messagebox.showinfo("窗口", "成功")
        print("this is click", event)

    def login(self):
        self.lb = ttk.Label(
            self,
            text="用 户 登 录用 户 登 录用 户 登 录用 户 登 录用 户 登 录用 户 登 录用 户 登 录用 户 登 录",
            padding=(0, 30, 0, 0),
            font=("黑体", 30),
            background="cyan",
            foreground="red",
            underline=3,
            # 文本内容位置
            anchor='se',
            # 文本到多少宽度后换行，单位是像素
            wraplength=100,
            # text内容多的时候的对齐方式
            justify='right',
        )
        self.lb.bind("<Button>", self.test)
        self.lb.pack(side=tkinter.RIGHT)


if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    app = Application(master=root)
    # 需要加上这两句，否则背景颜色不生效
    style = ttk.Style()
    style.theme_use('classic')
    root.mainloop()
