# -*- coding: utf-8 -*-

import unittest

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




    def test_add_string_string(self):
        self.assertRaises(code.concatenate('hola', 'hola'), 'holahola')



if __name__ == '__main__':
    unittest.main()
