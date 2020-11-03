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
    STELLAR_MAGNITUDE,
    STELLAR_LUMINOSITY,
    STELLAR_TEMPERATURE,
    STELLAR_RADIUS,
    STELLAR_MASS,
    PlanetaryOrbit
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


class TestPlanetaryOrbit(unittest.TestCase):
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
            orbit = PlanetaryOrbit(indx, radius_km)
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


class TestStellarTables(unittest.TestCase):
    ''' STELLAR_* tests
    '''

    def setUp(self):
        ''' setUp
            - Logging
        '''
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(logging.DEBUG)

    def test_magnitude(self):
        table_data = {
            "B0": {"Ia": -9.6, "Ib": -8.8, "II": -8.3,  "III": -7.8,  "IV": -7.5,  "V": -7.1},
            "B5": {"Ia": -8.5, "Ib": -6.9, "II": -5.9,  "III": -3.5,  "IV": -3.1,  "V": -2.71},
            "A0": {"Ia": -7.8, "Ib": -5.7, "II": -3.6,  "III": -1.36, "IV": -0.7,  "V": -0.1},
            "A5": {"Ia": -7.5, "Ib": -5.4, "II": -2.55, "III": -0.1,  "IV":  0.85, "V":  1.8},
            "F0": {"Ia": -7.2, "Ib": -4.9, "II": -2.18, "III":  0.45, "IV":  1.58, "V":  2.5},
            "F5": {"Ia": -7.0, "Ib": -4.5, "II": -2.0,  "III":  0.7,  "IV":  2.1,  "V":  3.4,  "VI": 4.8},
            "G0": {"Ia": -7.3, "Ib": -4.7, "II": -2.1,  "III":  0.52, "IV":  2.74, "V":  4.57, "VI": 5.97},
            "G5": {"Ia": -7.6, "Ib": -5.0, "II": -2.4,  "III":  0.08, "IV":  3.04, "V":  5.2,  "VI": 6.6},
            "K0": {"Ia": -7.7, "Ib": -5.4, "II": -2.6,  "III": -0.17, "IV":  3.1 , "V":  5.7,  "VI": 7.1},
            "K5": {"Ia": -7.8, "Ib": -6.0, "II": -3.7,  "III": -1.5,               "V":  7.4,  "VI": 8.8},
            "M0": {"Ia": -7.9, "Ib": -6.9, "II": -4.4,  "III": -1.9,               "V":  8.25, "VI": 9.65},
            "M5": {"Ia": -8.0, "Ib": -7.6, "II": -5.65, "III": -3.6,               "V": 10.2,  "VI": 11.6},
            "M9": {"Ia": -8.1, "Ib": -7.9, "II": -5.75, "III": -3.8,               "V": 13.9,  "VI": 15.3},
            "D": {"B": 8.1, "A": 10.5, "F": 13.6, "G": 15.3, "K": 15.6, "M": 15.9}
        }
        for clss in table_data.keys():
            for size in table_data[clss].keys():
                expected = table_data[clss][size]
                actual = STELLAR_MAGNITUDE.lookup(clss)[size]
                self.log.debug("star=%s%s expected=%f actual=%f", clss, size, expected, actual)
                self.assertTrue(expected == actual)

    def test_luminosity(self):
        table_data = {
            "B0": {"Ia": 560000.0, "Ib": 270000.0, "II": 170000.0, "III": 107000.0, "IV": 81000.0,  "V": 56000.0},
            "B5": {"Ia": 204000.0, "Ib":  46700.0, "II":  18600.0, "III":   6700.0, "IV":  2000.0,  "V":  1400.0},
            "A0": {"Ia": 107000.0, "Ib":  15000.0, "II":   2200.0, "III":    280.0, "IV":   156.0,  "V":    90.0},
            "A5": {"Ia":  81000.0, "Ib":  11700.0, "II":    850.0, "III":     90.0, "IV":    37.0,  "V":    16.0},
            "F0": {"Ia":  61000.0, "Ib":   7400.0, "II":    600.0, "III":     53.0, "IV":    19.0,  "V":     8.1},
            "F5": {"Ia":  51000.0, "Ib":   5100.0, "II":    510.0, "III":     43.0, "IV":    12.0,  "V":     3.5,   "VI": 0.977},
            "G0": {"Ia":  67000.0, "Ib":   6100.0, "II":    560.0, "III":     50.0, "IV":     6.5,  "V":     1.21,  "VI": 0.322},
            "G5": {"Ia":  89000.0, "Ib":   8100.0, "II":    740.0, "III":     75.0, "IV":     4.9,  "V":     0.67,  "VI": 0.186},
            "K0": {"Ia":  97000.0, "Ib":  11700.0, "II":    890.0, "III":     95.0, "IV":     4.67, "V":     0.42,  "VI": 0.117 },
            "K5": {"Ia": 107000.0, "Ib":  20400.0, "II":   2450.0, "III":    320.0,                 "V":     0.08,  "VI": 0.025},
            "M0": {"Ia": 117000.0, "Ib":  46000.0, "II":   4600.0, "III":    470.0,                 "V":     0.04,  "VI": 0.011},
            "M5": {"Ia": 129000.0, "Ib":  89000.0, "II":  14900.0, "III":   2280.0,                 "V":     0.007, "VI": 0.002},
            "M9": {"Ia": 141000.0, "Ib": 117000.0, "II":  16200.0, "III":   2690.0,                 "V":     0.001, "VI": 0.00006},
            "D": {"B": 0.046, "A": 0.005, "F": 0.0003, "G": 0.00006, "K": 0.00004, "M": 0.00003}
        }
        for clss in table_data.keys():
            for size in table_data[clss].keys():
                expected = table_data[clss][size]
                actual = STELLAR_LUMINOSITY.lookup(clss)[size]
                self.log.debug("star=%s%s expected=%f actual=%f", clss, size, expected, actual)
                self.assertTrue(expected == actual)
    
    def test_temperature(self):
        table_data = {
            "B0": {"Ia": 22000, "Ib": 24000, "II": 25000, "III": 26000, "IV": 27000, "V": 28000},
            "B5": {"Ia": 14200, "Ib": 14500, "II": 15100, "III": 15200, "IV": 15400, "V": 15500},
            "A0": {"Ia":  9000, "Ib":  9100, "II":  9300, "III":  9500, "IV":  9700, "V":  9900},
            "A5": {"Ia":  8000, "Ib":  8100, "II":  8200, "III":  8300, "IV":  8400, "V":  8500},
            "F0": {"Ia":  6900, "Ib":  7000, "II":  7100, "III":  7200, "IV":  7300, "V":  7400},
            "F5": {"Ia":  6100, "Ib":  6300, "II":  6400, "III":  6500, "IV":  6600, "V":  6700, "VI": 6800},
            "G0": {"Ia":  5400, "Ib":  5600, "II":  5700, "III":  5800, "IV":  5900, "V":  6000, "VI": 6100},
            "G5": {"Ia":  4700, "Ib":  4850, "II":  5000, "III":  5100, "IV":  5200, "V":  5500, "VI": 5600},
            "K0": {"Ia":  4000, "Ib":  4100, "II":  4300, "III":  4500, "IV":  4700, "V":  4900, "VI": 5000},
            "K5": {"Ia":  3300, "Ib":  3500, "II":  3650, "III":  3800,              "V":  4100, "VI": 4200},
            "M0": {"Ia":  2800, "Ib":  2900, "II":  3100, "III":  3400,              "V":  3500, "VI": 3600},
            "M5": {"Ia":  2000, "Ib":  2200, "II":  2400, "III":  2650,              "V":  2800, "VI": 2900},
            "M9": {"Ia":  1900, "Ib":  2000, "II":  2100, "III":  2200,              "V":  2300, "VI": 2400},
            "D": {"B": 25000, "A": 14000, "F": 6600, "G": 4500, "K": 3500, "M": 2700}
        }
        for clss in table_data.keys():
            for size in table_data[clss].keys():
                expected = table_data[clss][size]
                actual = STELLAR_TEMPERATURE.lookup(clss)[size]
                self.log.debug("star=%s%s expected=%d actual=%d", clss, size, expected, actual)
                self.assertTrue(expected == actual)

    def test_radius(self):
        table_data = {
            "B0": {"Ia":   52.0, "Ib":   30.0, "II":  22.0, "III":  16.0, "IV": 13.0, "V": 10.0},
            "B5": {"Ia":   75.0, "Ib":   35.0, "II":  20.0, "III":  10.0, "IV":  5.3, "V":  4.4},
            "A0": {"Ia":  135.0, "Ib":   50.0, "II":  18.0, "III":   6.2, "IV":  4.5, "V":  3.2},
            "A5": {"Ia":  149.0, "Ib":   55.0, "II":  14.0, "III":   4.6, "IV":  2.7, "V":  1.8},
            "F0": {"Ia":  174.0, "Ib":   59.0, "II":  16.0, "III":   4.7, "IV":  2.7, "V":  1.7},
            "F5": {"Ia":  204.0, "Ib":   60.0, "II":  18.0, "III":   5.2, "IV":  2.6, "V":  1.4,   "VI": 1.14},
            "G0": {"Ia":  298.0, "Ib":   84.0, "II":  25.0, "III":   7.1, "IV":  2.5, "V":  1.03,  "VI": 1.02},
            "G5": {"Ia":  454.0, "Ib":  128.0, "II":  37.0, "III":  11.0, "IV":  2.8, "V":  0.91,  "VI": 0.55},
            "K0": {"Ia":  654.0, "Ib":  216.0, "II":  54.0, "III":  16.0, "IV":  3.3, "V":  0.908, "VI": 0.4},
            "K5": {"Ia": 1010.0, "Ib":  392.0, "II": 124.0, "III":  42.0,             "V":  0.566, "VI": 0.308},
            "M0": {"Ia": 1467.0, "Ib":  857.0, "II": 237.0, "III":  63.0,             "V":  0.549, "VI": 0.256},
            "M5": {"Ia": 3020.0, "Ib": 2073.0, "II": 712.0, "III": 228.0,             "V":  0.358, "VI": 0.104},
            "M9": {"Ia": 3499.0, "Ib": 2876.0, "II": 931.0, "III": 360.0,             "V":  0.201, "VI": 0.053},
            "D": {"B": 0.018, "A": 0.017, "F": 0.013, "G": 0.012, "K": 0.009, "M": 0.006}
        }
        for clss in table_data.keys():
            for size in table_data[clss].keys():
                expected = table_data[clss][size]
                actual = STELLAR_RADIUS.lookup(clss)[size]
                self.log.debug("star=%s%s expected=%f actual=%f", clss, size, expected, actual)
                self.assertTrue(expected == actual)

    def test_mass(self):
        table_data = {
            "B0": {"Ia": 60.0, "Ib": 50.0, "II": 30.0, "III": 25.0, "IV": 20.0,  "V": 18.0},
            "B5": {"Ia": 30.0, "Ib": 25.0, "II": 20.0, "III": 15.0, "IV": 10.0,  "V":  6.5},
            "A0": {"Ia": 18.0, "Ib": 16.0, "II": 14.0, "III": 12.0, "IV":  6.0,  "V":  3.2},
            "A5": {"Ia": 15.0, "Ib": 13.0, "II": 11.0, "III":  9.0, "IV":  4.0,  "V":  2.1},
            "F0": {"Ia": 13.0, "Ib": 12.0, "II": 10.0, "III":  8.0, "IV":  2.5,  "V":  1.7},
            "F5": {"Ia": 12.0, "Ib": 10.0, "II":  8.1, "III":  5.0, "IV":  2.0,  "V":  1.3,   "VI": 0.8},
            "G0": {"Ia": 12.0, "Ib": 10.0, "II":  8.1, "III":  2.5, "IV":  1.75, "V":  1.04,  "VI": 0.6},
            "G5": {"Ia": 13.0, "Ib": 12.0, "II": 10.0, "III":  3.2, "IV":  2.0,  "V":  0.94,  "VI": 0.528},
            "K0": {"Ia": 14.0, "Ib": 13.0, "II": 11.0, "III":  4.0, "IV":  2.3,  "V":  0.825, "VI": 0.43},
            "K5": {"Ia": 18.0, "Ib": 16.0, "II": 14.0, "III":  5.0,              "V":  0.570, "VI": 0.33},
            "M0": {"Ia": 20.0, "Ib": 16.0, "II": 14.0, "III":  6.3,              "V":  0.489, "VI": 0.154},
            "M5": {"Ia": 25.0, "Ib": 20.0, "II": 16.0, "III":  7.4,              "V":  0.331, "VI": 0.104},
            "M9": {"Ia": 30.0, "Ib": 25.0, "II": 18.0, "III":  9.2,              "V":  0.215, "VI": 0.058},
            "D": {"B": 0.26, "A": 0.36, "F": 0.42, "G": 0.63, "K": 0.83, "M": 1.11}
        }
        for clss in table_data.keys():
            for size in table_data[clss].keys():
                expected = table_data[clss][size]
                actual = STELLAR_MASS.lookup(clss)[size]
                self.log.debug("star=%s%s expected=%f actual=%f", clss, size, expected, actual)
                self.assertTrue(expected == actual)
