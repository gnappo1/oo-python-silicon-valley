
class Startup:
   all = []
   def __init__(self, name, founder, domain):
      self.name, self.founder, self.domain = name, founder, domain
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
   def founder(self):
      return self._founder
   
   @founder.setter
   def founder(self, founder):
      if not isinstance(founder, str):
         raise TypeError("Founder must be a string")
      elif hasattr(self, "founder"):
         raise Exception("Founder cannot be reset!")
      else:
         self._founder = founder
   @property
   def domain(self):
      return self._domain
   
   @domain.setter
   def domain(self, domain):
      if not isinstance(domain, str):
         raise TypeError("domain must be a string")
      elif hasattr(self, "domain"):
         raise Exception("Domain cannot be reset!")
      else:
         self._domain = domain
   
   @classmethod
   def domains(cls):
      return [startup.domain for startup in Startup.all]

   @classmethod
   def find_by_founder(cls, founder):
      # return next(
      #    (
      #       startup
      #       for startup in Startup.all
      #       if startup.founder == founder
      #    )
      #    , None
      # )
      try:
         return [startup for startup in Startup.all if startup.founder == founder][0]
      except Exception as e:
         return None
      # if matches:= [startup for startup in Startup.all if startup.founder == founder]:
      #    return matches[0]
      # else:
      #    return None
      
# from .funding_round import FundingRound