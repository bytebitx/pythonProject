from tkinter import ttk, Tk


class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.login()

    def login(self):
        ttk.Label(text="用 户 登 录", padding=10, font=("黑体", 30)).pack()
        ttk.Label(text="账号", padding=10, font=("常规", 10))


if __name__ == '__main__':
    root = Tk()
    root.geometry('300x200')
    app = Application(master=root)
    root.mainloop()
