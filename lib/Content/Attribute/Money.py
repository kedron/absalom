""" Money.py -
"""

class Money(Attribute):

    @property
    def domestic_gross(self):
        return self._domestic_gross

    @property
    def international_gross(self):
        return self._international_gross

    @property
    def production_cost(self):
        return self._production_cost

    def __init__(self,
                 domestic_gross = None,
                 international_gross = None,
                 production_cost = None,
                ):
        _domestic_gross = domestic_gross
        _international_gross = international_gross
        _production_cost = production_cost
