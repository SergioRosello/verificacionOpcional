# -*- coding: utf-8 -*-

import unittest
import errno

from .context import code

class CoreTestSuite(unittest.TestCase):

#https://docs.python.org/2/library/errno.html

    def test_concatenate_check_args_arent_strings(self):
        self.assertEqual(code.concatenate(True, 2), errno.EINVAL)

    def test_concatenate_check_args_are_strings(self):
        self.assertEqual(code.concatenate('hola', 'hola'), 'holahola')

    def test_concatenate_check_whitespaces(self):
        self.assertEqual(code.concatenate('pr ueb a', 'es paci o'), 'pruebaespacio', "El resultado no es el esperado")

    def test_concatenate_string_with_more_than_ten_characters(self):
        self.assertEqual(code.concatenate('moreThanTenCharacters', '<10Chars'), errno.EINVAL)

    def test_concatenate_one_string(self):
        self.assertEqual(code.concatenate('hola'), errno.EPERM)

    def test_concatenate_more_than_ten_strings(self):
        self.assertEqual(code.concatenate('h', 'o', 'l', 'a', ', ', 'q', 'u', 'e', 't', 'a', 'l'), errno.E2BIG)



    def test_sumaElementos_integer_numbers(self):
        self.assertEqual(code.sumaelementos(1, 2, 3, 4, 5, 6), 21)

    def test_sumaelementos_float_numbers(self):
        self.assertEqual(code.sumaelementos(2.3, 4.5), 6.8)

    def test_sumaelementos_integer_and_float(self):
        self.assertEqual(code.sumaelementos(2.3, 4), 6.3)

    def test_sumaelementos_string_and_number(self):
        self.assertEqual(code.sumaelementos('hola', 3), 'hola3')

    def test_sumaelementos_numbers_and_strings(self):
        self.assertEqual(code.sumaelementos(3, 'hola', 5, 6, 'buenas'), '3hola56buenas')

    def test_sumaelementos_only_one_argument(self):
        self.assertEqual(code.sumaelementos(4), errno.EPERM)

    def test_sumaelementos_more_than_ten_arguments(self):
        self.assertEqual(code.sumaelementos('hola', 1, 2, 'buenas', 7, 'quetal', 2.543, '?', 23, -54, -4.3), errno.E2BIG)



if __name__ == '__main__':
    unittest.main()
