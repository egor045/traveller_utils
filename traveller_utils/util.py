'''
Utility classes
- Die
- Table
'''
from __future__ import print_function

from inspect import ismethod
from random import seed, randint
import json


class Die(object):
    '''
    Generic die-roller
    - sides = die type (number of sides)
    '''

    def __init__(self, sides=6):
        self.__sides = sides
        seed()

    def roll(self, dice=1, modifier=0, floor=0, ceiling=9999):
        '''
        Roll dice
        - dice = number of dice
        - modifier = modifier to roll
        - floor = minimum value
        - ceiling = maximum value
        '''
        roll = modifier
        for _ in range(0, dice):
            roll += randint(1, self.__sides)
        roll = max(floor, roll)
        roll = min(roll, ceiling)
        return roll


class Table(object):
    '''
    Lookup table
    '''

    def __init__(self):
        self.rows = []
        self.dice = None
        self.floor = 999999999
        self.ceiling = 0
        self.roller = Die()

    def add_row(self, number_range, value):
        '''
        Add row to table
        - number_range: one of tuple, int, str
        - value: thing to be returned
        '''
        if isinstance(number_range, tuple):
            if len(number_range) == 2:
                index = list(range(number_range[0], number_range[1] + 1))
                self.rows.append((index, value))
            for i in number_range:
                self.floor = min(self.floor, i)
                self.ceiling = max(self.ceiling, i)
        elif isinstance(number_range, int):
            row = ([number_range], value)
            self.floor = min(self.floor, number_range)
            self.ceiling = max(self.ceiling, number_range)
            self.rows.append(row)
        elif isinstance(number_range, str):
            row = ([number_range], value)
            self.rows.append(row)
        else:
            raise ValueError

    def lookup(self, indx):
        '''
        Return value matching indx
        '''
        for row in self.rows:
            if indx in row[0]:
                if ismethod(row[1]):
                    return row[1]()
                else:
                    return row[1]

    def roll(self, modifier=0):
        '''
        Return random row based on "dice" roll
        '''
        if self.dice is not None:
            result = self.lookup(
                self.roller.roll(
                    self.dice, modifier, self.floor, self.ceiling))
            if ismethod(result):
                return result()
            else:
                return result

    def display(self):
        '''
        Display entire table
        '''
        for row in self.rows:
            print(row)
        print(('Dice = ', self.dice))


class MinMax(object):
    '''Min-max class'''

    def __init__(self, v_1=None, v_2=None):
        if v_1 is None and v_2 is None:
            self._min = v_1
            self._max = v_2
        else:
            try:
                self._min = min(v_1, v_2)
                self._max = max(v_1, v_2)
            except TypeError:
                raise TypeError(
                    '{} ({}), {} ({}) different types'.format(
                        v_1, type(v_1),
                        v_2, type
                    )
                )

    def min(self):
        '''Min'''
        return self._min

    def max(self):
        '''Max'''
        return self._max

    def dict(self):
        '''dict representation'''
        return {
            'min': self._min,
            'max': self._max
        }

    def json(self):
        '''JSON representation'''
        return json.dumps(self.dict(), sort_keys=True)

    def __str__(self):
        return '<min = {} max = {}>'.format(self._min, self._max)

    def __repr__(self):
        return str(self)
