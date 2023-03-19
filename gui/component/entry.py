import tkinter
from tkinter import ttk, Tk, messagebox


class Application(ttk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.btn = None
        self.entry = None
        self.pack()
        self.login()

    def test(self, event):
        messagebox.showinfo("窗口", self.entry.get())
        print("this is click", event)
        text_content.set('this is master')

    def login(self):
        global text_content
        text_content = tkinter.StringVar()
        text_content.set("this is test")
        self.entry = ttk.Entry(
            self,
            font=("黑体", 30),
            background="cyan",
            foreground="red",
            textvariable=text_content
        )
        self.btn = ttk.Button(
            self,
            text="按钮",
        )
        self.btn.bind("<Button-1>", self.test)
        self.btn.pack()
        self.entry.pack()


if __name__ == '__main__':
    root = Tk()
    root.geometry('200x200')
    app = Application(master=root)
    # 需要加上这两句，否则背景颜色不生效
    style = ttk.Style()
    style.theme_use('classic')
    root.mainloop()
