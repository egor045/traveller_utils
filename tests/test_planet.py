'''test_planet.py'''

# pragma pylint: disable=C0413, E0401


import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import json
import logging
import unittest

from traveller_utils.planet import BasePlanet, Starport

logging.basicConfig()


class TestStarport(unittest.TestCase):
    ''' Starport unit tests'''

    def setUp(self):
        ''' setUp
            - Logging
        '''
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(logging.DEBUG)

    def test_create(self):
        ''' Starport test create'''
        for c in ["A", "B", "C", "D", "E", "X", "a", "b", "c", "d", "e", "x"]:
            s = Starport(c)
            self.assertIsInstance(s, Starport)
            self.assertTrue(str(s) == c.upper())
    
    def test_create_bogus(self):
        ''' Starport test invalid create'''
        for c in ["AA", "M", 31]:
            with self.assertRaises(ValueError):
                _ = Starport(c)


class TestBasePlanet(unittest.TestCase):
    ''' BasePlanet unit tests'''

    def setUp(self):
        ''' setUp
            - Logging
        '''
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(logging.DEBUG)
    
    def test_create(self):
        ''' BasePlanet test create'''
        p = BasePlanet()
        self.assertIsInstance(p, BasePlanet)
    
    def test_import(self):
        ''' BasePlanet test import'''
        upp = "A867943-B"
        p = BasePlanet(upp)
        self.log.debug("p = %s", str(p))
        self.assertTrue(str(p) == upp)
        self.assertTrue(p.starport == "A")
        self.assertTrue(p.size == 8)
        self.assertTrue(p.atmosphere == 6)
        self.assertTrue(p.hydrographics == 7)
        self.assertTrue(p.population == 9)
        self.assertTrue(p.government == 4)
        self.assertTrue(p.law_level == 3)
        self.assertTrue(p.tech_level == "B")

    def test_import_invalid_upp(self):
        ''' BasePlanet test import'''
        upp = "A867943B"
        with self.assertRaises(ValueError):
            _ = BasePlanet(upp)
