# -*- coding: utf-8 -*-

import unittest
import errno

from .context import code

class CoreTestSuite(unittest.TestCase):


    def test_concatenate(self):
        # SET-UP
        str1 = 'hola'
        str2 = 'hola'

        # EXECUTION
        result = code.concatenate(str1, str2)

        # ASSERT
        self.assertEqual(result, 'holahola', "El resultado no es el esperado")

#https://docs.python.org/2/library/errno.html


    def test_concatenate_string_with_more_than_ten_characters(self):
        self.assertEqual(code.concatenate('moreThanTenCharacters', '<10Chars'), errno.EINVAL)

    def test_concatenate_one_string(self):
        self.assertEqual(code.concatenate('hola'), errno.EPERM)

    def test_concatenate_more_than_ten_strings(self):
        self.assertEqual(code.concatenate('h', 'o', 'l', 'a', ', ', 'q', 'u', 'e', 't', 'a', 'l'), errno.E2BIG)

    def test_concatenate_two_strings(self):
        self.assertEquals(code.concatenate('hola', 'hola'), 'holahola')



if __name__ == '__main__':
    unittest.main()
