''' Trade classifications'''

VALID_TRADE_CLASSIFICATIONS = [
    "Ag",
    "Na",
    "In",
    "Ni",
    "Ri",
    "Po",
    "Wa",
    "De",
    "As",
    "Ic"
]

class TradeClassification():
    ''' Planetary trade  classification'''

    def __init__(self, tc: str):
        if tc in VALID_TRADE_CLASSIFICATIONS:
            self.__trade_classification = str(tc)
        else:
            raise ValueError(
                "Invalid classification {}".format(
                    str(tc)
                )
            )

    @property
    def trade_classification(self):
        ''' Return own value'''
        return self.__trade_classification

    def __str__(self):
        return self.__trade_classification
