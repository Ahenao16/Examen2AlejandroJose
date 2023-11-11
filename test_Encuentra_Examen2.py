from Encuentra_Examen2 import Encuentra
import pytest

def test_Encuentra():
    assert Encuentra([1,2,3,4],4) == True
    assert Encuentra([1, 2, 3, 5], 4) == True
    assert Encuentra([1, 2, 3, 4,8], 2) == True
