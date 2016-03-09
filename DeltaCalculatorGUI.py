from tkinter.filedialog import *
from tkinter.messagebox import askokcancel

import DeltaCalculatorGUI.lang.en as strings
import DeltaCalculatorGUI.colors as colors
import DeltaCalculatorGUI.dimensions as dimensions
from DeltaCalculatorGUI.entryFloat import EntryFloat
from delta import delta
from delta import dfile

__author__ = 'Paso'
__date__ = '09/03/2016'

filename = None
###########################################################################################
# Preferences
###########################################################################################
__file__ = open("DeltaCalculatorGUI/preferences", 'r')
__preferences__ = eval(__file__.read())
__file__.close()

# Import language
if __preferences__['language'] == "IT":
    import DeltaCalculatorGUI.lang.it as strings

###########################################################################################
# GUI
###########################################################################################
root = Tk()
root.geometry("1140x640")
root.title(strings.title)
root['padx'] = 5
root['pady'] = 5
root['background'] = colors.bg


def get(var):
    try:
        return var.get()
    except ValueError:
        return 0


def update(a, b, c):
    delta.printer = delta.Delta(get(pgr_var), get(pgh_var), eo=get(eo_var), co=get(co_var),
                                so=get(so_var), no=get(no_var), bo=get(bo_var),
                                dr=get(dr_var), sro=get(sro_var), ph=get(ph_var))

    if get(dr_var) < delta.printer.dr_min:
        dr_entry['bg'] = colors.invalid
    else:
        dr_entry['bg'] = colors.bg

    if get(sro_var) < delta.printer.sro_min or get(sro_var) > delta.printer.sro_max:
        sro_entry['bg'] = colors.invalid
    else:
        sro_entry['bg'] = colors.bg

    if get(ph_var) < delta.printer.ph_min:
        ph_entry['bg'] = colors.invalid
    else:
        ph_entry['bg'] = colors.bg

    dr_info['text'] = str(delta.printer.dr_min) + " < dr"
    sro_info['text'] = str(delta.printer.sro_min) + " < sro < " + str(delta.printer.sro_max)
    ph_info['text'] = str(delta.printer.ph_min) + " < ph"
    drd_var.set(str(delta.printer.drd))
    srod_var.set(str(delta.printer.srod))
    mina_var.set(str(delta.printer.mina))
    ha_var.set(str(delta.printer.ha))
    maxa_var.set(str(delta.printer.maxa))
    phd_var.set(str(delta.printer.phd))
    zh_var.set(str(delta.printer.zh))

    if filename:
        root.title('* ' + filename + " - " + strings.title)
    else:
        root.title('* ' + strings.title)


###########################################################################################
# Menu
###########################################################################################
menu = Menu(root)


#############################################
# Menu File
#############################################
def open_file():
    # define options for opening a file
    open_file_opt = {}
    open_file_opt['defaultextension'] = '.dlt'
    open_file_opt['filetypes'] = [('delta printer', '.dlt'), ('all files', '.*')]
    open_file_opt['initialdir'] = './'
    open_file_opt['initialfile'] = ''
    open_file_opt['title'] = 'Open'
    filename = askopenfilename(**open_file_opt)
    if filename:
        try:
            dlt = dfile.fopen(filename)
            pgr_var.set(dlt['pgr'])
            pgh_var.set(dlt['pgh'])
            delta.printer.minad = dlt['minad']
            delta.printer.maxad = dlt['maxad']
            eo_var.set(dlt['eo'])
            co_var.set(dlt['co'])
            so_var.set(dlt['so'])
            no_var.set(dlt['no'])
            bo_var.set(dlt['bo'])
            dr_var.set(dlt['dr'])
            sro_var.set(dlt['sro'])
            ph_var.set(dlt['ph'])
        except AttributeError:
            print(strings.cancel_file)
        except:
            print(strings.not_valid_file)

    root.title(filename + " - " + strings.title)


def save_file():
    if filename:
        dfile.fsave(filename)
        root.title(filename + " - " + strings.title)
    else:
        saveas_file()


