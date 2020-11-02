'''lbb6_systemgen_tables.py'''

from traveller_utils.util import Die, Table


class MaxOrbits(Table):
    ''' MaxOrbits - extends Table()
        Uses simple 2D6 roll for result
    '''

    def __init__(self):
        super().__init__()
    
    def lookup(self, indx):
        '''
        Return value matching indx
        '''
        if indx <= 0:
            return 0
        elif indx >= 12:
            return 12
        else:
            return int(indx)


class Orbit(object):

    def __init__(self, number, radius):
        self.__number = int(number)
        self.__radius_km = float(radius)
        self.__radius_au = round((self.__radius_km / 149.6), 1)

    @property
    def number(self):
        return self.__number
    
    @property
    def radius_km(self):
        return self.__radius_km
    
    @property
    def radius_au(self):
        return self.__radius_au


class SatelliteOrbit(Table):
    ''' SatrelliteOrbit - extends Table()
        Uses simple 2D6 roll for result
    '''

    def __init__(self, typ):
        super().__init__()
        try:
            assert str(typ).lower() in ["close", "far", "extreme"]
            self.type = str(typ).lower()
        except AssertionError:
            raise ValueError("Invalid type {}".format(typ))


    def lookup(self, indx):
        if int(indx) < 2:
            indx = 2
        if int(indx) > 12:
            indx = 12

        if self.type == "close":
            return int(indx) + 1
        elif self.type == "far":
            return (int(indx) + 1) * 5
        else:
            return (int(indx) + 1) * 25


D6 = Die(6)

# SYSTEM_NATURE
SYSTEM_NATURE_TABLE = Table()
SYSTEM_NATURE_TABLE.add_row((0,7), "Solo")
SYSTEM_NATURE_TABLE.add_row((8, 11), "Binary")
SYSTEM_NATURE_TABLE.add_row(12, "Trinary")
SYSTEM_NATURE_TABLE.dice = 2
SYSTEM_NATURE_TABLE.floor = 0
SYSTEM_NATURE_TABLE.ceiling = 12

# PRIMARY_TYPE
PRIMARY_TYPE = Table()
PRIMARY_TYPE.dice = 2
PRIMARY_TYPE.floor = 0
PRIMARY_TYPE.ceiling = 12
PRIMARY_TYPE.add_row((0, 1), "B")
PRIMARY_TYPE.add_row(2, "A")
PRIMARY_TYPE.add_row((3, 7), "M")
PRIMARY_TYPE.add_row(8, "K")
PRIMARY_TYPE.add_row(9, "G")
PRIMARY_TYPE.add_row((10, 12), "F")

# PRIMARY_SIZE
PRIMARY_SIZE = Table()
PRIMARY_SIZE.dice = 2
PRIMARY_SIZE.floor = 0
PRIMARY_SIZE.ceiling = 12
PRIMARY_SIZE.add_row(0, "Ia")
PRIMARY_SIZE.add_row(1, "Ib")
PRIMARY_SIZE.add_row(2, "II")
PRIMARY_SIZE.add_row(3, "III")
PRIMARY_SIZE.add_row(4, "IV")
PRIMARY_SIZE.add_row((5, 10), "V")
PRIMARY_SIZE.add_row(11, "VI")
PRIMARY_SIZE.add_row(12, "D")

# COMPANION_TYPE
COMPANION_TYPE = Table()
COMPANION_TYPE.dice = 2
COMPANION_TYPE.floor = 0
COMPANION_TYPE.ceiling = 12
COMPANION_TYPE.add_row(1, "B")
COMPANION_TYPE.add_row(2, "A")
COMPANION_TYPE.add_row((3, 4), "F")
COMPANION_TYPE.add_row((5, 6), "G")
COMPANION_TYPE.add_row((7, 8), "K")
COMPANION_TYPE.add_row((9, 12), "M")

# COMPANION_SIZE
COMPANION_SIZE = Table()
COMPANION_SIZE.dice = 2
COMPANION_SIZE.floor = 0
COMPANION_SIZE.ceiling = 12
COMPANION_SIZE.add_row(0, "Ia")
COMPANION_SIZE.add_row(1, "Ib")
COMPANION_SIZE.add_row(2, "II")
COMPANION_SIZE.add_row(3, "III")
COMPANION_SIZE.add_row(4, "IV")
COMPANION_SIZE.add_row((5, 6), "D")
COMPANION_SIZE.add_row((7, 8), "V")
COMPANION_SIZE.add_row(9, "VI")
COMPANION_SIZE.add_row((10, 12), "D")

