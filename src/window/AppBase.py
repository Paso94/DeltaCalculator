from src.menu.file import *
from src.menu.tools import *
from src.menu.preferences import *
from src.menu.help import *

import src.R.colors
import src.R.strings
import src.R.dimensions
from src import delta
from src.window.entryFloat import EntryFloat

__author__ = 'Paso'
__date__ = '11/11/2015'


class AppBase:
    def __init__(self, root, photo):
        self.window = root
        self.window["background"] = src.R.colors.bg

        self.filename = None
        ###########################################################################################
        # Menu
        ###########################################################################################
        self.menu = Menu(self.window)
        file_menu(self)
        preferences_menu(self)
        # view_menu(self)
        help_menu(self)
        # display the menu
        self.window.config(menu=self.menu)

        ###########################################################################################
        # Input
        ###########################################################################################
        # Frame
        input_frame = LabelFrame(self.window, text=src.R.strings.input, padx=5, pady=5, bg=src.R.colors.bg)
        input_frame.grid(**src.R.dimensions.input_grid)
        # Grid
        # Volume
        Label(input_frame, text=src.R.strings.pv_title, bg=src.R.colors.bg).grid(row=0, **src.R.dimensions.input_title_grid)
        self.pgr_var = self.input_row(input_frame, 1, src.R.strings.pgr_name, src.R.strings.pgr_symbol, delta.printer.pgr)
        self.pgh_var = self.input_row(input_frame, 2, src.R.strings.pgh_name, src.R.strings.pgh_symbol, delta.printer.pgh)
        # Horizontal Offsets
        Label(input_frame, text=src.R.strings.ho_title, bg=src.R.colors.bg).grid(row=3, **src.R.dimensions.input_title_grid)
        self.eo_var = self.input_row(input_frame, 4, src.R.strings.eo_name, src.R.strings.eo_symbol, delta.printer.eo)
        self.co_var = self.input_row(input_frame, 5, src.R.strings.co_name, src.R.strings.co_symbol, delta.printer.co)
        # Vertical Offsets
        Label(input_frame, text=src.R.strings.vo_title, bg=src.R.colors.bg).grid(row=6, **src.R.dimensions.input_title_grid)
        self.so_var = self.input_row(input_frame, 7, src.R.strings.so_name, src.R.strings.so_symbol, delta.printer.so)
        self.no_var = self.input_row(input_frame, 8, src.R.strings.no_name, src.R.strings.no_symbol, delta.printer.no)
        self.bo_var = self.input_row(input_frame, 9, src.R.strings.bo_name, src.R.strings.bo_symbol, delta.printer.bo)

        ###########################################################################################
        # Image
        ###########################################################################################
        # Frame
        '''
        image_frame = LabelFrame(self.window, text="Image", padx=5, pady=5, bg=R.colors.bg)
        image_frame.grid(ipadx=5, ipady=5, **R.dimensions.image_grid)
        photo = PhotoImage(file='delta.gif')
        Label(image_frame, image=photo).pack(fill="both")
        '''
        Label(self.window, image=photo, bg=src.R.colors.bg).grid(**src.R.dimensions.image_grid)
        ###########################################################################################
        # Output
        ###########################################################################################
        # Frame
        output_frame = LabelFrame(self.window, text=src.R.strings.output, padx=5, pady=5, bg=src.R.colors.bg)
        output_frame.grid(**src.R.dimensions.output_grid)

        # Grid Values
        # Geometry
        Label(output_frame, text=src.R.strings.g_title, bg=src.R.colors.bg).grid(row=0, **src.R.dimensions.input_title_grid)
        self.drd_var = self.output_row(output_frame, 1, src.R.strings.dr_name, src.R.strings.dr_symbol, delta.printer.drd)
        self.dr_var, self.dr_entry, self.dr_info = self.output_entry_row(output_frame, 1, delta.printer.dr,
                                                                         str(delta.printer.dr_min) + " < dr")
        self.srod_var = self.output_row(output_frame, 2, src.R.strings.sro_name, src.R.strings.sro_symbol, delta.printer.srod)
        self.sro_var, self.sro_entry, self.sro_info = self.output_entry_row(output_frame, 2, delta.printer.sro,
                                                                            str(delta.printer.sro_min) + " < sro < " +
                                                                            str(delta.printer.sro_max))
        # Angles
        Label(output_frame, text=src.R.strings.a_title, bg=src.R.colors.bg).grid(row=3, **src.R.dimensions.input_title_grid)
        self.mina_var = self.output_row(output_frame, 4, src.R.strings.mina_name, src.R.strings.mina_symbol, delta.printer.mina)
        self.ha_var = self.output_row(output_frame, 5, src.R.strings.ha_name, src.R.strings.ha_symbol, delta.printer.ha)
        self.maxa_var = self.output_row(output_frame, 6, src.R.strings.maxa_name, src.R.strings.maxa_symbol, delta.printer.maxa)
        # Heights
        Label(output_frame, text=src.R.strings.h_title, bg=src.R.colors.bg).grid(row=7, **src.R.dimensions.input_title_grid)
        self.phd_var = self.output_row(output_frame, 8, src.R.strings.ph_name, src.R.strings.ph_symbol, delta.printer.phd)
        self.ph_var, self.ph_entry, self.ph_info = self.output_entry_row(output_frame, 8, delta.printer.ph,
                                                                         str(delta.printer.ph_min) + " < ph")
        self.zh_var = self.output_row(output_frame, 9, src.R.strings.zh_name, src.R.strings.zh_symbol, delta.printer.zh)

    def update(self, a, b, c):
        delta.printer = delta.Delta(get(self.pgr_var), get(self.pgh_var), eo=get(self.eo_var), co=get(self.co_var),
                                    so=get(self.so_var), no=get(self.no_var), bo=get(self.bo_var),
                                    dr=get(self.dr_var), sro=get(self.sro_var), ph=get(self.ph_var))

        if get(self.dr_var) < delta.printer.dr_min:
            self.dr_entry['bg'] = src.R.colors.invalid
        else:
            self.dr_entry['bg'] = src.R.colors.bg

        if get(self.sro_var) < delta.printer.sro_min or get(self.sro_var) > delta.printer.sro_max:
            self.sro_entry['bg'] = src.R.colors.invalid
        else:
            self.sro_entry['bg'] = src.R.colors.bg

        if get(self.ph_var) < delta.printer.ph_min:
            self.ph_entry['bg'] = src.R.colors.invalid
        else:
            self.ph_entry['bg'] = src.R.colors.bg

        self.dr_info['text'] = str(delta.printer.dr_min) + " < dr"
        self.sro_info['text'] = str(delta.printer.sro_min) + " < sro < " + str(delta.printer.sro_max)
        self.ph_info['text'] = str(delta.printer.ph_min) + " < ph"
        # print(delta.printer.output_values)
        self.drd_var.set(str(delta.printer.drd))
        self.srod_var.set(str(delta.printer.srod))
        self.mina_var.set(str(delta.printer.mina))
        self.ha_var.set(str(delta.printer.ha))
        self.maxa_var.set(str(delta.printer.maxa))
        self.phd_var.set(str(delta.printer.phd))
        self.zh_var.set(str(delta.printer.zh))

        if self.filename:
            self.window.title('* ' + self.filename + " - " + src.R.strings.title)
        else:
            self.window.title('* ' + src.R.strings.title)

    def input_row(self, frame, row, name, symbol, value):
        Label(frame, text=name, bg=src.R.colors.bg).grid(row=row, **src.R.dimensions.input_names_grid)
        Label(frame, text=symbol, bg=src.R.colors.bg).grid(row=row, **src.R.dimensions.input_symbols_grid)
        var = DoubleVar()
        var.set(value)
        EntryFloat(frame, textvariable=var, width=src.R.dimensions.width_entries,
                   bg=src.R.colors.bg, justify=CENTER).grid(row=row, **src.R.dimensions.input_entries_grid)
        var.trace('w', self.update)
        return var

    @staticmethod
    def output_row(frame, row, name, symbol, string):
        Label(frame, text=name, bg=src.R.colors.bg).grid(row=row, **src.R.dimensions.output_names_grid)
        Label(frame, text=symbol, bg=src.R.colors.bg).grid(row=row, **src.R.dimensions.output_symbols_grid)
        var = StringVar()
        var.set(string)
        Label(frame, textvariable=var, width=src.R.dimensions.width_entries,
              bg=src.R.colors.bg).grid(row=row, **src.R.dimensions.output_labels_grid)
        return var

    def output_entry_row(self, frame, row, value, string):
        var = DoubleVar()
        var.set(value)
        entry = EntryFloat(frame, textvariable=var, width=src.R.dimensions.width_entries, bg=src.R.colors.bg, justify=CENTER)
        entry.grid(row=row, **src.R.dimensions.output_entries_grid)
        var.trace('w', self.update)
        info = Label(frame, text=string, width=src.R.dimensions.width_entries * 2 + 2, bg=src.R.colors.bg)
        info.grid(row=row, **src.R.dimensions.output_info_grid)
        return var, entry, info

    def open_file(self):
        self.filename = askopenfilename(**open_file_opt)
        if self.filename:
            try:
                file = open(self.filename, 'r')
                dlt = eval(file.read())
                file.close()
                self.pgr_var.set(dlt['pgr'])
                self.pgh_var.set(dlt['pgh'])
                delta.printer.minad = dlt['minad']
                delta.printer.maxad = dlt['maxad']
                self.eo_var.set(dlt['eo'])
                self.co_var.set(dlt['co'])
                self.so_var.set(dlt['so'])
                self.no_var.set(dlt['no'])
                self.bo_var.set(dlt['bo'])
                self.dr_var.set(dlt['dr'])
                self.sro_var.set(dlt['sro'])
                self.ph_var.set(dlt['ph'])
            except AttributeError:
                print("Apertura annullata")
            except:
                print("File non valido")

        self.window.title(self.filename + " - " + src.R.strings.title)

    def save_file(self, ):
        if self.filename:
            file = open(self.filename, 'w')
            file.write(str(delta.printer))
            file.close()
            self.window.title(self.filename + " - " + src.R.strings.title)
        else:
            self.saveas_file()

    def saveas_file(self):
        self.filename = asksaveasfilename(**saveas_file_opt)
        if self.filename:
            file = open(self.filename, 'w')
            file.write(str(delta.printer))
            file.close()
            self.window.title(self.filename + " - " + src.R.strings.title)

    def saveasdefault_file(self):
            file = open("delta.default", 'w')
            file.write(str(delta.printer))
            file.close()
            self.window.title(self.filename + " - " + src.R.strings.title)

    def info_dialog(self):
        top = Toplevel(self.window)
        top.geometry("230x442")
        dr_photo = PhotoImage(file='src/menu/dr.gif')
        Label(top, image=dr_photo).pack()
        sro_photo = PhotoImage(file='src/menu/sro.gif')
        Label(top, image=sro_photo).pack()
        ha_photo = PhotoImage(file='src/menu/ha.gif')
        Label(top, image=ha_photo).pack()
        ph_photo = PhotoImage(file='src/menu/ph.gif')
        Label(top, image=ph_photo).pack()
        zh_photo = PhotoImage(file='src/menu/zh.gif')
        Label(top, image=zh_photo).pack()
        self.window.wait_window(top)

    def about_dialog(self):
        top = Toplevel(self.window)
        top.geometry("200x100")
        text = src.R.strings.title + " - v0.1\nAuthor: Paso"
        Label(top, text=text).pack()
        self.window.wait_window(top)


def get(var):
    try:
        return var.get()
    except ValueError:
        return 0

# TODO Add scrollbar
