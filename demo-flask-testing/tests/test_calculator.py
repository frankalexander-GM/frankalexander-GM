"""Tests unitarios puros con assert - ideal para aprender"""
import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calculator import sumar, restar, multiplicar, dividir, es_par, factorial, validar_email, clasificar_edad

# ========== TESTS CON ASSERT SIMPLE ==========
def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0
    assert sumar(0, 0) == 0
    assert sumar(2.5, 2.5) == 5.0

def test_restar():
    assert restar(10, 5) == 5
    assert restar(0, 5) == -5
    assert restar(-5, -5) == 0

def test_multiplicar():
    assert multiplicar(3, 4) == 12
    assert multiplicar(-2, 5) == -10
    assert multiplicar(0, 100) == 0

def test_dividir_ok():
    assert dividir(10, 2) == 5
    assert dividir(7, 2) == 3.5
    assert dividir(-10, 2) == -5

def test_dividir_por_cero():
    # Prueba que lanza excepcion
    with pytest.raises(ValueError, match="No se puede dividir por cero"):
        dividir(10, 0)

def test_es_par():
    assert es_par(2) == True
    assert es_par(3) == False
    assert es_par(0) == True
    assert es_par(-4) == True
    # assert con not
    assert not es_par(7)

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(4) == 24

def test_factorial_errores():
    with pytest.raises(ValueError):
        factorial(-1)
    with pytest.raises(TypeError):
        factorial(3.5)
    with pytest.raises(TypeError):
        factorial("5")

def test_validar_email():
    assert validar_email("test@test.com") == True
    assert validar_email("frank@riftzone.online") == True
    assert validar_email("invalido") == False
    assert validar_email("sin@arroba") == False
    assert validar_email("") == False
    assert validar_email(123) == False

def test_clasificar_edad():
    assert clasificar_edad(5) == "niño"
    assert clasificar_edad(12) == "niño"
    assert clasificar_edad(13) == "adolescente"
    assert clasificar_edad(17) == "adolescente"
    assert clasificar_edad(18) == "adulto"
    assert clasificar_edad(30) == "adulto"
    assert clasificar_edad(65) == "adulto mayor"
    assert clasificar_edad(80) == "adulto mayor"

def test_clasificar_edad_negativa():
    with pytest.raises(ValueError, match="Edad no puede ser negativa"):
        clasificar_edad(-5)

# ========== TEST PARAMETRIZADO (MAS PROFESIONAL) ==========
@pytest.mark.parametrize("a,b,esperado", [
    (1, 1, 2),
    (0, 5, 5),
    (-3, 3, 0),
    (100, 200, 300),
])
def test_sumar_parametrizado(a, b, esperado):
    assert sumar(a, b) == esperado

@pytest.mark.parametrize("edad,esperado", [
    (10, "niño"),
    (15, "adolescente"),
    (25, "adulto"),
    (70, "adulto mayor"),
])
def test_clasificar_edad_parametrizado(edad, esperado):
    assert clasificar_edad(edad) == esperado
