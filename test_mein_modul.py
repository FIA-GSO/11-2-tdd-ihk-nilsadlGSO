import pytest
from mein_modul import *


testDataPercentPositive = [
      (1,100,1),
      (0,6,0),
      (0,100,0),
      (100,100,100)
      ]

@pytest.mark.parametrize('reached, maxPoints, expected', testDataPercentPositive)
def test_calculate_percent__postiv_test( reached, maxPoints, expected):

      result = calculate_percent(reached, maxPoints)
            
      assert result == expected
      
      
testDataPercentNegativeValue =[
      (-1,100, ValueError),
      (101,100, ValueError),
      (1, 5, ValueError),
]

@pytest.mark.parametrize('reached, maxPoints, expected', testDataPercentNegativeValue)
def test_calculate_percent__negative_value_test( reached, maxPoints, expected):
      
      result = calculate_percent(reached, maxPoints)
      
      assert result == expected
      
      
testDataPercentNegativeType=[
      (1, 'test', TypeError),
      ('test', 100, TypeError) 
]

@pytest.mark.parametrize('reached, maxPoints, expected', testDataPercentNegativeType)
def test_calculate_percent__negative_type_test( reached, maxPoints, expected):
      
      result = calculate_percent(reached, maxPoints)
      
      assert result == expected


      
testDataGradePositive = [
      (100, 'sehr gut'),
      (92, 'sehr gut'),
      (91, 'gut'),
      (81, 'gut'),
      (80, 'befriedigend'),
      (67, 'befriedigend'),
      (66, 'ausreichend'),
      (50, 'ausreichend'),
      (49, 'mangelhaft'),
      (30, 'mangelhaft'),
      (29, 'ungenügend'),
      (0, 'ungenügend'),
]

@pytest.mark.parametrize('percent, expected', testDataGradePositive)
def test_calculate_grade__postive_test(percent, expected):
      result = calculate_grade(percent)      
      assert result == expected

testDataGradeNegativeValue = [
      (-1, ValueError),
      (101, ValueError),
]

@pytest.mark.parametrize('percent, expected', testDataGradeNegativeValue)
def test_calculate_grade__negative_value_test(percent, expected):
      result = calculate_grade(percent)      
      assert result == expected

testDataGradeNegativeType = [
      ('test', TypeError)
]

@pytest.mark.parametrize('percent, expected', testDataGradeNegativeType)
def test_calculate_grade__negtaive_type_test(percent, expected):
      result = calculate_grade(percent)      
      assert result == expected