# COMPANION_ORBIT
COMPANION_ORBIT = Table()
COMPANION_ORBIT.dice = 2
COMPANION_ORBIT.floor = 0
COMPANION_ORBIT.ceiling = 12
COMPANION_ORBIT.add_row((0, 3), "Close")
COMPANION_ORBIT.add_row(4, 1)
COMPANION_ORBIT.add_row(5, 2)
COMPANION_ORBIT.add_row(6, 3)
COMPANION_ORBIT.add_row(7, D6.roll(dice=1, modifier=4))
COMPANION_ORBIT.add_row(8, D6.roll(dice=1, modifier=5))
COMPANION_ORBIT.add_row(9, D6.roll(dice=1, modifier=6))
COMPANION_ORBIT.add_row(10, D6.roll(dice=1, modifier=7))
COMPANION_ORBIT.add_row(11, D6.roll(dice=1, modifier=8))
COMPANION_ORBIT.add_row(12, "Far")

# MAX_ORBITS
MAX_ORBITS = MaxOrbits()
MAX_ORBITS.dice = 2
MAX_ORBITS.floor = 0
MAX_ORBITS.ceiling = 12

# GAS_GIANT_PRESENT
GAS_GIANT_PRESENT = Table()
GAS_GIANT_PRESENT.dice = 2
GAS_GIANT_PRESENT.floor = 0
GAS_GIANT_PRESENT.ceiling = 12
GAS_GIANT_PRESENT.add_row((1,9), "yes")
GAS_GIANT_PRESENT.add_row((10, 12), "no")

# GAS_GIANT+QTY
GAS_GIANT_QTY = Table()
GAS_GIANT_QTY.dice = 2
GAS_GIANT_QTY.floor = 1
GAS_GIANT_QTY.ceiling = 12
GAS_GIANT_QTY.add_row((1, 3), 1)
GAS_GIANT_QTY.add_row((4, 5), 2)
GAS_GIANT_QTY.add_row((6, 7), 3)
GAS_GIANT_QTY.add_row((8, 10), 4)
GAS_GIANT_QTY.add_row((11, 12), 5)

# PLANETOID_PRESENT
PLANETOID_PRESENT = Table()
PLANETOID_PRESENT.dice = 2
PLANETOID_PRESENT.floor = 0
PLANETOID_PRESENT.ceiling = 12
PLANETOID_PRESENT.add_row((0, 6), "yes")
PLANETOID_PRESENT.add_row((7, 12), "no")

# PLANETOID_QTY
PLANETOID_QTY = Table()
PLANETOID_QTY.dice = 2
PLANETOID_QTY.floor = 0
PLANETOID_QTY.ceiling = 12
PLANETOID_QTY.add_row(0, 3)
PLANETOID_QTY.add_row((1, 6), 2)
PLANETOID_QTY.add_row((7, 12), 1)

# PLANETARY_ORBITS
PLANETARY_ORBITS = Table()
PLANETARY_ORBITS.dice = 2
PLANETARY_ORBITS.floor = 0
PLANETARY_ORBITS.ceiling = 15
PLANETARY_ORBITS.add_row(0, Orbit(0, 29.9))
PLANETARY_ORBITS.add_row(1, Orbit(1, 59.8))
PLANETARY_ORBITS.add_row(2, Orbit(2, 104.7))
PLANETARY_ORBITS.add_row(3, Orbit(3, 149.6))
PLANETARY_ORBITS.add_row(4, Orbit(4, 239.3))
PLANETARY_ORBITS.add_row(5, Orbit(5, 418.9))
PLANETARY_ORBITS.add_row(6, Orbit(6, 777.9))
PLANETARY_ORBITS.add_row(7, Orbit(7, 1495.9))
PLANETARY_ORBITS.add_row(8, Orbit(8, 2932))
PLANETARY_ORBITS.add_row(9, Orbit(9, 5804))
PLANETARY_ORBITS.add_row(10, Orbit(10, 11548))
PLANETARY_ORBITS.add_row(11, Orbit(11, 23038))
PLANETARY_ORBITS.add_row(12, Orbit(12, 46016))
PLANETARY_ORBITS.add_row(13, Orbit(13, 91972))
PLANETARY_ORBITS.add_row(14, Orbit(14, 183885))
PLANETARY_ORBITS.add_row(15, Orbit(15, 367711))

