'''planet.py - base class for planets (usable in CT, MT, MgT, CE)'''

from ehex import ehex
import re

UPP_MATCH = re.compile(r"(.)(.)(.)(.)(.)(.)(.)-(.)")


class Starport():
    ''' Starport'''

    def __init__(self, code: str=""):
        '''
            Valid codes = A B C D E X
        '''
        try:
            assert str(code).upper() in ["A", "B", "C", "D", "E", "X"]
        except AssertionError:
            raise ValueError("Inappropriate value {} for starport".format(code))
        self.__code = str(code).upper()
    
    def __str__(self):
        return self.__code


class BasePlanet():
    ''' Base planet'''

    def __init__(self, upp: str="", name: str=""):
        self.trade_classifications = []
        self.__name = str(name)
        if str(upp) == "":
            self.__starport = ""
            self.__size = ehex()
            self.__atmosphere = ehex()
            self.__hydrographics = ehex()
            self.__population = ehex()
            self.__government = ehex()
            self.__law_level = ehex()
            self.__tech_level = ehex()
        else:
            self.import_upp(str(upp))
    
    def __str__(self):
        return "{}{}{}{}{}{}{}-{}".format(
            str(self.__starport),
            str(self.__size),
            str(self.__atmosphere),
            str(self.__hydrographics),
            str(self.__population),
            str(self.__government),
            str(self.__law_level),
            str(self.__tech_level)
        )

    def import_upp(self, upp: str=""):
        ''' Import UPP'''
        m = UPP_MATCH.match(str(upp))
        if m:
            self.__starport = str(Starport(m.group(1)))
            self.__size = ehex(m.group(2))
            self.__atmosphere = ehex(m.group(3))
            self.__hydrographics = ehex(m.group(4))
            self.__population = ehex(m.group(5))
            self.__government = ehex(m.group(6))
            self.__law_level = ehex(m.group(7))
            self.__tech_level = ehex(m.group(8))
        else:
            raise ValueError("Invalid UPP {}".format(str(upp)))

    @property
    def starport(self):
        return self.__starport
    
    @property
    def size(self):
        return self.__size
    
    @property
    def atmosphere(self):
        return self.__atmosphere

    @property
    def hydrographics(self):
        return self.__hydrographics
    
    @property
    def population(self):
        return self.__population
    
    @property
    def government(self):
        return self.__government
    
    @property
    def law_level(self):
        return self.__law_level
    
    @property
    def tech_level(self):
        return self.__tech_level

    @property
    def name(self):
        return self.__name
