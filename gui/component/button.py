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
        self.login()

    def test(self, event):
        messagebox.showinfo("窗口", "成功")
        print("this is click", event)

    def test_command(self):
        messagebox.showinfo("窗口", "成功button")
        print("this is button")
        btn_text.set('command')

    def login(self):
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
        # self.lb.bind("<Button>", self.test)
        self.btn.pack(side=tk.RIGHT)



if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x800')
    btn_text = tk.StringVar()
    app = Application(master=root)
    # 需要加上这两句，否则背景颜色不生效
    style = ttk.Style()
    style.theme_use('classic')
    root.mainloop()
