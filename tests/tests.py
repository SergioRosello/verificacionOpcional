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

    def test_concatenate_one_string(self):
        self.assertEqual(code.concatenate('hola'), errno.EPERM)

    def test_concatenate_string_string(self):
        self.assertEquals(code.concatenate('hola', 'hola'), 'holahola')



if __name__ == '__main__':
    unittest.main()
