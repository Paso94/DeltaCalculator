from tkinter import *
from tkinter.simpledialog import Dialog


import src.R.strings

__author__ = 'Paso'
__date__ = '11/11/2015'


def preferences_menu(app_base):
    menu = Menu(app_base.menu, tearoff=0)
    language_menu = Menu(menu)
    language_menu.add_radiobutton(label='English', command=lambda: set_language('EN'), indicatoron='false')
    language_menu.add_radiobutton(label='Italiano', command=lambda: set_language('IT'))
    menu.add_cascade(label=src.R.strings.language_menu, menu=language_menu)
    menu.add_separator()
    menu.add_command(label="Save as default", command=lambda: saveasdefault_dialog(app_base))
    app_base.menu.add_cascade(label=src.R.strings.preferences_menu, menu=menu)


def set_language(lng):
    file = open("src/preferences", 'r')
    preferences = eval(file.read())
    file.close()
    preferences['language'] = lng
    file = open("src/preferences", 'w')
    file.write(str(preferences))
    file.close()


def saveasdefault_dialog(app_base):
    '''
    top = Toplevel(app_base)
    top.geometry("200x100")
    app_base.wait_window(top)
    # app_base.saveasdefault_file()
    '''
    DefaultDialog(app_base)


class DefaultDialog(Dialog):

    def body(self, master):

        text = src.R.strings.default
        Label(master, text=text).pack()


    def apply(self):
        print("Save as default")
