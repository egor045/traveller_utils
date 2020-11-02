'''test_ct_lbb6_continuation.py'''

# pragma pylint: disable=C0413, E0401


import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import json
import logging
import unittest

from traveller_utils.ct.lbb6_systemgen_tables import (
    SYSTEM_NATURE_TABLE, 
    PRIMARY_TYPE, 
    PRIMARY_SIZE,
    COMPANION_TYPE,
    COMPANION_SIZE,
    COMPANION_ORBIT,
    MAX_ORBITS,
    GAS_GIANT_PRESENT,
    GAS_GIANT_QTY,
    PLANETOID_PRESENT,
    PLANETOID_QTY,
    PLANETARY_ORBITS,
    SATELLITE_RING_ORBITS,
    SATELLITE_CLOSE_ORBITS,
    SATELLITE_FAR_ORBITS,
    SATELLITE_EXTREME_ORBITS,
    CAPTURED_PLANETS_PRESENCE,
    CAPTURED_PLANETS_QTY,
    ZONES,
    Orbit
)
from traveller_utils.util import Die

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

def mock_roll(dice, modifier):
    ''' Fake roll - return 3 + modifier
    '''
    print("modifier = %d" % modifier)
    return 3 * dice  + int(modifier)


class TestSystemNatureTable(unittest.TestCase):
    ''' SYSTEM_NATURE_TABLE unit tests'''

    def setUp(self):
        ''' setUp
            - Logging
        '''
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(logging.DEBUG)

    def test_system_nature_table(self):
        ''' SYSTEM_NATURE_TABLE test contents'''

        expected = {
            0: "Solo", 1: "Solo", 2: "Solo", 3: "Solo", 4: "Solo", 5: "Solo", 6: "Solo", 7: "Solo",
            8: "Binary", 9: "Binary", 10: "Binary", 11: "Binary",
            12: "Trinary"
        }
        for roll in expected.keys():
            result = SYSTEM_NATURE_TABLE.lookup(roll)
            self.log.debug("roll = %d expected = %s actual = %s", roll, expected[roll], result)
            self.assertTrue(result == expected[roll])


class TestPrimaryTables(unittest.TestCase):
    ''' PRIMARY_* unit tests'''

    def setUp(self):
        ''' setUp
            - Logging
        '''
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(logging.DEBUG)

    def test_primary_type_table(self):
        ''' PRIMARY_TYPE test contents'''

        expected = {
            0: "B", 1: "B", 2: "A", 3: "M", 4: "M", 5: "M", 6: "M", 7: "M",
            8: "K", 9: "G", 10: "F", 11: "F", 12: "F"
        }
        for roll in expected.keys():
            result = PRIMARY_TYPE.lookup(roll)
            self.log.debug("roll = %d expected = %s actual = %s", roll, expected[roll], result)
            self.assertTrue(result == expected[roll])

    def test_primary_SIZE_table(self):
        ''' PRIMARY_SIZE test contents'''

        expected = {
            0: "Ia", 1: "Ib", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "V", 7: "V",
            8: "V", 9: "V", 10: "V", 11: "VI", 12: "D"
        }
        for roll in expected.keys():
            result = PRIMARY_SIZE.lookup(roll)
            self.log.debug("roll = %d expected = %s actual = %s", roll, expected[roll], result)
            self.assertTrue(result == expected[roll])


