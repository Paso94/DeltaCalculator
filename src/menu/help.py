from tkinter import *

__author__ = 'Paso'
__date__ = '30/10/2015'


def help_menu(app_base):
    menu = Menu(app_base.menu, tearoff=0)
    menu.add_command(label="Info", command=app_base.info_dialog)
    menu.add_separator()
    # menu.add_command(label="Check for Update...", command=menu_update)
    menu.add_command(label="About", command=app_base.about_dialog)
    app_base.menu.add_cascade(label="Help", menu=menu)





