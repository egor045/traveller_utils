'''test_ct_subsector.py'''

# pragma pylint: disable=C0413, E0401


import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import json
import logging
import unittest

from traveller_utils.ct.subsector import Subsector
from traveller_utils.ct.planet import Planet

logging.basicConfig()


class TestCTSubsector(unittest.TestCase):
    ''' CT Subsector unit tests'''

    def setUp(self):
        ''' setUp
            - Logging
        '''
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(logging.DEBUG)
    
    def test_create(self):
        ''' CT Subsector test create'''
        s = Subsector("test subsector")
        self.assertTrue(s.name == "test subsector")
        self.assertTrue(len(s.hexes) == 80)

    def test_generate(self):
        ''' CT Subsector test generate'''

        s = Subsector()
        s.generate(dm=4)    # Guarantees a planet in every hex
        for h in s.hexes.keys():
            self.assertIsInstance(s.hexes[h], Planet)
