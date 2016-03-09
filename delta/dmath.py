import math

__author__ = 'Paso'
__date__ = '07/03/2016'


def cos(angle):
    return math.cos(math.radians(angle))


def sin(angle):
    return math.sin(math.radians(angle))


def acos(value):
    try:
        return math.degrees(math.acos(value))
    except ValueError:
        print(value)
        return -1


def asin(value):
    try:
        return math.degrees(math.asin(value))
    except ValueError:
        print(value)
        return -1


def to_numb(arg, type='float', min=0.0, max=float('inf')):
    """
        :param arg: object
        :param type: Optional 'int'
        :param min: Optional
        :param max: Optional
    """
    if type == 'float':
        arg = float(arg)
    elif type == 'int':
        arg = int(arg)
    else:
        raise AttributeError("'numb' not valid : is only valid 'float' and 'int'")
    min = float(min)
    max = float(max)
    if min < 0:
        raise AttributeError("'min' is < of 0")
    if min > max:
        raise AttributeError("'min' is > of 'max'")
    if min > arg or arg > max:
        raise ValueError("'arg' is out of limits")
    return arg
