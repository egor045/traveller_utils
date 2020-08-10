'''angdia.py -- return angular diameter of object given its size and distance'''

from math import atan2, pi


MODES = ["deg", "rad"]

def angdia(diameter: float, distance: float, mode: str):
    ''' Return angular diameter for object of size <diameter> at distance (distance>
    '''
    try:
        assert str(mode) in MODES
    except AssertionError:
        raise ValueError(
            "Invalid mode {}, should be one of {}".format( str(mode), ", ".join(MODES))
        )

    try:
        assert float(diameter) > 0.0
        assert float(distance) > 0.0
        if str(mode) == "deg":
            return round(atan2(float(diameter), float(distance)) * 180.0 / pi, 3)
        else:
            return round(atan2(float(diameter), float(distance)), 3)

    except ValueError:
        raise ValueError("Could not convert distance ({}) or diameter ({}) to float".format(distance, diameter))
    except AssertionError:
        raise ValueError("distance ({}) and diameter ({}) must be positive".format(distance, diameter))
