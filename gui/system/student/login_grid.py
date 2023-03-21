import tkinter as tk
from tkinter import ttk, Tk, messagebox

from gui.system.student import const


class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.createLoginPage()

    def createLoginPage(self):
        self.lb_1 = ttk.Label(text="用 户 登 录", font=("宋体", 30), anchor='center')
        self.lb_1.grid(row=0, column=1, columnspan=3, sticky='ew')

        self.lb_account = ttk.Label(text="账号", font=("宋体", 15), anchor='center')
        self.lb_account.grid(row=1, column=0, sticky='w', pady=20, padx=20)

        self.entry_input_account = ttk.Entry()
        self.entry_input_account.grid(row=2, column=0, columnspan=2, sticky='w', padx=20)

        self.lb_pwd = ttk.Label(text="密码", font=("宋体", 15))
        self.lb_pwd.grid(row=3, column=0, sticky='w', pady=20, padx=20)

        # self.lb_pwd = ttk.Label(text="密码不能为空", font=("宋体", 10), foreground='red')
        # self.lb_pwd.place_forget()

        self.entry_input_pwd = ttk.Entry(show='*')
        self.entry_input_pwd.grid(row=4, column=0, columnspan=2, sticky='w', padx=20)

        self.btn = tk.Button(text="登 录", font=("仿宋", 20), command=self.login)
        self.btn.grid(row=5, column=1, pady=10)
        self.btn.bind("<Return>", self.login)


    def login(self):
        # self.lb_pwd.place_forget()
        input_account = self.entry_input_account.get()
        input_pwd = self.entry_input_pwd.get()
        if str(input_account) == '':
            messagebox.showerror("输入错误", "请输入账号")
        elif str(input_pwd) == '':
            # self.lb_pwd.place(relx=0.45, rely=0.62)
            messagebox.showerror("输入错误", "请输入密码")
        elif str(input_account) != const.USER_NAME:
            messagebox.showerror("输入错误", "输入的账号错误")
        elif str(input_pwd) != const.USER_PWD:
            messagebox.showerror("输入错误", "输入的密码错误")
        else:
            messagebox.showinfo("窗口", "登录成功")
            root.destroy()
        pass


if __name__ == '__main__':
    root = Tk()
    root.title('学生信息管理系统')
    root.geometry('500x400')
    root.resizable(False, False)
    app = Application(master=root)
    # 需要加上这两句，否则背景颜色不生效
    style = ttk.Style()
    style.theme_use('classic')
    root.mainloop()