class TestCompanionTables(unittest.TestCase):
    ''' COMPANION_* unit tests'''

    def setUp(self):
        ''' setUp
            - Logging
        '''
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(logging.DEBUG)

    def test_companion_type_table(self):
        ''' COMPANION_TYPE test contents'''

        expected = {
            1: "B", 2: "A", 3: "F", 4: "F", 5: "G", 6: "G", 7: "K",
            8: "K", 9: "M", 10: "M", 11: "M", 12: "M"
        }
        for roll in expected.keys():
            result = COMPANION_TYPE.lookup(roll)
            self.log.debug("roll = %d expected = %s actual = %s", roll, expected[roll], result)
            self.assertTrue(result == expected[roll])

    def test_companion_size_table(self):
        ''' COMPANION_SIZE test contents'''

        expected = {
            0: "Ia", 1: "Ib", 2: "II", 3: "III", 4: "IV", 5: "D", 6: "D", 7: "V",
            8: "V", 9: "VI", 10: "D", 11: "D", 12: "D"
        }
        for roll in expected.keys():
            result = COMPANION_SIZE.lookup(roll)
            self.log.debug("roll = %d expected = %s actual = %s", roll, expected[roll], result)
            self.assertTrue(result == expected[roll])

    def test_companion_orbit_table(self):
        ''' COMPANION_ORBIT test contents'''

        expected = {
            0: ["Close"], 1: ["Close"], 2: ["Close"], 3: ["Close"], 4: [1], 5: [2], 6: [3], 
            7: range(5, 11), 8: range(6, 12), 9: range(7, 13), 
            10: range(8, 14), 11: range(9, 15), 12: ["Far"]
        }
        for roll in expected.keys():
            result = COMPANION_ORBIT.lookup(roll)
            self.log.debug("roll = %d expected = %s actual = %s", roll, expected[roll], result)
            self.assertTrue(result in expected[roll])


class TestMaxOrbits(unittest.TestCase):
    ''' MaxOrbits tests
    '''

    def setUp(self):
        ''' setUp
            - Logging
        '''
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(logging.DEBUG)

    def test_max_orbits_roll(self):

        for roll in range(0, 12):
            result = MAX_ORBITS.lookup(roll)
            self.log.debug("roll = %d actual = %s", roll, result)
            self.assertTrue(result == roll)
    
        result = MAX_ORBITS.lookup(-1)
        self.assertTrue(result == 0)

        result = MAX_ORBITS.lookup(15)
        self.assertTrue(result == 12)


class TestGasGiantTables(unittest.TestCase):
    ''' GAS_GIANT_* test contents'''

    def setUp(self):
        ''' setUp
            - Logging
        '''
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(logging.DEBUG)

    def test_gas_giant_present_table(self):
        expected = {
            1: "yes", 2: "yes", 3: "yes", 4: "yes", 5: "yes", 6: "yes", 7: "yes", 8: "yes", 9: "yes", 
            10: "no", 11: "no", 12: "no"
        }
        for roll in expected.keys():
            result = GAS_GIANT_PRESENT.lookup(roll)
            self.log.debug("roll = %d expected = %s actual = %s", roll, expected[roll], result)
            self.assertTrue(result == expected[roll])

    def test_gas_giant_qty_table(self):
        expected = {
            1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6:3, 7: 3, 8: 4, 9: 4, 10: 4, 11: 5, 12: 5
        }
        for roll in expected.keys():
            result = GAS_GIANT_QTY.lookup(roll)
            self.log.debug("roll = %d expected = %s actual = %s", roll, expected[roll], result)
            self.assertTrue(result == expected[roll])


class TestPlanetoidTables(unittest.TestCase):
    ''' PLANETOID_* test contents'''

    def setUp(self):
        ''' setUp
            - Logging
        '''
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(logging.DEBUG)

    def test_gas_giant_present_table(self):
        expected = {
            0: "yes", 1: "yes", 2: "yes", 3: "yes", 4: "yes", 5: "yes", 6: "yes", 
            7: "no", 8: "no", 9: "no", 10: "no", 11: "no", 12: "no"
        }
        for roll in expected.keys():
            result = PLANETOID_PRESENT.lookup(roll)
            self.log.debug("roll = %d expected = %s actual = %s", roll, expected[roll], result)
            self.assertTrue(result == expected[roll])

    def test_gas_giant_qty_table(self):
        expected = {
            0: 3, 1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7:1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1
        }
        for roll in expected.keys():
            result = PLANETOID_QTY.lookup(roll)
            self.log.debug("roll = %d expected = %s actual = %s", roll, expected[roll], result)
            self.assertTrue(result == expected[roll])


