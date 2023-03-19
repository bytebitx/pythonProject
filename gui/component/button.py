import tkinter as tk
from tkinter import ttk, messagebox

from tkmacosx import Button


# button的事件和command同时设置，只有事件生效
# command的方法没有event，和事件绑定的方法有event


class Application(ttk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.lb = None
        self.pack()
        self.createWedgit()

    def test(self, event):
        messagebox.showinfo("窗口", "成功")
        print("this is click", event)

    def test_command(self):
        messagebox.showinfo("窗口", "成功button")
        print("this is button")
        btn_text.set('command')

    def test_command2(self, event):
            messagebox.showinfo("窗口", event.widget)
            print("this is button")
            btn_text.set('command')

    def test_command3(self, a, b, c):
            messagebox.showinfo("窗口", a + b + c)
            print("this is button")
            btn_text.set('command')

    def createWedgit(self):
        btn_text.set('改变文字1')
        self.btn = Button(
            self,
            text="改变文字",
            underline=3,
            # 鼠标经过，光标呈现的样式
            cursor='xterm',
            command=self.test_command,
            textvariable=btn_text,
            font=('经典繁方篆', 36, 'normal'),
            background='cyan',
            bg='cyan',
            width=200
        )
        self.btn_2 = Button(
            self,
            text="改变文字2",
            underline=3,
            # 鼠标经过，光标呈现的样式
            cursor='xterm',
            font=('经典繁方篆', 36, 'normal'),
            background='cyan',
            bg='cyan',
            width=200
        )
        self.btn_3 = Button(
            self,
            text="改变文字3",
            underline=3,
            # 鼠标经过，光标呈现的样式
            cursor='xterm',
            command=lambda: self.test_command3('my', 'name', 'is tom'),
            font=('经典繁方篆', 36, 'normal'),
            background='cyan',
            bg='cyan',
            width=200
        )
        self.btn_4 = Button(
            self,
            text="改变文字4",
            underline=3,
            # 鼠标经过，光标呈现的样式
            cursor='xterm',
            command=self.test_command,
            font=('经典繁方篆', 36, 'normal'),
            background='cyan',
            bg='cyan',
            width=200
        )
        # self.lb.bind("<Button>", self.test)
        self.btn.pack()
        self.btn_2.pack(side=tk.RIGHT)
        self.btn_3.pack(side=tk.RIGHT)
        self.btn_4.pack(side=tk.BOTTOM)

        self.btn_2.bind('<Button-2>', self.test_command2)
        self.btn.bind("<Return>", self.test_command)


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x800')
    btn_text = tk.StringVar()
    app = Application(master=root)
    # 需要加上这两句，否则背景颜色不生效
    style = ttk.Style()
    style.theme_use('classic')
    root.mainloop()
