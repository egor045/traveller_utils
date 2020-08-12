'''test_ct_planet.py'''

# pragma pylint: disable=C0413, E0401


import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import json
import logging
import unittest

from traveller_utils.ct.planet import Planet

logging.basicConfig()


class TestCTPlanet(unittest.TestCase):
    ''' CT Planet unit tests'''

    def setUp(self):
        ''' setUp
            - Logging
        '''
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(logging.DEBUG)
    
    def test_create(self):
        ''' Planet test create'''
        p = Planet()
        self.assertIsInstance(p, Planet)
    
