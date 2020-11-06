'''test_ct_lbb6_systemgen.py'''

# pragma pylint: disable=C0413, E0401


import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import json
import logging
import unittest

from mock import patch

from traveller_utils.ct.lbb6_systemgen import (
    Star,
    System,
    bode,
    find_nearest_classification
)
from traveller_utils.util import Die

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

def mock_roll(dice=1, modifier=0, floor=0, ceiling=9999):
    ''' Fake roll - return 3 + modifier
    '''
    print("modifier = %d" % modifier)
    result = 3 * dice + modifier
    result = max(floor, result)
    result = min(ceiling, result)
    log.debug('returning %s', result)
    return result

def mock_randint(floor=0, ceiling=9):
    return 6

class TestStar(unittest.TestCase):
    ''' Star unit tests
    '''

    def setUp(self):
        ''' setUp
            - Logging
        '''
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(logging.DEBUG)
    
    @patch("traveller_utils.util.Die.roll", side_effect=mock_roll)
    @patch("traveller_utils.ct.lbb6_systemgen.randint", side_effect=mock_randint)
    def test_star(self, mock_roll, mock_randint):
        star = Star()
        self.log.debug("star = %s", str(star))
        self.assertTrue(star.type == "M")
        self.assertTrue(star.size == "V")
        self.assertTrue(star.classification == 6)


class TestBode(unittest.TestCase):
    ''' Bode function unit tests
    '''

    def setUp(self):
        ''' setUp
            - Logging
        '''
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(logging.DEBUG)
    
    def test_bode(self):
        test_data = {
             0: {"AU": 0.2, "mkm": 29.9},
             1: {"AU": 0.4, "mkm": 59.8},
             2: {"AU": 0.7, "mkm": 104.7},
            11: {"AU": 154.0, "mkm": 23038.4}
        }
        for orbit_number in test_data.keys():
            expected = test_data[orbit_number]
            result = bode(orbit_number)
            self.log.debug("orbit_number=%d expected=%s actual AU=%s", orbit_number, expected, result)
            self.assertTrue(expected["AU"] == result["AU"])
            self.assertTrue(expected["mkm"] == result["mkm"])


class TestFindNearestClassification(unittest.TestCase):
    ''' find_nearest_classification function unit tests
    '''

    def setUp(self):
        ''' setUp
            - Logging
        '''
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(logging.DEBUG)

    def test_find_nearest_classification(self):
        data = [
            {"search": "A0II", "expected": "A0II"},
            {"search": "A2II", "expected": "A0II"},
            {"search": "A4II", "expected": "A5II"},
            {"search": "A5II", "expected": "A5II"},
            {"search": "A7II", "expected": "A5II"},
            {"search": "A8II", "expected": "F0II"},
            {"search": "M8II", "expected": "M9II"},
            {"search": "M2V", "expected": "M0V"},
            {"search": "DB", "expected": "DB"}
        ]
        for i in data:
            result = find_nearest_classification(i["search"])
            self.log.debug("search = %s expected = %s result = %s", i["search"], i["expected"], result)
            self.assertTrue(i["expected"] == result)


class TestSystemGen(unittest.TestCase):

    def setUp(self):
        ''' setUp
            - Logging
        '''
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(logging.DEBUG)

    def test_systemgen(self):
        s = System(loglevel=logging.DEBUG)
        self.log.info("primary: %s", str(s.primary))
        if len(s.companions) != 0:
            for c in s.companions:
                self.log.info("companion: %s", str(c))
        for k in s.orbits.keys():
            self.log.info("orbit %d: %s", k, s.orbits[k])
        self.log.info("test run complete")
        self.assertTrue(0 == 1)