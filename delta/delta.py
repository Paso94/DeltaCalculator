from math import sqrt
from delta.dmath import *

__author__ = 'Paso'
__date__ = '07/03/2016'


class Delta:
    # precision of float
    precision_linear = 2
    precision_angle = 4

    def __init__(self, pgr, pgh, minad=30, maxad=80, eo=0, co=0, so=0, no=0, bo=0, dr=0, sro=0, ph=0):
        # Volume
        self.pgr = pgr  # Printing radius
        self.pgh = pgh  # Printing height
        # default angle
        self.minad = minad  # Min angle default
        self.maxad = maxad  # Max angle default
        # Horizontal offsets
        self.eo = eo  # Effector offset
        self.co = co  # Carriage offset
        # Vertical offsets
        self.so = so  # Endstop offset
        self.no = no  # Nozzle offset
        self.bo = bo  # Bed offset
        # Geometry
        self.dr = dr  # Diagonal rod
        self.sro = sro  # Smooth rod offset
        # Printer height
        self.ph = ph  # Printer height

    def __repr__(self):
        return "{ 'pgr':" + str(self.pgr) + ", 'pgh':" + str(self.pgh) + \
               ", 'minad':" + str(self.minad) + ", 'maxad':" + str(self.maxad) + \
               ", 'eo':" + str(self.eo) + ", 'co':" + str(self.co) + \
               ", 'so':" + str(self.so) + ", 'no':" + str(self.no) + ", 'bo':" + str(self.bo) + \
               ", 'dr':" + str(self.dr) + ", 'sro':" + str(self.sro) + ", 'ph':" + str(self.ph) + " }"

    # Inputs ###################################################################

    # Volume

    # Printing radius
    @property
    def pgr(self):
        return round(self._pgr, self.precision_linear)

    @pgr.setter
    def pgr(self, value):
        self._pgr = to_numb(value)

    # Printing height
    @property
    def pgh(self):
        return round(self._pgh, self.precision_linear)

    @pgh.setter
    def pgh(self, value):
        self._pgh = to_numb(value)

    # Default angle

    # Min angle default
    @property
    def minad(self):
        return round(self._minad, self.precision_angle)

    @minad.setter
    def minad(self, value):
        self._minad = to_numb(value, max=90)

    # Max angle default
    @property
    def maxad(self):
        return round(self._maxad, self.precision_angle)

    @maxad.setter
    def maxad(self, value):
        self._maxad = to_numb(value, min=self._minad, max=90)

    # Horizontal offsets

    # Effector offset
    @property
    def eo(self):
        return round(self._eo, self.precision_linear)

    @eo.setter
    def eo(self, value):
        self._eo = to_numb(value)

    # Carriage offset
    @property
    def co(self):
        return round(self._co, self.precision_linear)

    @co.setter
    def co(self, value):
        self._co = to_numb(value)

    # Vertical offsets

    # Endstop offset
    @property
    def so(self):
        return round(self._so, self.precision_linear)

    @so.setter
    def so(self, value):
        self._so = to_numb(value)

    # Nozzle offset
    @property
    def no(self):
        return round(self._no, self.precision_linear)

    @no.setter
    def no(self, value):
        self._no = to_numb(value)

    # Bed offset
    @property
    def bo(self):
        return round(self._bo, self.precision_linear)

    @bo.setter
    def bo(self, value):
        self._bo = to_numb(value)

    # Outputs ###################################################################

    # Geometry

    # Diagonal rod default
    @property
    def drd(self):
        try:
            return round(2 * self.pgr / (cos(self.minad) - cos(self.maxad)), self.precision_linear)
        except ZeroDivisionError:
            return 0.0

    # Diagonal rod min
    @property
    def dr_min(self):
        return 2 * self.pgr

    # Diagonal rod
    @property
    def dr(self):
        return round(self._dr, self.precision_linear)

    @dr.setter
    def dr(self, value):
        try:
            self._dr = to_numb(value, min=self.dr_min)
        except ValueError:
            self._dr = to_numb(self.dr_min)

    # Smooth rod offset default
    @property
    def srod(self):
        return round(self.eo + self.co + self.pgr + self.dr * cos(self.maxad), self.precision_linear)

    # Smooth rod offset min
    @property
    def sro_min(self):
        return self.eo + self.co + self.pgr

    # Smooth rod offset max
    @property
    def sro_max(self):
        return self.eo + self.co + self.dr - self.pgr

    # Smooth rod offset
    @property
    def sro(self):
        return round(self._sro, self.precision_linear)

    @sro.setter
    def sro(self, value):
        try:
            self._sro = to_numb(value, min=self.sro_min, max=self.sro_max)
        except ValueError:
            if value < self.sro_min:
                self._sro = to_numb(self.sro_min)
            elif value > self.sro_max:
                self._sro = to_numb(self.sro_max)
            else:
                raise AttributeError("C'è un bug nel codice")

    # Angles

    # Min angle
    @property
    def mina(self):
        return round(acos((self._sro - self._eo - self._co + self._pgr) / self._dr), self.precision_angle)

    # Home angle
    @property
    def ha(self):
        return round(acos((self._sro - self._eo - self._co) / self._dr), self.precision_angle)

    # Max angle
    @property
    def maxa(self):
        return round(acos((self._sro - self._eo - self._co - self._pgr) / self._dr), self.precision_angle)

    # Joint angle
    @property
    def aja(self):
        return round(atan(self._pgr / (self._sro - self._eo - self._co)), self.precision_angle)

    # Heights

    # Printer height min
    @property
    def ph_min(self):
        return round(self._pgh + self._dr * sin(self.maxa) + self._so + self._no + self._bo, self.precision_linear)

    # Printer height default
    @property
    def phd(self):
        return round(math.ceil(self.ph_min), self.precision_linear)

    # Printer height
    @property
    def ph(self):
        return round(self._ph, self.precision_linear)

    @ph.setter
    def ph(self, value):
        try:
            self._ph = to_numb(value, min=self.ph_min)
        except ValueError:
            if value < self.ph_min:
                self._ph = to_numb(self.ph_min)
            else:
                raise AttributeError("C'è un bug nel codice")

    # Z Home position
    @property
    def zh(self):
        return round(self.ph - (self._so + self._no + self._bo) - sqrt(self._dr ** 2 - (self._sro - self._eo - self._co) ** 2),
                     self.precision_linear)

    # Others ################################################################

    @property
    def inputs(self):
        return self._pgr, self._pgh, self._minad, self._maxad, self._eo, self._co, self._so, self._no, self._bo

    @property
    def outputs(self):
        return self._dr, self._sro, self._ph

    @property
    def output_values(self):
        return self.drd, self.srod, self.mina, self.ha, self.maxa, self.phd, self.z


printer = Delta(**eval(open('delta/delta.cache', 'r').read()))
