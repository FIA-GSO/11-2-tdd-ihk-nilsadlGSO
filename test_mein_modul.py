import pytest
from mein_modul import *


testDataPositive = [
      (1,100,1),
      (0,100,0),
      (100,100,100)
      ]

testDataNegativeValue =[
      (-1,100, ValueError),
      (101,100, ValueError),
      (1, 5, ValueError),

]

testDataNegativeType=[
      (1, 'test', TypeError),
      ('test', 100, TypeError) 
]


@pytest.mark.parametrize('reached, maxPoints, expected', testDataPositive)
def test_calculate_percent__postiv_test( reached, maxPoints, expected):

      result = calculate_percent(reached, maxPoints)
            
      assert result == expected


@pytest.mark.parametrize('reached, maxPoints, expected', testDataNegativeValue)
def test_calculate_percent__negative_value_test( reached, maxPoints, expected):
      
      result = calculate_percent(reached, maxPoints)
      
      assert result == expected

@pytest.mark.parametrize('reached, maxPoints, expected', testDataNegativeType)
def test_calculate_percent__negative_type_test( reached, maxPoints, expected):
      
      result = calculate_percent(reached, maxPoints)
      
      assert result == expected