# SATELLITE_RING_ORBITS
SATELLITE_RING_ORBITS = Table()
SATELLITE_RING_ORBITS.dice = 1
SATELLITE_RING_ORBITS.floor = 1
SATELLITE_RING_ORBITS.ceiling = 6
SATELLITE_RING_ORBITS.add_row((1,3), 1)
SATELLITE_RING_ORBITS.add_row((4, 5), 2)
SATELLITE_RING_ORBITS.add_row(6, 3)

# SATELLITE_CLOSE_ORBITS
SATELLITE_CLOSE_ORBITS = SatelliteOrbit("close")
SATELLITE_CLOSE_ORBITS.dice = 2
SATELLITE_CLOSE_ORBITS.floor = 2
SATELLITE_CLOSE_ORBITS.ceiling = 12

# SATELLITE_FAR_ORBITS
SATELLITE_FAR_ORBITS = SatelliteOrbit("far")
SATELLITE_FAR_ORBITS.dice = 2
SATELLITE_FAR_ORBITS.floor = 2
SATELLITE_FAR_ORBITS.ceiling = 12

# SATELLITE_EXTREME_ORBITS
SATELLITE_EXTREME_ORBITS = SatelliteOrbit("extreme")
SATELLITE_EXTREME_ORBITS.dice = 2
SATELLITE_EXTREME_ORBITS.floor = 2
SATELLITE_EXTREME_ORBITS.ceiling = 12

# CAPTURED_PLANETS_PRESENCE
CAPTURED_PLANETS_PRESENCE = Table()
CAPTURED_PLANETS_PRESENCE.dice = 1
CAPTURED_PLANETS_PRESENCE.floor = 1
CAPTURED_PLANETS_PRESENCE.ceiling = 6
CAPTURED_PLANETS_PRESENCE.add_row((1, 4), "no")
CAPTURED_PLANETS_PRESENCE.add_row((5, 6), "yes")

# CAPTURED_PLANETS_QTY
CAPTURED_PLANETS_QTY = Table()
CAPTURED_PLANETS_QTY.dice = 1
CAPTURED_PLANETS_QTY.floor = 1
CAPTURED_PLANETS_QTY.ceiling = 6
CAPTURED_PLANETS_QTY.add_row((1, 2), 1)
CAPTURED_PLANETS_QTY.add_row((3, 4), 2)
CAPTURED_PLANETS_QTY.add_row((5, 6), 3)

# EMPTY_ORBITS_VACANT
EMPTY_ORBITS_VACANT = Table()
EMPTY_ORBITS_VACANT.dice = 1
EMPTY_ORBITS_VACANT.floor = 1
EMPTY_ORBITS_VACANT.ceiling = 6
EMPTY_ORBITS_VACANT.add_row((1, 4), "no")
EMPTY_ORBITS_VACANT.add_row((5, 6), "yes")

# EMPTY_ORNITS_QTY
EMPTY_ORBITS_QTY = Table()
EMPTY_ORBITS_QTY.dice = 1
EMPTY_ORBITS_QTY.floor = 1
EMPTY_ORBITS_QTY.ceiling = 6
EMPTY_ORBITS_QTY.add_row((1, 2), 1)
EMPTY_ORBITS_QTY.add_row((3, 4), 2)
EMPTY_ORBITS_QTY.add_row((5, 6), 3)

