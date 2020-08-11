'''test_trade_classifications.py'''

# pragma pylint: disable=C0413, E0401


import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import json
import logging
import unittest

from traveller_utils.ct.trade_classifications import TradeClassification


class TestTradeClassifications(unittest.TestCase):
    ''' Test trade classifications'''

    def test_valid_tc(self):
        ''' trade_classification create valid'''
        for tc in [
            "Ag",
            "Na",
            "In",
            "Ni",
            "Ri",
            "Po",
            "Wa",
            "De",
            "As",
            "Ic"
        ]:
            classification = TradeClassification(tc)
            self.assertTrue(tc == str(classification))
    
    def test_invalid_tc(self):
        ''' trade_classification create invalid'''
        for tc in [
            1,
            "bogus"
        ]:
            with self.assertRaises(ValueError):
                _ = TradeClassification(tc)
