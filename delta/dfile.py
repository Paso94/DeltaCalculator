from delta import delta

__author__ = 'Paso'
__date__ = '07/03/2016'


def fsave(filename):
    """
        :param filename: string

    """
    file = open(filename, 'w')
    file.write(str(delta.printer))
    file.close()


def fopen(filename):
    """
        :param filename: string

    """
    file = open(filename, 'r')
    dlt = file.read()
    file.close()
    return eval(dlt)