class TestOrbit(unittest.TestCase):
    ''' Orbit tests'''

    def setUp(self):
        ''' setUp
            - Logging
        '''
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(logging.DEBUG)

    def test_orbit(self):
        expected = {
            0: (29.9, 0.2), 1: (59.8, 0.4), 2: (104.7, 0.7), 3: (149.6, 1.0)
        }
        for indx in expected.keys():
            radius_km = expected[indx][0]
            radius_au = expected[indx][1]
            orbit = Orbit(indx, radius_km)
            self.log.debug(
                "indx = %d radius_km = %f radius_au = %f orbit.number = %d, orbit.radius_km = %f orbit.radius_au = %f", 
                indx, radius_km, radius_au, orbit.number, orbit.radius_km, orbit.radius_au
            )

            self.assertTrue(orbit.number == indx)
            self.assertTrue(orbit.radius_km == radius_km)
            self.assertTrue(orbit.radius_au == radius_au)


class TestPlanetaryOrbits(unittest.TestCase):

    ''' PLANETARY_ORBITS tests'''

    def setUp(self):
        ''' setUp
            - Logging
        '''
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(logging.DEBUG)

    def test_orbit(self):
        expected = {
            0: (29.9, 0.2), 1: (59.8, 0.4), 2: (104.7, 0.7), 3: (149.6, 1.0),
            4: (239.3, 1.6), 5: (418.9, 2.8), 6: (777.9, 5.2), 7: (1495.9, 10.0),
            8: (2932.0, 19.6), 9: (5804.0, 38.8), 10: (11548.0, 77.2), 11: (23038.0, 154.0),
            12: (46016.0, 307.6), 13: (91972.0, 614.8), 14: (183885.0, 1229.2), 15: (367711.0, 2458.0)
        }
        for indx in expected.keys():
            radius_km = expected[indx][0]
            radius_au = expected[indx][1]
            result = PLANETARY_ORBITS.lookup(indx)
            self.log.debug(
                "indx = %d radius_km = %f radius_au = %f result.number = %d, result.radius_km = %f result.radius_au = %f", 
                indx, radius_km, radius_au, result.number, result.radius_km, result.radius_au
            )

            self.assertTrue(result.number == indx)
            self.assertTrue(result.radius_km == radius_km)
            self.assertTrue(result.radius_au == radius_au)


class TestSatelliteOrbits(unittest.TestCase):
    ''' SatelliteOrbits tests
    '''

    def setUp(self):
        ''' setUp
            - Logging
        '''
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(logging.DEBUG)

    def test_satellite_close_orbits_roll(self):

        for roll in range(2, 12):
            expected = roll + 1
            result = SATELLITE_CLOSE_ORBITS.lookup(roll)
            self.log.debug("roll = %d expected = %d actual = %d", roll, expected, result)
            self.assertTrue(result == expected)
    
        for r in [(-1, 3), (15, 13)]:
            roll = r[0]
            expected = r[1]
            result = SATELLITE_CLOSE_ORBITS.lookup(roll)
            self.log.debug("roll = %d expected = %d actual = %d", roll, expected, result)
            self.assertTrue(result == expected)

    def test_satellite_far_orbits_roll(self):

        for roll in range(2, 12):
            expected = (roll + 1) * 5
            result = SATELLITE_FAR_ORBITS.lookup(roll)
            self.log.debug("roll = %d expected = %d actual = %d", roll, expected, result)
            self.assertTrue(result == expected)
    
        for r in [(-1, 15), (15, 65)]:
            roll = r[0]
            expected = r[1]
            result = SATELLITE_FAR_ORBITS.lookup(roll)
            self.log.debug("roll = %d expected = %d actual = %d", roll, expected, result)
            self.assertTrue(result == expected)

    def test_satellite_extreme_orbits_roll(self):

        for roll in range(2, 12):
            expected = (roll + 1) * 25
            result = SATELLITE_EXTREME_ORBITS.lookup(roll)
            self.log.debug("roll = %d expected = %d actual = %d", roll, expected, result)
            self.assertTrue(result == expected)
    
        for r in [(-1,75), (15, 325)]:
            roll = r[0]
            expected = r[1]
            result = SATELLITE_EXTREME_ORBITS.lookup(roll)
            self.log.debug("roll = %d expected = %d actual = %d", roll, expected, result)
            self.assertTrue(result == expected)


