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


class PlanetaryOrbit(object):

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
PLANETARY_ORBITS.add_row(0, PlanetaryOrbit(0, 29.9))
PLANETARY_ORBITS.add_row(1, PlanetaryOrbit(1, 59.8))
PLANETARY_ORBITS.add_row(2, PlanetaryOrbit(2, 104.7))
PLANETARY_ORBITS.add_row(3, PlanetaryOrbit(3, 149.6))
PLANETARY_ORBITS.add_row(4, PlanetaryOrbit(4, 239.3))
PLANETARY_ORBITS.add_row(5, PlanetaryOrbit(5, 418.9))
PLANETARY_ORBITS.add_row(6, PlanetaryOrbit(6, 777.9))
PLANETARY_ORBITS.add_row(7, PlanetaryOrbit(7, 1495.9))
PLANETARY_ORBITS.add_row(8, PlanetaryOrbit(8, 2932))
PLANETARY_ORBITS.add_row(9, PlanetaryOrbit(9, 5804))
PLANETARY_ORBITS.add_row(10, PlanetaryOrbit(10, 11548))
PLANETARY_ORBITS.add_row(11, PlanetaryOrbit(11, 23038))
PLANETARY_ORBITS.add_row(12, PlanetaryOrbit(12, 46016))
PLANETARY_ORBITS.add_row(13, PlanetaryOrbit(13, 91972))
PLANETARY_ORBITS.add_row(14, PlanetaryOrbit(14, 183885))
PLANETARY_ORBITS.add_row(15, PlanetaryOrbit(15, 367711))

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

# Stellar magnitude
STELLAR_MAGNITUDE = Table()
STELLAR_MAGNITUDE.add_row("B0", {"Ia": -9.6, "Ib": -8.8, "II": -8.3, "III": -7.8, "IV": -7.5, "V": -7.1})
STELLAR_MAGNITUDE.add_row("B5", {"Ia": -8.5, "Ib": -6.9, "II": -5.9, "III": -3.5, "IV": -3.1, "V": -2.71})
STELLAR_MAGNITUDE.add_row("A0", {"Ia": -7.8, "Ib": -5.7, "II": -3.6, "III": -1.36, "IV": -0.7, "V": -0.1})
STELLAR_MAGNITUDE.add_row("A5", {"Ia": -7.5, "Ib": -5.4, "II": -2.55, "III": -0.1, "IV": 0.85, "V": 1.8})
STELLAR_MAGNITUDE.add_row("F0", {"Ia": -7.2, "Ib": -4.9, "II": -2.18, "III": 0.45, "IV": 1.58, "V": 2.5})
STELLAR_MAGNITUDE.add_row("F5", {"Ia": -7.0, "Ib": -4.5, "II": -2.0, "III": 0.7, "IV": 2.1, "V": 3.4, "VI": 4.8})
STELLAR_MAGNITUDE.add_row("G0", {"Ia": -7.3, "Ib": -4.7, "II": -2.1, "III": 0.52, "IV": 2.74, "V": 4.57, "VI": 5.97})
STELLAR_MAGNITUDE.add_row("G5", {"Ia": -7.6, "Ib": -5.0, "II": -2.4, "III": 0.08, "IV": 3.04, "V": 5.2, "VI": 6.6})
STELLAR_MAGNITUDE.add_row("K0", {"Ia": -7.7, "Ib": -5.4, "II": -2.6, "III": -0.17, "IV": 3.1, "V": 5.7, "VI": 7.1})
STELLAR_MAGNITUDE.add_row("K5", {"Ia": -7.8, "Ib": -6.0, "II": -3.7, "III": -1.5, "V": 7.4, "VI": 8.8})
STELLAR_MAGNITUDE.add_row("M0", {"Ia": -7.9, "Ib": -6.9, "II": -4.4, "III": -1.9, "V": 8.25, "VI": 9.65})
STELLAR_MAGNITUDE.add_row("M5", {"Ia": -8.0, "Ib": -7.6, "II": -5.65, "III": -3.6, "V": 10.2, "VI": 11.6})
STELLAR_MAGNITUDE.add_row("M9", {"Ia": -8.1, "Ib": -7.9, "II": -5.75, "III": -3.8, "V": 13.9, "VI": 15.3})
STELLAR_MAGNITUDE.add_row("D",  {"B": 8.1, "A": 10.5, "F": 13.6, "G": 15.3, "K": 15.6, "M": 15.9})

