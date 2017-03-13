# -*- coding: utf-8 -*-
import errno


def sum_elements(*args):
    output = None
    if len(args) < 2:
        output = errno.EPERM
    elif len(args) > 10:
        output = errno.E2BIG

    # Control de errores
    # por que no puedo hacer esto:
    # [output = errno.EINVAL for arg in args if not(isinstance(arg, str)
    # or isinstance(arg, int) or isinstance(arg, float))]
    else:
        for arg in args:
            if not(isinstance(arg, str) or isinstance(arg, int) or isinstance(arg, float)):
                output = errno.EINVAL
            if isinstance(arg, str):
                output = ''

        if output is '':
            for arg in args:
                output = output + str(arg)

        elif output is None:
            output = sum(args)

    return output


def concatenate(*args):
    chain = ''
    output = None
    if len(args) < 2:
        output = errno.EPERM
    elif len(args) > 10:
        output = errno.E2BIG
    for string in args:
        if not isinstance(string, str):
            output = errno.EINVAL
        elif len(string) > 10:
            output = errno.EINVAL

    if output is None:
        for string in args:
            chain = chain + string
        output = chain.replace(" ", "")

    return output


if __name__ == "__main__":
    print concatenate('hola', 'hola')
    print sum_elements('hola', 1, 2, 'buenas', 7, 'quetal', 2.543, '?', 23, -54, -4.3)