def saveas_file():
    # define options for saving a file
    saveas_file_opt = {}
    saveas_file_opt['defaultextension'] = '.dlt'
    saveas_file_opt['filetypes'] = [('delta printer', '.dlt'), ('all files', '.*')]
    saveas_file_opt['initialdir'] = './'
    saveas_file_opt['initialfile'] = ''
    saveas_file_opt['title'] = 'Save as...'
    filename = asksaveasfilename(**saveas_file_opt)
    if filename:
        dfile.fsave(filename)
        root.title(filename + " - " + strings.title)


menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="Open", command=open_file)
menu_file.add_command(label="Save", command=save_file)
menu_file.add_command(label="Save as...", command=saveas_file)
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)


#############################################
# Menu Preferences
#############################################
def set_language(lng):
    __preferences__['language'] = lng
    file = open("DeltaCalculatorGUI/preferences", 'w')
    file.write(str(__preferences__))
    file.close()


def saveasdefault_dialog():
    if askokcancel("Save as default", strings.default_menu):
        dfile.fsave('src/delta/delta.default')
        root.title(strings.title)


menu_preferences = Menu(menu, tearoff=0)
language_menu = Menu(menu_preferences)
language_menu.add_radiobutton(label='English', command=lambda: set_language('EN'))
language_menu.add_radiobutton(label='Italiano', command=lambda: set_language('IT'))
menu_preferences.add_cascade(label=strings.language_menu, menu=language_menu)
menu_preferences.add_separator()
menu_preferences.add_command(label="Save as default", command=saveasdefault_dialog)
menu.add_cascade(label=strings.preferences_menu, menu=menu_preferences)


#############################################
# Menu Help
#############################################


def info_dialog():
    top = Toplevel(root)
    top.geometry("230x442")
    dr_photo = PhotoImage(file='DeltaCalculatorGUI/res/dr.gif')
    Label(top, image=dr_photo).pack()
    sro_photo = PhotoImage(file='DeltaCalculatorGUI/res/sro.gif')
    Label(top, image=sro_photo).pack()
    ha_photo = PhotoImage(file='DeltaCalculatorGUI/res/ha.gif')
    Label(top, image=ha_photo).pack()
    ph_photo = PhotoImage(file='DeltaCalculatorGUI/res/ph.gif')
    Label(top, image=ph_photo).pack()
    zh_photo = PhotoImage(file='DeltaCalculatorGUI/res/zh.gif')
    Label(top, image=zh_photo).pack()
    root.wait_window(top)


def about_dialog():
    top = Toplevel(root)
    top.geometry("300x100")
    text = strings.title + " - v0.2\nAuthor: Paso\nhttps://github.com/Paso94/DeltaCalculator"
    Label(top, text=text).pack()
    root.wait_window(top)


menu_help = Menu(menu, tearoff=0)
menu_help.add_command(label="Info", command=info_dialog)
menu_help.add_separator()
# menu.add_command(label="Check for Update...", command=menu_update)
menu_help.add_command(label="About", command=about_dialog)
menu.add_cascade(label="Help", menu=menu_help)
#############################################
root.config(menu=menu)


###########################################################################################
# Input
###########################################################################################
def input_row(frame, row, name, symbol, value):
    Label(frame, text=name, bg=colors.bg).grid(row=row, **dimensions.input_names_grid)
    Label(frame, text=symbol, bg=colors.bg).grid(row=row, **dimensions.input_symbols_grid)
    var = DoubleVar()
    var.set(value)
    EntryFloat(frame, textvariable=var, width=dimensions.width_entries, bg=colors.bg, justify=CENTER) \
        .grid(row=row, **dimensions.input_entries_grid)
    var.trace('w', update)
    return var


# Frame
input_frame = LabelFrame(root, text=strings.input, padx=5, pady=5, bg=colors.bg)
input_frame.grid(**dimensions.input_grid)
# Grid
# Volume
Label(input_frame, text=strings.pv_title, bg=colors.bg).grid(row=0, **dimensions.input_title_grid)

