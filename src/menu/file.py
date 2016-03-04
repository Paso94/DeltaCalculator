from tkinter.filedialog import *

__author__ = 'Paso'
__date__ = '30/10/2015'


def file_menu(app_base):
    menu = Menu(app_base.menu, tearoff=0)
    menu.add_command(label="Open", command=app_base.open_file)
    menu.add_command(label="Save", command=app_base.save_file)
    menu.add_command(label="Save as...", command=app_base.saveas_file)
    menu.add_separator()
    menu.add_command(label="Exit", command=app_base.window.quit)
    app_base.menu.add_cascade(label="File", menu=menu)


# define options for opening a file
open_file_opt = {}
open_file_opt['defaultextension'] = '.dlt'
open_file_opt['filetypes'] = [('delta printer', '.dlt'), ('all files', '.*')]
open_file_opt['initialdir'] = './'
open_file_opt['initialfile'] = ''
# options['parent'] = root
open_file_opt['title'] = 'Open'

# define options for saving a file
saveas_file_opt = {}
saveas_file_opt['defaultextension'] = '.dlt'
saveas_file_opt['filetypes'] = [('delta printer', '.dlt'), ('all files', '.*')]
saveas_file_opt['initialdir'] = './'
saveas_file_opt['initialfile'] = ''
saveas_file_opt['title'] = 'Save as...'
