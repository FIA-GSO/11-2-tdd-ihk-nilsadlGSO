def calculate_percent(reached, maxPoints):
      if not isinstance(reached, int) or not isinstance(maxPoints, int) :
            return TypeError
      
      if maxPoints < 6:
            return ValueError
      
      if reached > maxPoints or reached < 0:
            return ValueError
      
      else:
            result: int = reached / maxPoints * 100
      
            return result
      

def calculate_grade(percent):
      if not isinstance(percent, int):
            return TypeError
      
      if percent < 0 or percent > 100:
            return ValueError
      
      if percent in range(0, 30):
            return 'ungenügend'
      if percent in range(30, 50):
            return 'mangelhaft'
      if percent in range(50, 67):
            return 'ausreichend'
      if percent in range(67, 81):
            return 'befriedigend'
      if percent in range(81, 92):
            return 'gut'
      if percent in range(92, 101):
            return 'sehr gut'