# Stellar luminosity
STELLAR_LUMINOSITY = Table()
STELLAR_LUMINOSITY.add_row("B0", {"Ia": 560000.0, "Ib": 270000.0, "II": 170000.0, "III": 107000.0, "IV": 81000.0,  "V": 56000.0})
STELLAR_LUMINOSITY.add_row("B5", {"Ia": 204000.0, "Ib":  46700.0, "II":  18600.0, "III":  6700.0, "IV":   2000.0,  "V":  1400.0})
STELLAR_LUMINOSITY.add_row("A0", {"Ia": 107000.0, "Ib":  15000.0, "II":   2200.0, "III":   280.0, "IV":    156.0,  "V":    90.0})
STELLAR_LUMINOSITY.add_row("A5", {"Ia":  81000.0, "Ib":  11700.0, "II":    850.0, "III":    90.0, "IV":     37.0,  "V":    16.0})
STELLAR_LUMINOSITY.add_row("F0", {"Ia":  61000.0, "Ib":   7400.0, "II":    600.0, "III":    53.0, "IV":     19.0,  "V":     8.1})
STELLAR_LUMINOSITY.add_row("F5", {"Ia":  51000.0, "Ib":   5100.0, "II":    510.0, "III":    43.0, "IV":     12.0,  "V":     3.5,   "VI": 0.977})
STELLAR_LUMINOSITY.add_row("G0", {"Ia":  67000.0, "Ib":   6100.0, "II":    560.0, "III":    50.0, "IV":      6.5,  "V":     1.21,  "VI": 0.322})
STELLAR_LUMINOSITY.add_row("G5", {"Ia":  89000.0, "Ib":   8100.0, "II":    740.0, "III":    75.0, "IV":      4.9,  "V":     0.67,  "VI": 0.186})
STELLAR_LUMINOSITY.add_row("K0", {"Ia":  97000.0, "Ib":  11700.0, "II":    890.0, "III":    95.0, "IV":      4.67, "V":     0.42,  "VI": 0.117})
STELLAR_LUMINOSITY.add_row("K5", {"Ia": 107000.0, "Ib":  20400.0, "II":   2450.0, "III":   320.0,                  "V":     0.08,  "VI": 0.025})
STELLAR_LUMINOSITY.add_row("M0", {"Ia": 117000.0, "Ib":  46000.0, "II":   4600.0, "III":   470.0,                  "V":     0.04,  "VI": 0.011})
STELLAR_LUMINOSITY.add_row("M5", {"Ia": 129000.0, "Ib":  89000.0, "II":  14900.0, "III":  2280.0,                  "V":     0.007, "VI": 0.002})
STELLAR_LUMINOSITY.add_row("M9", {"Ia": 141000.0, "Ib": 117000.0, "II":  16200.0, "III":  2690.0,                  "V":     0.001, "VI": 0.00006})
STELLAR_LUMINOSITY.add_row("D",  {"B": 0.046, "A": 0.005, "F": 0.0003, "G": 0.00006, "K": 0.00004,  "M": 0.00003})

