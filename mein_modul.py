def calculate_percent(reached, maxPoints):
      if type(reached) is not int or type(maxPoints) is not int:
            return TypeError
      
      if maxPoints < 6:
            return ValueError
      
      if reached > maxPoints or reached < 0:
            return ValueError
      
      else:
            result: int = reached / maxPoints * 100
      
            return result