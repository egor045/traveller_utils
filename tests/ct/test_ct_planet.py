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
        ''' CT Planet test create'''
        p = Planet()
        self.assertIsInstance(p, Planet)
    
    def test_trade_classification(self):
        ''' CT Planet trade classificaions'''

        # Ag
        for atm in "456789":
            for hyd in "45678":
                for pop in "567":
                    upp = "X5{}{}{}00-0".format(atm, hyd, pop)
                    p1977 = Planet(upp=upp, mode="1977")
                    p1981 = Planet(upp=upp, mode="1981")
                    self.log.debug("upp: %s p1977 TCs: %s p1981 TCs: %s", upp, p1977.trade_classifications, p1981.trade_classifications)
                    self.assertTrue("Ag" in p1977.trade_classifications)
                    self.assertTrue("Ag" in p1981.trade_classifications)
        # Na
        for atm in "0123":
            for hyd in "0123":
                for pop in "6789A":
                    upp = "X5{}{}{}00-0".format(atm, hyd, pop)
                    p1977 = Planet(upp=upp, mode="1977")
                    p1981 = Planet(upp=upp, mode="1981")
                    self.log.debug("upp: %s p1977 TCs: %s p1981 TCs: %s", upp, p1977.trade_classifications, p1981.trade_classifications)
                    self.assertTrue("Na" in p1977.trade_classifications)
                    self.assertTrue("Na" in p1981.trade_classifications)
        # In
        for atm in "012479":
            for pop in "9A":
                upp = "X5{}0{}00-0".format(atm, pop)
                p1977 = Planet(upp=upp, mode="1977")
                p1981 = Planet(upp=upp, mode="1981")
                self.log.debug("upp: %s p1977 TCs: %s p1981 TCs: %s", upp, p1977.trade_classifications, p1981.trade_classifications)
                self.assertTrue("In" in p1977.trade_classifications)
                self.assertTrue("In" in p1981.trade_classifications)
        # Ni
        for pop in "0123456":
            upp = "X550{}00-0".format(pop)
            p1977 = Planet(upp=upp, mode="1977")
            p1981 = Planet(upp=upp, mode="1981")
            self.log.debug("upp: %s p1977 TCs: %s p1981 TCs: %s", upp, p1977.trade_classifications, p1981.trade_classifications)
            self.assertTrue("Ni" in p1977.trade_classifications)
            self.assertTrue("Ni" in p1981.trade_classifications)
        # Ri
        for gov in "456789":
            for atm in "68":
                for pop in "678":
                    upp = "X5{}0{}{}0-0".format(atm, pop, gov)
                    p1977 = Planet(upp=upp, mode="1977")
                    p1981 = Planet(upp=upp, mode="1981")
                    self.log.debug("upp: %s p1977 TCs: %s p1981 TCs: %s", upp, p1977.trade_classifications, p1981.trade_classifications)
                    self.assertTrue("Ri" in p1977.trade_classifications)
                    self.assertTrue("Ri" in p1981.trade_classifications)
        # Po
        for atm in "2345":
            for hyd in "0123":
                upp = "X5{}{}500-0".format(atm, hyd)
                p1977 = Planet(upp=upp, mode="1977")
                p1981 = Planet(upp=upp, mode="1981")
                self.log.debug("upp: %s p1977 TCs: %s p1981 TCs: %s", upp, p1977.trade_classifications, p1981.trade_classifications)
                self.assertTrue("Po" in p1977.trade_classifications)
                self.assertTrue("Po" in p1981.trade_classifications)
        # De
        p1981 = Planet(upp="X510000-0")
        self.log.debug("upp: %s p1981 TCs: %s", upp, p1981.trade_classifications)
        self.assertTrue("De" in p1981.trade_classifications)
        p1981 = Planet(upp="X000000-0")
        self.log.debug("upp: %s p1981 TCs: %s", upp, p1981.trade_classifications)
        self.assertTrue("De" not in p1981.trade_classifications)
        # Va
        p1981 = Planet(upp="X500000-0")
        self.log.debug("upp: %s p1981 TCs: %s", upp, p1981.trade_classifications)
        self.assertTrue("Va" in p1981.trade_classifications)
        p1981 = Planet(upp="X000000-0")
        self.log.debug("upp: %s p1981 TCs: %s", upp, p1981.trade_classifications)
        self.assertTrue("Va" not in p1981.trade_classifications)
        # As
        p1981 = Planet(upp="X000000-0")
        self.log.debug("upp: %s p1981 TCs: %s", upp, p1981.trade_classifications)
        self.assertTrue("As" in p1981.trade_classifications)
        # Ic
        for hyd in "123456789A":
            for atm in "01":
                p1981 = Planet(upp="X5{}{}000-0".format(atm, hyd))
                self.log.debug("upp: %s p1981 TCs: %s", upp, p1981.trade_classifications)
                self.assertTrue("Ic" in p1981.trade_classifications)
        for hyd in "123456789A":
            for atm in "3456789ABC":
                p1981 = Planet(upp="X5{}{}000-0".format(atm, hyd))
                self.log.debug("upp: %s p1981 TCs: %s", upp, p1981.trade_classifications)
                self.assertTrue("Ic" not in p1981.trade_classifications)