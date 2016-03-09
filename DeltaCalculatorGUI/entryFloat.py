from tkinter import Entry

import DeltaCalculatorGUI.colors
import DeltaCalculatorGUI.dimensions
from delta import delta

__author__ = 'Paso'
__date__ = '06/11/2015'


class EntryFloat(Entry):
    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self['validate'] = 'key'
        vcmd = (parent.register(self._validate), '%P')
        self['validatecommand'] = vcmd

    def _validate(self, entry_value):
        if entry_value == '':
            self['bg'] = DeltaCalculatorGUI.colors.alert
            return True
        try:
            if float(entry_value) < 0 or entry_value[::-1].find('.') > delta.Delta.precision_linear:
                return False
        except ValueError:
            return False
        if float(entry_value) == 0:
            self['bg'] = DeltaCalculatorGUI.colors.alert
            return True
        self['bg'] = DeltaCalculatorGUI.colors.bg
        return True

    def set(self, s):
        self.delete(0, DeltaCalculatorGUI.dimensions.width_entries)
        self.insert(0, s)