STELLAR_TEMPERATURE = Table()
STELLAR_TEMPERATURE.add_row("B0", {"Ia": 22000, "Ib": 24000, "II": 25000, "III": 26000, "IV": 27000, "V": 28000})
STELLAR_TEMPERATURE.add_row("B5", {"Ia": 14200, "Ib": 14500, "II": 15100, "III": 15200, "IV": 15400, "V": 15500})
STELLAR_TEMPERATURE.add_row("A0", {"Ia":  9000, "Ib":  9100, "II":  9300, "III":  9500, "IV":  9700, "V":  9900})
STELLAR_TEMPERATURE.add_row("A5", {"Ia":  8000, "Ib":  8100, "II":  8200, "III":  8300, "IV":  8400, "V":  8500})
STELLAR_TEMPERATURE.add_row("F0", {"Ia":  6900, "Ib":  7000, "II":  7100, "III":  7200, "IV":  7300, "V":  7400})
STELLAR_TEMPERATURE.add_row("F5", {"Ia":  6100, "Ib":  6300, "II":  6400, "III":  6500, "IV":  6600, "V":  6700, "VI": 6800})
STELLAR_TEMPERATURE.add_row("G0", {"Ia":  5400, "Ib":  5600, "II":  5700, "III":  5800, "IV":  5900, "V":  6000, "VI": 6100})
STELLAR_TEMPERATURE.add_row("G5", {"Ia":  4700, "Ib":  4850, "II":  5000, "III":  5100, "IV":  5200, "V":  5500, "VI": 5600})
STELLAR_TEMPERATURE.add_row("K0", {"Ia":  4000, "Ib":  4100, "II":  4300, "III":  4500, "IV":  4700, "V":  4900, "VI": 5000})
STELLAR_TEMPERATURE.add_row("K5", {"Ia":  3300, "Ib":  3500, "II":  3650, "III":  3800,              "V":  4100, "VI": 4200})
STELLAR_TEMPERATURE.add_row("M0", {"Ia":  2800, "Ib":  2900, "II":  3100, "III":  3400,              "V":  3500, "VI": 3600})
STELLAR_TEMPERATURE.add_row("M5", {"Ia":  2000, "Ib":  2200, "II":  2400, "III":  2650,              "V":  2800, "VI": 2900})
STELLAR_TEMPERATURE.add_row("M9", {"Ia":  1900, "Ib":  2000, "II":  2100, "III":  2200,              "V":  2300, "VI": 2400})
STELLAR_TEMPERATURE.add_row("D",  {"B": 25000 , "A": 14000, "F": 6600, "G": 4500, "K": 3500, "M": 2700})

STELLAR_RADIUS = Table()
STELLAR_RADIUS.add_row("B0", {"Ia":   52.0, "Ib":   30.0, "II":  22.0, "III":  16.0, "IV": 13.0, "V": 10.0})
STELLAR_RADIUS.add_row("B5", {"Ia":   75.0, "Ib":   35.0, "II":  20.0, "III":  10.0, "IV":  5.3, "V":  4.4})
STELLAR_RADIUS.add_row("A0", {"Ia":  135.0, "Ib":   50.0, "II":  18.0, "III":   6.2, "IV":  4.5, "V":  3.2})
STELLAR_RADIUS.add_row("A5", {"Ia":  149.0, "Ib":   55.0, "II":  14.0, "III":   4.6, "IV":  2.7, "V":  1.8})
STELLAR_RADIUS.add_row("F0", {"Ia":  174.0, "Ib":   59.0, "II":  16.0, "III":   4.7, "IV":  2.7, "V":  1.7})
STELLAR_RADIUS.add_row("F5", {"Ia":  204.0, "Ib":   60.0, "II":  18.0, "III":   5.2, "IV":  2.6, "V":  1.4,   "VI": 1.14})
STELLAR_RADIUS.add_row("G0", {"Ia":  298.0, "Ib":   84.0, "II":  25.0, "III":   7.1, "IV":  2.5, "V":  1.03,  "VI": 1.02})
STELLAR_RADIUS.add_row("G5", {"Ia":  454.0, "Ib":  128.0, "II":  37.0, "III":  11.0, "IV":  2.8, "V":  0.91 , "VI": 0.55})
STELLAR_RADIUS.add_row("K0", {"Ia":  654.0, "Ib":  216.0, "II":  54.0, "III":  16.0, "IV":  3.3, "V":  0.908, "VI": 0.4})
STELLAR_RADIUS.add_row("K5", {"Ia": 1010.0, "Ib":  392.0, "II": 124.0, "III":  42.0,             "V":  0.566, "VI": 0.308})
STELLAR_RADIUS.add_row("M0", {"Ia": 1467.0, "Ib":  857.0, "II": 237.0, "III":  63.0,             "V":  0.549, "VI": 0.256})
STELLAR_RADIUS.add_row("M5", {"Ia": 3020.0, "Ib": 2073.0, "II": 712.0, "III": 228.0,             "V":  0.358, "VI": 0.104})
STELLAR_RADIUS.add_row("M9", {"Ia": 3499.0, "Ib": 2876.0, "II": 931.0, "III": 360.0,             "V":  0.201, "VI": 0.053})
STELLAR_RADIUS.add_row("D",  {"B": 0.018, "A": 0.017, "F": 0.013, "G": 0.012, "K": 0.009, "M": 0.006})

