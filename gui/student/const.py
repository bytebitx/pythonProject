import ttkbootstrap as ttk

USER_NAME = 'admin'
USER_PWD = 'admin'

COLLEGE = ["计算机学院", "美术学院", "体育学院"]


class Center:

    @staticmethod
    def show_center(self: ttk.Window):
        w = 600
        h = 500
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        x = (width - w) / 2
        y = (height - h) / 2
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.attributes("-alpha", 1)
        self.resizable(False, False)
        # 需要加上这两句，否则背景颜色不生效
        # style = ttk.Style()
        # style.theme_use('classic')

    @staticmethod
    def show_top_center(self: ttk.Toplevel):
        w = 600
        h = 500
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        x = (width - w) / 2
        y = (height - h) / 2
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.attributes("-alpha", 1)
        self.resizable(False, False)
        # 需要加上这两句，否则背景颜色不生效
        # style = ttk.Style()
        # style.theme_use('classic')
