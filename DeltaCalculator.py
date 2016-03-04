from tkinter import *

import src.R.strings
from src.window.AppBase import AppBase

__author__ = 'Paso'
__date__ = '29/10/2015'

file = open("src/preferences", 'r')
preferences = eval(file.read())
file.close()
root = Tk()
root['padx'] = 5
root['pady'] = 5
photo = PhotoImage(file='src/delta.gif')
app_base = AppBase(root, photo)
# tk_window.resizable(3000, 2000)
root.geometry("1140x640")
root.title(src.R.strings.title)
root.mainloop()
