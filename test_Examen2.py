from Examen2 import *

obj1 = MiClase(111,224,2,["canción 1", "canción 2", "canción 3","canción 4" ,"canción 5"],[0.7,0.9, 0.2, 0.8, 1])

def test_ObtieneValencia():
    assert obj1.ObtieneValencia(obj1.Valencia) == 3

def test_DivisibleTempo():
    assert obj1.DivisibleTempo(obj1.Tempo) == [1, 2, 4, 7, 8, 14, 16, 28, 32, 56, 112, 224]

def test_ObtieneMasBailable():
    assert obj1.ObtieneMasBailable(obj1.listaBailabilidad) == 1

def test_VerificaListaCanciones():
     assert obj1.VerificaListaCanciones(obj1.listaCanciones) == True
