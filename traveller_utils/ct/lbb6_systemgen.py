'''lbb6_systemgen.py'''

import logging
import re
from sortedcontainers import SortedDict
from random import randint, seed
from ehex import ehex

from traveller_utils.ct.planet import Planet
from traveller_utils.util import Die, Table
from traveller_utils.ct.trade_classifications import TradeClassification
from traveller_utils.ct.lbb6_systemgen_tables import (
    PRIMARY_SIZE,
    SYSTEM_NATURE_TABLE,
    PRIMARY_TYPE,
    COMPANION_ORBIT,
    COMPANION_SIZE,
    COMPANION_TYPE,
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
)

logging.basicConfig()
log = logging.getLogger()

D6 = Die(6)

seed()

# Invalid star/size/decimal classification combinations
INVALID_STAR_COMBINATIONS = [
    "K5IV", "M0IV", "M5IV", "M9IV",
    "B0VI", "B5VI", "A0VI", "A5VI", "F0VI"
]

def bode(orbit_no):
    ''' Determine Bode's rule result for orbit orbit_no
        Return result in AU, mkm 
        orbit_no >= 0
    '''
    try:
        assert orbit_no >= 0
    except AssertionError:
        raise ValueError("Invalid value {} for orbit_no".format(orbit_no))
    
    if orbit_no == 0:
        au = 0.2
    elif orbit_no == 1:
        au = 0.4
    else:
        au = round(0.4 + (0.3 * 2 ** (orbit_no - 2)), 1)
    mkm = round(au * 149.6, 1)
    return {"AU": au, "mkm": mkm}

def find_nearest_classification(star: str=""):
    ''' Find nearest tabled stellar classification to star
    '''
    
    # Direct match in ZONES?
    if ZONES.lookup(str(star)) is not None:
        return str(star)

    m = re.match(r"^([BAFGKM])(\d)([IV].*)$", star)
    if m:
        star_type = m.group(1)
        star_classification = int(m.group(2))
        star_size = m.group(3)
    else:
        raise ValueError("Invalid star {}".format(star))

    table_types = "BAFGKM"
    type_index = table_types.find(star_type)

    log.debug("star_type = %s star_classification = %d star_size = %s", star_type, star_classification, star_size)
    # Classification: 0-2 -> 0, 3-7 -> 5, 8-9 -> types++ 0 unless M
    if star_classification in range(1, 3):
        return "{}0{}".format(star_type, star_size)
    if star_classification in range(3, 8):
        return "{}5{}".format(star_type, star_size)
    if star_classification in range(8, 10):
        if star_type == "M":
            return "M9{}".format(star_size)
        else:
            return "{}0{}".format(table_types[type_index + 1], star_size)


class Orbit():
    ''' CT LBB6 Orbit
    '''
    
    def __init__(self, orbit_number, contents=None):
        self.__orbit_number = orbit_number
        details = bode(orbit_number)
        self.__au = details["AU"]
        self.__mkm = details["mkm"]
        self.contents = contents
    
    def __str__(self):
        return(
            "Orbit<orbit={} ({:f} AU {:f} mkm) contents={}>".format(
                self.__orbit_number,
                self.__au,
                self.__mkm,
                self.contents
            )
        )
    
    @property
    def orbit_number(self):
        return self.__orbit_number
    
    @property
    def au(self):
        return self.__au
    
    @property
    def mkm(self):
        return self.__mkm


class Star():
    ''' CT LBB6 star
    '''

    def __init__(self, dm: int=0):
        self.__type = ""
        self.__size = ""
        self.__classification = None
        self.__generate(dm)

    def __generate(self, dm: int=0):
        ''' Generate star
        '''
        self.__type_die_roll = D6.roll(dice=2, modifier=dm, floor=2, ceiling=12)
        self.__size_die_roll = D6.roll(dice=2, modifier=dm, floor=2, ceiling=12)
        self.__type = PRIMARY_TYPE.lookup(self.__type_die_roll)
        self.__size = PRIMARY_SIZE.lookup(self.__size_die_roll)
        if self.__size != "D":
            self.__classification = randint(0, 9)  
        # Invalid combinations
        if self.__size == "IV":
            if self.__type == "M":
                self.__size = "V"
            if self.__type == "K" and self.classification > 5:
                self.__size = "V"
        if self.__size == "VI":
            if self.type in ["B", "A"]:
                self.__size = "V"
            if self.type == "F" and self.classification < 5:
                self.__size = "V"
            
    
    
    @property
    def type_die_roll(self):
        return self.__type_die_roll
    
    @property
    def size_die_roll(self):
        return self.__size_die_roll
    
    @property
    def type(self):
        return self.__type
    
    @property
    def size(self):
        return self.__size
    
    @property
    def classification(self):
        return self.__classification

    def __str__(self):
        if self.size != "D":
            return "{}{:1d}{}".format(self.__type, self.__classification, self.__size)
        else:
            return "D{}".format(self.__type)


