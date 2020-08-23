'''subsector.py - subsector'''

from traveller_utils.util import Die
from traveller_utils.ct.planet import Planet

D6 = Die(6)


class Subsector():
    ''' Subsector - collection of hexes, possibly containing systems
    '''

    def __init__(self, name: str=""):
        self.hexes = {}
        self.name = str(name)
        for hex_x in range(1, 9):
            for hex_y in range(1, 11):
                hex_id = "{:02d}{:02d}".format(hex_x, hex_y)
                self.hexes[hex_id] = None
    
    def __str__(self):
        doc = ["Name: {}".format(self.name)]
        for hex_id in self.hexes.keys():
            if self.hexes[hex_id] is not None:
                planet = self.hexes[hex_id]
                doc.append(
                    "{} {:25s} {}".format(
                        hex_id,
                        planet.name,
                        str(planet)
                    )
                )
        return "\n".join(doc)

    def generate(self, dm: int=0):
        ''' Generate subsector contents
            - dm: modifier to D6 roll for contents
        '''
        for hex_id in self.hexes.keys():
            roll = D6.roll(1, int(dm))
            if roll >= 4:
                self.hexes[hex_id] = Planet()
