
class VentureCapitalist:
    all = []
    def __init__(self, name, total_worth):
        self.name, self.total_worth = name, total_worth
        type(self).all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        else:
            self._name = name

    @property
    def total_worth(self):
        return self._total_worth
    
    @total_worth.setter
    def total_worth(self, total_worth):
        if not isinstance(total_worth, float):
            raise TypeError("Total Worth must be a float")
        else:
            self._total_worth = total_worth

    @classmethod
    def tres_commas_club(cls):
        return [vc for vc in cls.all if vc.total_worth > 1_000_000_000]
# from .funding_round import FundingRound