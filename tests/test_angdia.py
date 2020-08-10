'''test_angdia.py'''

# pragma pylint: disable=C0413, E0401


import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import json
import logging
import unittest

from math import atan2, pi

import traveller_utils

class TestAngdia(unittest.TestCase):
    ''' angdia unit tests'''

    def test_basic_deg(self):
        ''' angdia test calculations (deg)'''

        diameter = 3.0
        distance = 4.0
        expected = round(atan2(diameter, distance) * 180.0 / pi, 3)
        self.assertTrue(traveller_utils.angdia.angdia(diameter, distance, "deg") == expected)

        diameter = 3
        distance = 4
        expected = round(atan2(diameter, distance) * 180.0 / pi, 3)
        self.assertTrue(traveller_utils.angdia.angdia(diameter, distance, "deg") == expected)


    def test_basic_rad(self):
        ''' angdia test calculations (rad)'''

        diameter = 3.0
        distance = 4.0
        expected = round(atan2(diameter, distance), 3)
        self.assertTrue(traveller_utils.angdia.angdia(diameter, distance, "rad") == expected)

        diameter = 3
        distance = 4
        expected = round(atan2(diameter, distance), 3)
        self.assertTrue(traveller_utils.angdia.angdia(diameter, distance, "rad") == expected)

    def test_errors_args(self):
        ''' angdia test bad args'''
        mode = "foo"
        with self.assertRaises(ValueError):
            _ = traveller_utils.angdia.angdia(3, 4, mode)
            _ = traveller_utils.angdia.angdia("A", 3.1, "deg")
            _ = traveller_utils.angdia.angdia(-0.1, 3.1, "deg")