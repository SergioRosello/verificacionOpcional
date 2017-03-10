# -*- coding: utf-8 -*-
import errno


def concatenate(*args):
    output = ''
    if len(args) < 2 or len(args) > 10:
        return errno.EPERM
    for string in args:
        output = output + string
    return output


    for string in args:
        string = string + string[i]
        i


if __name__ == "__main__":
    concatenate('hola', 'hola')