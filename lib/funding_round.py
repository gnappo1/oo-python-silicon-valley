class FundingRound:
    all = []
    def __init__(self, startup, venture_capitalist, funding_type, investment):
        self.startup, self.venture_capitalist, self.funding_type, self.investment = startup, venture_capitalist, funding_type, investment
        type(self).all.append(self)
    
    @property
    def startup(self):
        return self._startup
    
    @startup.setter
    def startup(self, startup):
        from .startup import Startup
        if not isinstance(startup, Startup):
            raise TypeError("Startup should be an object of the class Startup")
        elif hasattr(self, "startup"):
            raise Exception("Cannot reset startup after birth")
        else:
            self._startup = startup

    @property
    def venture_capitalist(self):
        return self._venture_capitalist
    
    @venture_capitalist.setter
    def venture_capitalist(self, venture_capitalist):
        from .venture_capitalist import VentureCapitalist
        if not isinstance(venture_capitalist, VentureCapitalist):
            raise TypeError("Venture capitalist should be an object of the class VentureCapitalist")
        elif hasattr(self, "venture_capitalist"):
            raise Exception("Cannot reset venture_capitalist after birth")
        else:
            self._venture_capitalist = venture_capitalist

    @property
    def funding_type(self):
        return self._funding_type
    
    @funding_type.setter
    def funding_type(self, funding_type):
        if isinstance(funding_type, str):
            self._funding_type = funding_type
        else:
            raise TypeError("Funding Type should be a string")

    @property
    def investment(self):
        return self._investment
    
    @investment.setter
    def investment(self, investment):
        if isinstance(investment, float) and investment >= 0.0:
            self._investment = investment
        else:
            raise TypeError("Investment should be a float greater or equal to 0")