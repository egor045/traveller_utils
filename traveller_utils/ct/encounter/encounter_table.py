'''encounter_table.py'''

import json
import logging
from collections import OrderedDict
from textwrap import wrap
from traveller_utils.ct.planet import Planet
from .animal import Carnivore
from .animal import Herbivore
from .animal import Omnivore
from .animal import Scavenger
from .event import Event
from .tables import TERRAIN_TYPES_DM

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.ERROR)


class EncounterTableBase(object):
    '''EncounterTable base class'''

    def __init__(self, terrain, upp=None):
        self.terrain = None
        self.rows = OrderedDict()
        self.__size = 0
        self.planet = None

        LOGGER.debug('terrain_type = %s', terrain)
        LOGGER.debug('upp = %s', upp)

        try:
            assert terrain in TERRAIN_TYPES_DM
            self.terrain = terrain
        except AssertionError:
            raise ValueError('Invalid terrain type {}'.format(terrain))
        if upp is not None:
            try:
                self.planet = Planet(upp=upp)
            except TypeError:
                raise ValueError('Invalid UPP {}'.format(upp))

    def generate(self):
        '''Dummy method'''
        pass

    def __str__(self):
        if self.planet is None:
            upp = ''
        else:
            upp = str(self.planet)
        doc = []
        doc.append('{} Terrain {}'.format(self.terrain, upp))
        doc.append('{:3} {:28} {:6} {:5} {:8}  {}'.format(
            'Die', 'Animal Type', 'Weight', 'Hits', 'Armor', 'Wounds & Weapons'))
        for _ in self.rows:
            if isinstance(self.rows[_], Event):
                doc.append(
                    ' {:2d} {}'.format(
                        int(_),
                        '\n    '.join(wrap(str(self.rows[_]), width=84))
                    )
                )
            else:
                LOGGER.debug('quantity = %s', self.rows[_].quantity)
                # ' {:2d} {:2d} {:23} {:5d} kg {:5} {:8} {:3d} {:13} {:8}'
                doc.append(
                    ' {:2d} {:2d} {:23} {:5} kg {:5} {:8} {:3} {:19} {:8}'.\
                        format(
                            int(_),
                            self.rows[_].quantity,
                            self.rows[_].type,
                            self.rows[_].weight,
                            str(self.rows[_].hits),
                            self.rows[_].armor,
                            self.rows[_].wounds,
                            self.rows[_].weapons,
                            self.rows[_].behaviour
                        )
                )
        return '\n'.join(doc)

    def dict(self):
        '''dict() representation'''
        doc = {
            'upp': None,
            'terrain': str(self.terrain),
            'rows': []
        }
        for _ in self.rows:
            doc['rows'].append(
                (_, self.rows[_].dict())
            )
        if self.planet is not None:
            doc['upp'] = str(self.planet)
        return doc

    def json(self):
        '''JSON representation'''
        return json.dumps(self.dict(), sort_keys=True)


class EncounterTable1D(EncounterTableBase):
    '''D6 encounter table'''

    def __init__(self, terrain, upp=None):
        super().__init__(terrain, upp)
        self.__size = 6
        self.generate()

    def generate(self):
        '''
        Add 6 rows
        - Scavenger
        - Herbivore x 3
        - Omnivore
        - Carnivore
        '''
        if self.planet is None:
            upp = None
        else:
            upp = str(self.planet)
        if self.planet.atmosphere == 0:
            self.rows['1'] = Event(self.terrain, upp)
            self.rows['2'] = Event(self.terrain, upp)
            self.rows['3'] = Event(self.terrain, upp)
            self.rows['4'] = Event(self.terrain, upp)
            self.rows['5'] = Event(self.terrain, upp)
            self.rows['6'] = Event(self.terrain, upp)
        else:
            self.rows['1'] = Scavenger(self.terrain, upp)
            self.rows['2'] = Herbivore(self.terrain, upp)
            self.rows['3'] = Herbivore(self.terrain, upp)
            self.rows['4'] = Herbivore(self.terrain, upp)
            self.rows['5'] = Omnivore(self.terrain, upp)
            self.rows['6'] = Carnivore(self.terrain, upp)


class EncounterTable2D(EncounterTableBase):
    '''2D6 encounter table'''

    def __init__(self, terrain, upp=None):
        super().__init__(terrain, upp)
        self.__size = 6
        self.generate()

    def generate(self):
        '''Add 11 rows'''
        if self.planet is None:
            upp = None
        else:
            upp = str(self.planet)
        if self.planet.atmosphere == 0:
            return
        self.rows['2'] = Scavenger(self.terrain, upp)
        self.rows['3'] = Omnivore(self.terrain, upp)
        self.rows['4'] = Scavenger(self.terrain, upp)
        self.rows['5'] = Omnivore(self.terrain, upp)
        self.rows['6'] = Herbivore(self.terrain, upp)
        self.rows['7'] = Herbivore(self.terrain, upp)
        self.rows['8'] = Herbivore(self.terrain, upp)
        self.rows['9'] = Carnivore(self.terrain, upp)
        self.rows['10'] = Event(self.terrain, upp, strict=False)
        self.rows['11'] = Carnivore(self.terrain, upp)
        self.rows['12'] = Carnivore(self.terrain, upp)