class CompanionStar(Star):
    ''' CT LBB6 companion star
    '''

    def __init__(self, type_dm: int=0, size_dm: int=0):
        super().__init__()
        self.orbit = None
        self.__generate(type_dm, size_dm)
    
    def __generate(self, type_dm: int=0, size_dm: int=0):
        ''' Generate star
        '''
        self.__type_die_roll = D6.roll(dice=2, modifier=type_dm, floor=2, ceiling=12)
        self.__size_die_roll = D6.roll(dice=2, modifier=size_dm, floor=2, ceiling=12)
        self.__type = PRIMARY_TYPE.lookup(self.__type_die_roll)
        self.__size = PRIMARY_SIZE.lookup(self.__size_die_roll)
        if self.__size != "D":
            self.__classification = randint(0, 9)
        else:
            self.__classification = None


class System():
    ''' CT LBB6 system
    '''
    def __init__(self, mainworld=None, loglevel=logging.INFO):
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(loglevel)
        self.companions = []
        self.orbits = SortedDict()
        self.system_description = {
                "available_orbits": [],
                "captured_planets": 0,
                "empty_orbits": 0,
                "gas_giants": 0,
                "planetoid_belts": 0,
                "habitable_zone": 0
            }
        try:
            self.log.debug("type(mainworld) = %s", type(mainworld))
            assert isinstance(mainworld, Planet) or (mainworld is None)
        except AssertionError:
            raise ValueError("Invalid mainworld {}".format(str(mainworld)))
        self.mainworld = mainworld
        self.log.info("logging at %s", self.log.getEffectiveLevel())
    
        self.determine_system_nature()
    
    def determine_system_nature(self, dm: int=0):
        ''' Determine:
        
            - Primary star type and size
            - Companion star(s) type and size
            - Companion star(s) orbits
            - Available orbits
            - Unavailable orbits
            - Habitable zone orbit
            - Captured planets
            - Empty orbits
            - Gas giants
            - Planetoid belts
        '''
        system_nature = SYSTEM_NATURE_TABLE.roll()
        self.log.debug("system_nature = %s", system_nature)
        
        self.determine_primary()
        self.determine_available_orbits()
        self.determine_companion_details(system_nature)

    def determine_primary(self):
        self.log.debug("determining primary details")
        primary_star_dm = 0
        if self.mainworld is not None:
            # Mainworld specified
            if self.mainworld.population >= 8 or self.mainworld.atmosphere in range(4, 9):
                primary_star_dm = 4
        self.log.debug("primary_star_dm = %d", primary_star_dm)
        self.primary = Star(primary_star_dm)
        self.primary_table_entry = find_nearest_classification(str(self.primary))
        self.log.info("primary = %s", str(self.primary))
        self.log.debug("primary_table_entry = %s", self.primary_table_entry)

    def determine_available_orbits(self):
        self.log.debug("determining available orbits")
        dms = 0
        if self.primary.size in ["Ia", "Ib", "II"]:
            dms += 8
        if self.primary.size == "III":
            dms += 4
        if self.primary.type == "M":
            dms -= 4
        if self.primary.type == "K":
            dms -= 2
        self.log.debug("availaible orbits DM = %d", dms)
        maximum_orbit = MAX_ORBITS.roll(dms)
        innermost_orbit = max(ZONES.lookup(str(self.primary_table_entry))["inner"], 0)
        self.log.debug("maximum orbit = %d", maximum_orbit)
        self.log.debug("innermost orbit = %d", innermost_orbit)
        for o in range(innermost_orbit, maximum_orbit + 1):
            self.orbits[o] = Orbit(o)
        self.log.debug("orbits = %s", [x for x in self.orbits.keys()])

    def determine_companion_details(self, system_nature):
        if system_nature != "Solo":
            self.log.debug("Adding binary companion")
            self.add_companion()
        if system_nature == "Trinary":
            self.log.debug("Adding trinary companion")
            self.add_companion()
    
    def add_companion(self):
        
        companion = CompanionStar(type_dm=self.primary.type_die_roll, size_dm=self.primary.size_die_roll)
        companion_orbit = COMPANION_ORBIT.roll()
        self.log.debug("companion = %s, companion orbit = %s", str(companion), companion_orbit)
        self.log.debug("primary interior orbit = %d", ZONES.lookup(self.primary_table_entry)["interior"])
        self.companions.append(companion)
        if companion_orbit not in ["Close", "Far"]:
            if int(companion_orbit) < ZONES.lookup(self.primary_table_entry)["interior"]:
                self.log.debug("changing companion_orbit to 'Close'")
                companion_orbit = "Close"

        # Remove orbits in companion "beaten zone"
        if companion_orbit not in ["Close", "Far"]:
            self.log.debug("removing orbits cleared by companion")
            for o in range(int(companion_orbit / 2) + 1, companion_orbit):
                self.log.debug("checking orbit %d", o)
                if o in self.orbits.keys():
                    self.log.debug("removing orbit %d", o)
                    del self.orbits[o]
            for o in range(companion_orbit + 1, companion_orbit + 3):
                self.log.debug("checking orbit %d", o)
                if o in self.orbits.keys():
                    self.log.debug("removing orbit %d", o)
                    del self.orbits[o]
        self.orbits[companion_orbit] = Orbit(companion_orbit)
        self.orbits[companion_orbit].contents = companion




    def place_known_components(self):
        pass
    
    def generate_worlds(self):
        pass

    def determine_satellites(self):
        pass

    def generate_satellites(self):
        pass

    def determine_additional_world_characteristics(self):
        pass

    def designate_mainworld_determine_characteristics(self):
        pass
