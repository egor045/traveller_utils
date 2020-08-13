'''planet.py'''

from ehex import ehex

from traveller_utils.planet import BasePlanet
from traveller_utils.util import Die
from traveller_utils.ct.trade_classifications import TradeClassification

D6 = Die(6)

class Planet(BasePlanet):
    ''' CT planet extends BasePlanet'''

    def __init__(self, upp: str="", name: str="", mode: str="1981"):
        super().__init__(upp=upp, name=name)
        try:
            assert str(mode) in ["1977", "1981"]
        except AssertionError:
            raise ValueError("Invalid mode {} for planet".format(mode))
        self.__mode = str(mode)
        if upp == "":
            self.generate()
        self.trade_classification()
    
    def generate(self):
        ''' Generate UPP'''

        # Starport
        r = D6.roll(2)
        if r <= 4:
            starport = "A"
        elif 4 < r <= 6:
            starport = "B"
        elif 6 < r <= 9:
            starport = "C"
        elif 9 < r <= 10:
            starport = "D"
        elif r == 11:
            starport = "E"
        else:
            starport = "X"

        # Size
        size = ehex(D6.roll(2, -2, floor=0))

        # Atmosphere
        if size == 0:
            atmosphere = 0
        else:
            r = D6.roll(dice=2, modifier=int(size) - 7, floor=0, ceiling=12)
            atmosphere = ehex(r)
        
        # Hydrographics
        ''' 1977 version: 
            - size = 0 or 1 => hydro = 0
            - modifier based on size
            1981 version: 
            - size = 0 => hydro = 0
            - modifier based on atmosphere
        '''
        if self.__mode == "1977":
            dm = int(size) - 7
        else:
            dm = int(atmosphere) - 7
        if self.__mode == "1977" and size in [0, 1]:
            hydrographics = 0
        elif self.__mode == "1981" and size == 0:
            hydrographics = 0
        else:
            if atmosphere <= 1 or atmosphere >= 10:
                dm = dm - 4
            r = D6.roll(dice=2, modifier=dm, floor=0, ceiling=10)
            hydrographics = ehex(r)
        
        # Population
        population = ehex(D6.roll(dice=2, modifier=-2, floor=0, ceiling=10))

        # Government
        r = D6.roll(dice=2, modifier=int(population) - 7, floor=0, ceiling=13)
        government = ehex(r)

        # Law level
        r = D6.roll(dice=2, modifier=int(government) - 7, floor=0, ceiling=10)
        law_level = ehex(r)

        # Tech level
        dm = 0
        if starport == "A":
            dm += 6
        if starport == "B":
            dm += 4
        if starport == "C":
            dm += 2
        if starport == "X":
            dm -= 4

        if size in [0, 1]:
            dm += 2
        if 2 <= size <= 4:
            dm += 1
        if atmosphere <= 3 or atmosphere >= 10:
            dm += 1
        if hydrographics == 9:
            dm += 1
        if hydrographics == 10:
            dm += 2
        if 1 <= population <= 5:
            dm += 1
        if population == 9:
            dm += 2
        if population == 10:
            dm += 4
        if government in [0, 5]:
            dm += 1
        if government == "D":
            dm -= 2
        tech_level = ehex(D6.roll(dice=1, modifier=dm, floor=0))

        upp = "{}{}{}{}{}{}{}-{}".format(
            starport,
            size,
            atmosphere,
            hydrographics,
            population,
            government,
            law_level,
            tech_level
        )
        self.import_upp(upp)

    def trade_classification(self):
        ''' Determine trade classifications for planet'''
        # Ag
        if (4 <= self.atmosphere <= 9) and (5 <= self.population <= 7) and (4 <= self.hydrographics <= 8):
            self.trade_classifications.append("Ag")
        # Na
        if self.atmosphere <= 3 and self.hydrographics <= 3 and self.population >= 6:
            self.trade_classifications.append("Na")
        # In
        if self.population >= 9 and self.atmosphere in [0, 1, 2, 4, 7, 9]:
            self.trade_classifications.append("In")
        # Ni
        if self.population <= 6:
            self.trade_classifications.append("Ni")
        # Ri
        if (4 <= self.government <= 9) and (self.atmosphere in [6, 8]) and (6 <= self.population <= 8):
            self.trade_classifications.append("Ri")
        # Po
        if (2 <= self.atmosphere <= 5) and self.hydrographics <= 3:
            self.trade_classifications.append("Po")
        
        '''
        1981 extras:
            - Desert (De)
            - Vacuum (Va)
            - Asteroid (As)
            - Ice-capped (Ic)
        '''
        if self.__mode == "1981":
            if self.hydrographics == 0 and self.size != 0:
                self.trade_classifications.append("De")
            if self.atmosphere == 0 and self.size != 0:
                self.trade_classifications.append("Va")
            if self.size == 0:
                self.trade_classifications.append("As")
            if self.atmosphere <= 1 and self.hydrographics >= 1:
                self.trade_classifications.append("Ic")