STELLAR_MASS = Table()
STELLAR_MASS.add_row("B0", {"Ia": 60.0, "Ib": 50.0, "II": 30.0, "III": 25.0, "IV": 20.0,  "V": 18.0})
STELLAR_MASS.add_row("B5", {"Ia": 30.0, "Ib": 25.0, "II": 20.0, "III": 15.0, "IV": 10.0,  "V":  6.5})
STELLAR_MASS.add_row("A0", {"Ia": 18.0, "Ib": 16.0, "II": 14.0, "III": 12.0, "IV":  6.0,  "V":  3.2})
STELLAR_MASS.add_row("A5", {"Ia": 15.0, "Ib": 13.0, "II": 11.0, "III":  9.0, "IV":  4.0,  "V":  2.1})
STELLAR_MASS.add_row("F0", {"Ia": 13.0, "Ib": 12.0, "II": 10.0, "III":  8.0, "IV":  2.5,  "V":  1.7})
STELLAR_MASS.add_row("F5", {"Ia": 12.0, "Ib": 10.0, "II":  8.1, "III":  5.0, "IV":  2.0,  "V":  1.3,   "VI": 0.8})
STELLAR_MASS.add_row("G0", {"Ia": 12.0, "Ib": 10.0, "II":  8.1, "III":  2.5, "IV":  1.75, "V":  1.04,  "VI": 0.6})
STELLAR_MASS.add_row("G5", {"Ia": 13.0, "Ib": 12.0, "II": 10.0, "III":  3.2, "IV":  2.0,  "V":  0.94,  "VI": 0.528})
STELLAR_MASS.add_row("K0", {"Ia": 14.0, "Ib": 13.0, "II": 11.0, "III":  4.0, "IV":  2.3,  "V":  0.825, "VI": 0.43})
STELLAR_MASS.add_row("K5", {"Ia": 18.0, "Ib": 16.0, "II": 14.0, "III":  5.0,              "V":  0.57,  "VI": 0.33})
STELLAR_MASS.add_row("M0", {"Ia": 20.0, "Ib": 16.0, "II": 14.0, "III":  6.3,              "V":  0.489, "VI": 0.154})
STELLAR_MASS.add_row("M5", {"Ia": 25.0, "Ib": 20.0, "II": 16.0, "III":  7.4,              "V":  0.331, "VI": 0.104})
STELLAR_MASS.add_row("M9", {"Ia": 30.0, "Ib": 25.0, "II": 18.0, "III":  9.2,              "V":  0.215, "VI": 0.058})
STELLAR_MASS.add_row("D",  {"B": 0.26, "A": 0.36, "F": 0.42, "G": 0.63, "K": 0.83, "M": 1.11})
