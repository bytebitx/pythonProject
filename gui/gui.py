from tkinter import Tk, ttk


class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        # self.master = master
        # self.pack()
        ttk.Label(text="Hello World!").pack()
        # self.lable_1.pack()


if __name__ == '__main__':
    root = Tk()
    root.geometry('300x200')
    app = Application(master=root)
    root.mainloop()


# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()
