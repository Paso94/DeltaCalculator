from tkinter import Menu

__author__ = 'Paso'
__date__ = '11/11/2015'


def tools_menu(app_base):
    menu = Menu(app_base.menu, tearoff=0)
    menu.add_command(label="SPU", command=menu_spu)
    app_base.menu.add_cascade(label="Tools", menu=menu)


def menu_spu():
    print("SPU")
