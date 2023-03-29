import ttkbootstrap as ttk

from gui.student.const import Center
from gui.student.login import PageLogin

if __name__ == '__main__':
    root = ttk.Window(themename="superhero")
    Center.show_center(root)
    PageLogin(root)
    root.mainloop()