pgr_var = input_row(input_frame, 1, strings.pgr_name, strings.pgr_symbol, delta.printer.pgr)
pgh_var = input_row(input_frame, 2, strings.pgh_name, strings.pgh_symbol, delta.printer.pgh)
# Horizontal Offsets
Label(input_frame, text=strings.ho_title, bg=colors.bg).grid(row=3, **dimensions.input_title_grid)
eo_var = input_row(input_frame, 4, strings.eo_name, strings.eo_symbol, delta.printer.eo)
co_var = input_row(input_frame, 5, strings.co_name, strings.co_symbol, delta.printer.co)
# Vertical Offsets
Label(input_frame, text=strings.vo_title, bg=colors.bg).grid(row=6, **dimensions.input_title_grid)
so_var = input_row(input_frame, 7, strings.so_name, strings.so_symbol, delta.printer.so)
no_var = input_row(input_frame, 8, strings.no_name, strings.no_symbol, delta.printer.no)
bo_var = input_row(input_frame, 9, strings.bo_name, strings.bo_symbol, delta.printer.bo)


###########################################################################################
# Output
###########################################################################################
def output_row(frame, row, name, symbol, string):
    Label(frame, text=name, bg=colors.bg).grid(row=row, **dimensions.output_names_grid)
    Label(frame, text=symbol, bg=colors.bg).grid(row=row, **dimensions.output_symbols_grid)
    var = StringVar()
    var.set(string)
    Label(frame, textvariable=var, width=dimensions.width_entries, bg=colors.bg) \
        .grid(row=row, **dimensions.output_labels_grid)
    return var


def output_entry_row(frame, row, value, string):
    var = DoubleVar()
    var.set(value)
    entry = EntryFloat(frame, textvariable=var, width=dimensions.width_entries, bg=colors.bg, justify=CENTER)
    entry.grid(row=row, **dimensions.output_entries_grid)
    var.trace('w', update)
    info = Label(frame, text=string, width=dimensions.width_entries * 2 + 2, bg=colors.bg)
    info.grid(row=row, **dimensions.output_info_grid)
    return var, entry, info  # Frame


output_frame = LabelFrame(root, text=strings.output, padx=5, pady=5, bg=colors.bg)
output_frame.grid(**dimensions.output_grid)

# Grid Values
# Geometry
Label(output_frame, text=strings.g_title, bg=colors.bg).grid(row=0, **dimensions.input_title_grid)
drd_var = output_row(output_frame, 1, strings.dr_name, strings.dr_symbol, delta.printer.drd)
dr_var, dr_entry, dr_info = output_entry_row(output_frame, 1, delta.printer.dr, str(delta.printer.dr_min) + " < dr")
srod_var = output_row(output_frame, 2, strings.sro_name, strings.sro_symbol, delta.printer.srod)
sro_var, sro_entry, sro_info = output_entry_row(output_frame, 2, delta.printer.sro, str(delta.printer.sro_min) +
                                                " < sro < " + str(delta.printer.sro_max))
# Angles
Label(output_frame, text=strings.a_title, bg=colors.bg).grid(row=3, **dimensions.input_title_grid)
mina_var = output_row(output_frame, 4, strings.mina_name, strings.mina_symbol, delta.printer.mina)
ha_var = output_row(output_frame, 5, strings.ha_name, strings.ha_symbol, delta.printer.ha)
maxa_var = output_row(output_frame, 6, strings.maxa_name, strings.maxa_symbol, delta.printer.maxa)
aja_var = output_row(output_frame, 7, strings.aja_name, strings.aja_symbol, delta.printer.aja)
# Heights
Label(output_frame, text=strings.h_title, bg=colors.bg).grid(row=8, **dimensions.input_title_grid)
phd_var = output_row(output_frame, 9, strings.ph_name, strings.ph_symbol, delta.printer.phd)
ph_var, ph_entry, ph_info = output_entry_row(output_frame, 8, delta.printer.ph, str(delta.printer.ph_min) + " < ph")
zh_var = output_row(output_frame, 10, strings.zh_name, strings.zh_symbol, delta.printer.zh)

###########################################################################################
# Image
###########################################################################################
photo = PhotoImage(file='DeltaCalculatorGUI/res/delta.gif')
# Frame
Label(root, image=photo, bg=colors.bg).grid(**dimensions.image_grid)

###########################################################################################

# tk_window.resizable(3000, 2000)
root.mainloop()