class TestCapturedPlanets(unittest.TestCase):
    ''' CAPTURED_PLANETS_* tests
    '''

    def setUp(self):
        ''' setUp
            - Logging
        '''
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(logging.DEBUG)

    def test_captured_planets_presence(self):
        table_data = {
            1: "no", 2: "no", 3: "no", 4: "no",
            5: "yes", 6: "yes"
        }
        for roll in table_data.keys():
            expected = table_data[roll]
            result = CAPTURED_PLANETS_PRESENCE.lookup(roll)
            self.log.debug("roll = %d expected = %s actual = %s", roll, expected, result)
            self.assertTrue(result == expected)
    
    def test_captured_planets_qty(self):
        for roll in range(1, 6):
            expected = int((roll + 1) / 2)
            result = CAPTURED_PLANETS_QTY.lookup(roll)
            self.log.debug("roll = %d expected = %d actual = %d", roll, expected, result)
            self.assertTrue(result == expected)


class TestZones(unittest.TestCase):
    ''' ZONES tests
    '''

    def setUp(self):
        ''' setUp
            - Logging
        '''
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(logging.DEBUG)

    def test_zones(self):
        table_data = {
            "Ia": {
                "B0": {"interior": -1, "inner": 8, "habitable": 13},
                "B5": {"interior": -1, "inner": 7, "habitable": 12},
                "A0": {"interior":  1, "inner": 7, "habitable": 12},
                "A5": {"interior":  1, "inner": 7, "habitable": 12},
                "F0": {"interior":  2, "inner": 6, "habitable": 12},
                "F5": {"interior":  2, "inner": 6, "habitable": 11},
                "G0": {"interior":  3, "inner": 7, "habitable": 12},
                "G5": {"interior":  4, "inner": 7, "habitable": 12},
                "K0": {"interior":  5, "inner": 7, "habitable": 12},
                "K5": {"interior":  5, "inner": 7, "habitable": 12},
                "M0": {"interior":  6, "inner": 7, "habitable": 12},
                "M5": {"interior":  7, "inner": 8, "habitable": 12},
                "M9": {"interior":  7, "inner": 8, "habitable": 12}
            },
            "Ib": {
                "B0": {"interior": -1, "inner": 8, "habitable": 13},
                "B5": {"interior": -1, "inner": 6, "habitable": 11},
                "A0": {"interior": -1, "inner": 5, "habitable": 11},
                "A5": {"interior": -1, "inner": 5, "habitable": 10},
                "F0": {"interior": -1, "inner": 5, "habitable": 10},
                "F5": {"interior": -1, "inner": 4, "habitable": 10},
                "G0": {"interior": -1, "inner": 4, "habitable": 10},
                "G5": {"interior":  1, "inner": 5, "habitable": 10},
                "K0": {"interior":  3, "inner": 5, "habitable": 10},
                "K5": {"interior":  4, "inner": 6, "habitable": 11},
                "M0": {"interior":  5, "inner": 6, "habitable": 11},
                "M5": {"interior":  6, "inner": 7, "habitable": 12},
                "M9": {"interior":  7, "inner": 8, "habitable": 12}
            },
            "II": {
                "B0": {"interior": -1, "inner": 7, "habitable": 12},
                "B5": {"interior": -1, "inner": 5, "habitable": 11},
                "A0": {"interior": -1, "inner": 3, "habitable":  9},
                "A5": {"interior": -1, "inner": 2, "habitable":  8},
                "F0": {"interior": -1, "inner": 2, "habitable":  8},
                "F5": {"interior": -1, "inner": 2, "habitable":  8},
                "G0": {"interior": -1, "inner": 2, "habitable":  8},
                "G5": {"interior": -1, "inner": 2, "habitable":  8},
                "K0": {"interior": -1, "inner": 2, "habitable":  9},
                "K5": {"interior": -1, "inner": 3, "habitable":  9},
                "M0": {"interior":  3, "inner": 4, "habitable": 10},
                "M5": {"interior":  5, "inner": 6, "habitable": 11},
                "M9": {"interior":  5, "inner": 6, "habitable": 11}
            },
            "III": {
                "B0": {"interior": -1, "inner": 7, "habitable": 12},
                "B5": {"interior": -1, "inner": 5, "habitable": 10},
                "A0": {"interior": -1, "inner": 1, "habitable":  8},
                "A5": {"interior": -1, "inner": 1, "habitable":  7},
                "F0": {"interior": -1, "inner": 1, "habitable":  6},
                "F5": {"interior": -1, "inner": 1, "habitable":  6},
                "G0": {"interior": -1, "inner": 1, "habitable":  6},
                "G5": {"interior": -1, "inner": 1, "habitable":  7},
                "K0": {"interior": -1, "inner": 1, "habitable":  7},
                "K5": {"interior": -1, "inner": 1, "habitable":  8},
                "M0": {"interior": -1, "inner": 2, "habitable":  8},
                "M5": {"interior":  3, "inner": 4, "habitable":  9},
                "M9": {"interior":  4, "inner": 5, "habitable":  9}
            },
            "IV": {
                "B0": {"interior": -1, "inner": 7, "habitable": 12},
                "B5": {"interior": -1, "inner": 3, "habitable":  9},
                "A0": {"interior": -1, "inner": 1, "habitable":  7},
                "A5": {"interior": -1, "inner": 0, "habitable":  6},
                "F0": {"interior": -1, "inner": 0, "habitable":  6},
                "F5": {"interior": -1, "inner": 0, "habitable":  5},
                "G0": {"interior": -1, "inner": 0, "habitable":  5},
                "G5": {"interior": -1, "inner": 0, "habitable":  5},
                "K0": {"interior": -1, "inner": 0, "habitable":  4}
            },
            "V": {
                "B0": {"interior": -1, "inner":  6, "habitable": 12},
                "B5": {"interior": -1, "inner":  3, "habitable":  9},
                "A0": {"interior": -1, "inner":  0, "habitable":  7},
                "A5": {"interior": -1, "inner":  0, "habitable":  6},
                "F0": {"interior": -1, "inner":  0, "habitable":  5},
                "F5": {"interior": -1, "inner":  0, "habitable":  4},
                "G0": {"interior": -1, "inner":  0, "habitable":  3},
                "G5": {"interior": -1, "inner":  0, "habitable":  2},
                "K0": {"interior": -1, "inner":  0, "habitable":  2},
                "K5": {"interior": -1, "inner": -1, "habitable":  0},
                "M0": {"interior": -1, "inner": -1, "habitable":  0},
                "M5": {"interior": -1, "inner": -1, "habitable": -1},
                "M9": {"interior": -1, "inner": -1, "habitable": -1}
            },
            "VI": {
                "F5": {"interior": -1, "inner":  0, "habitable":  3},
                "G0": {"interior": -1, "inner":  0, "habitable":  2},
                "G5": {"interior": -1, "inner":  0, "habitable":  1},
                "K0": {"interior": -1, "inner":  0, "habitable":  1},
                "K5": {"interior": -1, "inner": -1, "habitable": -1},
                "M0": {"interior": -1, "inner": -1, "habitable": -1},
                "M5": {"interior": -1, "inner": -1, "habitable": -1},
                "M9": {"interior": -1, "inner": -1, "habitable": -1}
            },
            "D": {
                "B": {"interior": -1, "inner": -1, "habitable":  0},
                "A": {"interior": -1, "inner": -1, "habitable": -1},
                "F": {"interior": -1, "inner": -1, "habitable": -1},
                "G": {"interior": -1, "inner": -1, "habitable": -1},
                "K": {"interior": -1, "inner": -1, "habitable": -1},
                "M": {"interior": -1, "inner": -1, "habitable": -1}
            }
        }
        for size in table_data.keys():
            for star_type in table_data[size].keys():
                expected = table_data[size][star_type]
                if size == "D":
                    code = "D{}".format(star_type)
                else:
                    code = "{}{}".format(star_type, size)
                result = ZONES.lookup(code)
                self.log.debug("code = %s expected = %s result = %s", code, expected, result)
                self.assertTrue(expected["interior"] == result["interior"])
                self.assertTrue(expected["inner"] == result["inner"])
                self.assertTrue(expected["habitable"] == result["habitable"])
