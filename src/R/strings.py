
__author__ = 'Paso'
__date__ = '02/11/2015'

# Window title
title = "Delta Calculator"
# Inputs
input = "Inputs"
pv_title = "Printing Volume"
pgr_name = "Printing Radius"
pgr_symbol = "[pgr]"
pgh_name = "Printing Height"
pgh_symbol = "[pgh]"
ho_title = "Horizontal Offsets"
eo_name = "Effector Offset"
eo_symbol = "[eo]"
co_name = "Carriage Offset"
co_symbol = "[co]"
vo_title = "Vertical Offsets"
so_name = "Endstop Offset"
so_symbol = "[so]"
no_name = "Nozzle Offset"
no_symbol = "[no]"
bo_name = "Bed Offset"
bo_symbol = "[bo]"

# Outputs
output = "Outputs"
g_title = "Geometry"
dr_name = "Diagonal Rod"
dr_symbol = "[dr]"
sro_name = "Smoooth Rod Offset"
sro_symbol = "[sro]"
a_title = "Angles"
mina_name = "Min Angle"
mina_symbol = "[α]"
ha_name = "Home Angle"
ha_symbol = "[ha]"
maxa_name = "Max Angle"
maxa_symbol = "[β]"
h_title = "Heights"
ph_name = "Printer Height"
ph_symbol = "[ph]"
zh_name = "Z Home Position"
zh_symbol = "[zh]"

# Menu
preferences_menu = "Preferences"
language_menu = "Language"
default_menu = "Are you sure?"

#File 
cancel_file = "Opening canceled"
not_valid_file = "File not valid"

__file__ = open("src/preferences", 'r')
__preferences__ = eval(__file__.read())
__file__.close()

if __preferences__['language'] == "EN":
    pass

if __preferences__['language'] == "IT":
    # Inputs
    pv_title = "Volume di Stampa"
    pgr_name = "Raggio di Stampa"
    pgh_name = "Altezza di Stampa"
    ho_title = "Offsets Orizzontali"
    eo_name = "Offset dell'Effector"
    co_name = "Offset del Carrello"
    vo_title = "Offsets Verticali"
    so_name = "Offset dell'Endstop"
    no_name = "Offset del Nozzle"
    bo_name = "Offset del Piano"
    # Outputs
    g_title = "Geometria"
    dr_name = "Barre diagonali"
    sro_name = "Offset delle Barre Liscie"
    a_title = "Angoli"
    mina_name = "Angolo Minimo"
    ha_name = "Angolo in Home"
    maxa_name = "Angolo Massimo"
    h_title = "Altezze"
    ph_name = "Altezza della Stampante"
    zh_name = "Z in Home"
    # Menu
    preferences_menu = "Preferenze"
    language_menu = "Lingua"
    default_menu = "Sei sicuro?"
    #File
    cancel_file = "Apertura annullata"
    not_valid_file = "File non valido"