# ZONES
ZONES = Table()
# Subdwarfs
ZONES.add_row("F5VI", {"interior": -1, "inner": 0, "habitable": 3})
ZONES.add_row("G0VI", {"interior": -1, "inner": 0, "habitable": 2})
ZONES.add_row("G5VI", {"interior": -1, "inner": 0, "habitable": 1})
ZONES.add_row("K0VI", {"interior": -1, "inner": 0, "habitable": 1})
ZONES.add_row("K5VI", {"interior": -1, "inner": -1, "habitable": -1})
ZONES.add_row("M0VI", {"interior": -1, "inner": -1, "habitable": -1})
ZONES.add_row("M5VI", {"interior": -1, "inner": -1, "habitable": -1})
ZONES.add_row("M9VI", {"interior": -1, "inner": -1, "habitable": -1})
# White Dwarfs
ZONES.add_row("DB", {"interior": -1, "inner": -1, "habitable": 0})
ZONES.add_row("DA", {"interior": -1, "inner": -1, "habitable": -1})
ZONES.add_row("DF", {"interior": -1, "inner": -1, "habitable": -1})
ZONES.add_row("DG", {"interior": -1, "inner": -1, "habitable": -1})
ZONES.add_row("DK", {"interior": -1, "inner": -1, "habitable": -1})
ZONES.add_row("DM", {"interior": -1, "inner": -1, "habitable": -1})
ZONES.add_row("DA", {"interior": -1, "inner": -1, "habitable": -1})
# Bright Supergiants
ZONES.add_row("B0Ia", {"interior": -1, "inner": 8, "habitable": 13})
ZONES.add_row("B5Ia", {"interior": -1, "inner": 7, "habitable": 12})
ZONES.add_row("A0Ia", {"interior": 1, "inner": 7, "habitable": 12})
ZONES.add_row("A5Ia", {"interior": 1, "inner": 7, "habitable": 12})
ZONES.add_row("F0Ia", {"interior": 2, "inner": 6, "habitable": 12})
ZONES.add_row("F5Ia", {"interior": 2, "inner": 6, "habitable": 11})
ZONES.add_row("G0Ia", {"interior": 3, "inner": 7, "habitable": 12})
ZONES.add_row("G5Ia", {"interior": 4, "inner": 7, "habitable": 12})
ZONES.add_row("K0Ia", {"interior": 5, "inner": 7, "habitable": 12})
ZONES.add_row("K5Ia", {"interior": 5, "inner": 7, "habitable": 12})
ZONES.add_row("M0Ia", {"interior": 6, "inner": 7, "habitable": 12})
ZONES.add_row("M5Ia", {"interior": 7, "inner": 8, "habitable": 12})
ZONES.add_row("M9Ia", {"interior": 7, "inner": 8, "habitable": 12})
# Weaker Supergiants
ZONES.add_row("B0Ib", {"interior": -1, "inner": 8, "habitable": 13})
ZONES.add_row("B5Ib", {"interior": -1, "inner": 6, "habitable": 11})
ZONES.add_row("A0Ib", {"interior": -1, "inner": 5, "habitable": 11})
ZONES.add_row("A5Ib", {"interior": -1, "inner": 5, "habitable": 10})
ZONES.add_row("F0Ib", {"interior": -1, "inner": 5, "habitable": 10})
ZONES.add_row("F5Ib", {"interior": -1, "inner": 4, "habitable": 10})
ZONES.add_row("G0Ib", {"interior": -1, "inner": 4, "habitable": 10})
ZONES.add_row("G5Ib", {"interior": 1, "inner":  5, "habitable": 10})
ZONES.add_row("K0Ib", {"interior": 3, "inner":  5, "habitable": 10})
ZONES.add_row("K5Ib", {"interior": 4, "inner":  6, "habitable": 11})
ZONES.add_row("M0Ib", {"interior": 5, "inner":  6, "habitable": 11})
ZONES.add_row("M5Ib", {"interior": 6, "inner":  7, "habitable": 12})
ZONES.add_row("M9Ib", {"interior": 7, "inner":  8, "habitable": 12})
# Bright Giants
ZONES.add_row("B0II", {"interior": -1, "inner": 7, "habitable": 12})
ZONES.add_row("B5II", {"interior": -1, "inner": 5, "habitable": 11})
ZONES.add_row("A0II", {"interior": -1, "inner": 3, "habitable": 9})
ZONES.add_row("A5II", {"interior": -1, "inner": 2, "habitable": 8})
ZONES.add_row("F0II", {"interior": -1, "inner": 2, "habitable": 8})
ZONES.add_row("F5II", {"interior": -1, "inner": 2, "habitable": 8})
ZONES.add_row("G0II", {"interior": -1, "inner": 2, "habitable": 8})
ZONES.add_row("G5II", {"interior": -1, "inner": 2, "habitable": 8})
ZONES.add_row("K0II", {"interior": -1, "inner": 2, "habitable": 9})
ZONES.add_row("K5II", {"interior": -1, "inner": 3, "habitable": 9})
ZONES.add_row("M0II", {"interior":  3, "inner": 4, "habitable": 10})
ZONES.add_row("M5II", {"interior":  5, "inner": 6, "habitable": 11})
ZONES.add_row("M9II", {"interior":  5, "inner": 6, "habitable": 11})
# Giants
ZONES.add_row("B0III", {"interior": -1, "inner": 7, "habitable": 12})
ZONES.add_row("B5III", {"interior": -1, "inner": 5, "habitable": 10})
ZONES.add_row("A0III", {"interior": -1, "inner": 1, "habitable": 8})
ZONES.add_row("A5III", {"interior": -1, "inner": 1, "habitable": 7})
ZONES.add_row("F0III", {"interior": -1, "inner": 1, "habitable": 6})
ZONES.add_row("F5III", {"interior": -1, "inner": 1, "habitable": 6})
ZONES.add_row("G0III", {"interior": -1, "inner": 1, "habitable": 6})
ZONES.add_row("G5III", {"interior": -1, "inner": 1, "habitable": 7})
ZONES.add_row("K0III", {"interior": -1, "inner": 1, "habitable": 7})
ZONES.add_row("K5III", {"interior": -1, "inner": 1, "habitable": 8})
ZONES.add_row("M0III", {"interior": -1, "inner": 2, "habitable": 8})
ZONES.add_row("M5III", {"interior": 3, "inner": 4, "habitable": 9})
ZONES.add_row("M9III", {"interior": 4, "inner": 5, "habitable": 9})
# Subgiants
ZONES.add_row("B0IV", {"interior": -1, "inner": 7, "habitable": 12})
ZONES.add_row("B5IV", {"interior": -1, "inner": 3, "habitable": 9})
ZONES.add_row("A0IV", {"interior": -1, "inner": 1, "habitable": 7})
ZONES.add_row("A5IV", {"interior": -1, "inner": 0, "habitable": 6})
ZONES.add_row("F0IV", {"interior": -1, "inner": 0, "habitable": 6})
ZONES.add_row("F5IV", {"interior": -1, "inner": 0, "habitable": 5})
ZONES.add_row("G0IV", {"interior": -1, "inner": 0, "habitable": 5})
ZONES.add_row("G5IV", {"interior": -1, "inner": 0, "habitable": 5})
ZONES.add_row("K0IV", {"interior": -1, "inner": 0, "habitable": 4})
# Main Sequence Stars
ZONES.add_row("B0V", {"interior": -1, "inner": 6, "habitable": 12})
ZONES.add_row("B5V", {"interior": -1, "inner": 3, "habitable": 9})
ZONES.add_row("A0V", {"interior": -1, "inner": 0, "habitable": 7})
ZONES.add_row("A5V", {"interior": -1, "inner": 0, "habitable": 6})
ZONES.add_row("F0V", {"interior": -1, "inner": 0, "habitable": 5})
ZONES.add_row("F5V", {"interior": -1, "inner": 0, "habitable": 4})
ZONES.add_row("G0V", {"interior": -1, "inner": 0, "habitable": 3})
ZONES.add_row("G5V", {"interior": -1, "inner": 0, "habitable": 2})
ZONES.add_row("K0V", {"interior": -1, "inner": 0, "habitable": 2})
ZONES.add_row("K5V", {"interior": -1, "inner": -1, "habitable": 0})
ZONES.add_row("M0V", {"interior": -1, "inner": -1, "habitable": 0})
ZONES.add_row("M5V", {"interior": -1, "inner": -1, "habitable": -1})
ZONES.add_row("M9V", {"interior": -1, "inner": -1, "habitable": -1})

# SUBORDINATE_GOVERNMENT
SUBORDINATE_GOVERNMENT = Table()
SUBORDINATE_GOVERNMENT.dice = 1
SUBORDINATE_GOVERNMENT.floor = 1
SUBORDINATE_GOVERNMENT.ceiling = 5
SUBORDINATE_GOVERNMENT.add_row(1, 0)
SUBORDINATE_GOVERNMENT.add_row(2, 1)
SUBORDINATE_GOVERNMENT.add_row(3, 2)
SUBORDINATE_GOVERNMENT.add_row(4, 3)
SUBORDINATE_GOVERNMENT.add_row(5, 6)
