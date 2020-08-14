'''MinMax test_util.py'''

# pragma pylint: disable=C0413, E0401


import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import json
import logging
import unittest

from mock import mock

import traveller_utils
from ehex import ehex

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

def mock_randint(min, max):
    ''' Fake randint - return int(max / 2)
    '''
    return int(max / 2)



class TestMinMax(unittest.TestCase):
    '''MinMax unit tests'''

    def test_min_max_basic(self):
        '''MinMax basic unit tests'''

        # No args => None, None
        minmax = traveller_utils.util.MinMax()
        self.assertTrue(minmax.min() is None)
        self.assertTrue(minmax.max() is None)

        # Test min vs max
        minmax = traveller_utils.util.MinMax(2, 1)
        self.assertTrue(minmax.min() == 1)
        self.assertTrue(minmax.max() == 2)
        minmax = traveller_utils.util.MinMax(1, 2)
        self.assertTrue(minmax.min() == 1)
        self.assertTrue(minmax.max() == 2)

        # Test min == max
        minmax = traveller_utils.util.MinMax(1, 1)
        self.assertTrue(minmax.min() == minmax.max())

    def test_representations(self):
        ''' MinMax test representations'''
        minmax = traveller_utils.util.MinMax(1, 2)
        self.assertTrue(minmax.dict() == {'min': 1, 'max': 2})
        self.assertTrue(str(minmax) == '<min = 1 max = 2>')
        LOGGER.debug('minmax.json() = %s', minmax.json())
        self.assertTrue(
            minmax.json() == json.dumps({'min': 1, 'max': 2}, sort_keys=True)
        )

    def test_valid_data_types(self):
        '''MinMax test data types'''
        tests = [
            1.5, 3.5,           # float-float
            1, 2.0,             # int-float
            'a', 'b',           # str-str
            'a', 'bbb',         # str-str
            [0, 1], [1, 0],     # list-list
            ehex(1), ehex(6),   # ehex-ehex
            1, ehex(6),         # int-ehex
            ehex(6), 'A',       # ehex-str
        ]
        i = 0
        while i < len(tests):
            v_1 = tests[i]
            v_2 = tests[i + 1]
            i += 2

            minmax = traveller_utils.util.MinMax(v_1, v_2)
            LOGGER.debug(
                'v_1 = %s v_2 = %s minmax = %s',
                v_1, v_2, str(minmax)
            )
            self.assertTrue(minmax.min() == v_1)
            self.assertTrue(minmax.max() == v_2)

    def test_invalid_data_types(self):
        '''MinMax test invalid data types'''
        tests = [
            {'a': 1, 'b': 3}, {'c': 1, 'd': 2}, # dict
        ]
        i = 0
        while i < len(tests):
            v_1 = tests[i]
            v_2 = tests[i + 1]
            i += 2

            with self.assertRaises(TypeError):
                LOGGER.debug('v_1 = %s v_2 = %s', v_1, v_2)
                _ = traveller_utils.util.MinMax(v_1, v_2)

    def test_invalid_comparisons(self):
        '''MinMax test invalid comparisons'''
        tests = [
            'a', 1,         # str-int
            'a', 1.0,       # str-float
            [1, 0], 1,      # list-int
            1.0, [1, 0],    # float-list
            1, None,        # int-None
            1.0, None,      # float-None
            'a', None,      # str-None
            [1, 0], None    # list-None
        ]
        i = 0
        while i < len(tests):
            v_1 = tests[i]
            v_2 = tests[i + 1]
            i += 2

            with self.assertRaises(TypeError):
                LOGGER.debug('v_1 = %s v_2 = %s', v_1, v_2)
                _ = traveller_utils.util.MinMax(v_1, v_2)

        # Test one param only
        with self.assertRaises(TypeError):
            _ = traveller_utils.util.MinMax(1)


class TestDie(unittest.TestCase):
    ''' Die unit tests'''

    def test_die_basic(self):
        ''' Die basic tests
            - Can create die
            - Can roll die
        '''
        d = traveller_utils.util.Die(6)
        r = d.roll()
        LOGGER.debug("roll = %s", r)
        self.assertTrue( 0 < r < 7)

    def test_modifier(self):
        ''' Die test effect of modifier
        '''
        with mock.patch('traveller_utils.util.randint', mock_randint):
            d = traveller_utils.util.Die(6)
            r = d.roll(dice=1, modifier=2)
            LOGGER.debug("roll = %s", r)
            self.assertTrue(r == 5)
    
    def test_floor(self):
        ''' Die test effect of floor
        '''
        with mock.patch('traveller_utils.util.randint', mock_randint):
            d = traveller_utils.util.Die(6)
            r = d.roll(dice=1, floor=4)
            LOGGER.debug("roll = %s", r)
            self.assertTrue(r == 4)
    
    def test_ceiling(self):
        ''' Die test effect of ceiling
        '''
        with mock.patch('traveller_utils.util.randint', mock_randint):
            d = traveller_utils.util.Die(6)
            r = d.roll(dice=1, ceiling=2)
            LOGGER.debug("roll = %s", r)
            self.assertTrue(r == 2)
