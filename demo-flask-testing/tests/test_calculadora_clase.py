"""Tests para la CLASE Calculadora con pytest + assert"""
import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calculadora import Calculadora

@pytest.fixture
def calc():
    """Fixture: crea una calculadora limpia para cada test"""
    return Calculadora()

# ========== TESTS BASICOS CON ASSERT ==========
def test_sumar(calc):
    assert calc.sumar(2, 3) == 5
    assert calc.sumar(-1, 1) == 0
    assert calc.sumar(0, 0) == 0
    assert calc.sumar(2.5, 2.5) == 5.0

def test_restar(calc):
    assert calc.restar(10, 5) == 5
    assert calc.restar(0, 5) == -5
    assert calc.restar(-5, -5) == 0

def test_multiplicar(calc):
    assert calc.multiplicar(3, 4) == 12
    assert calc.multiplicar(-2, 5) == -10
    assert calc.multiplicar(0, 100) == 0

def test_dividir(calc):
    assert calc.dividir(10, 2) == 5
    assert calc.dividir(7, 2) == 3.5
    assert calc.dividir(-10, 2) == -5

def test_dividir_por_cero(calc):
    with pytest.raises(ValueError, match="No se puede dividir por cero"):
        calc.dividir(10, 0)
    # tambien con 0.0
    with pytest.raises(ValueError):
        calc.dividir(5, 0)

def test_potencia(calc):
    assert calc.potencia(2, 3) == 8
    assert calc.potencia(5, 0) == 1
    assert calc.potencia(2, -1) == 0.5
    assert calc.potencia(9, 0.5) == 3.0

def test_raiz_cuadrada(calc):
    assert calc.raiz_cuadrada(9) == 3.0
    assert calc.raiz_cuadrada(16) == 4.0
    assert calc.raiz_cuadrada(0) == 0.0
    assert calc.raiz_cuadrada(2) == pytest.approx(1.4142, rel=1e-3)

def test_raiz_negativa_error(calc):
    with pytest.raises(ValueError, match="No se puede calcular raiz"):
        calc.raiz_cuadrada(-9)

def test_porcentaje(calc):
    assert calc.porcentaje(200, 15) == 30
    assert calc.porcentaje(100, 50) == 50
    assert calc.porcentaje(80, 0) == 0

def test_historial(calc):
    calc.sumar(2, 3)
    calc.multiplicar(2, 5)
    historial = calc.obtener_historial()
    assert len(historial) == 2
    assert "2 + 3 = 5" in historial[0]
    assert "2 * 5 = 10" in historial[1]

def test_limpiar_historial(calc):
    calc.sumar(1, 1)
    calc.restar(5, 2)
    assert len(calc.obtener_historial()) == 2
    calc.limpiar_historial()
    assert calc.obtener_historial() == []
    assert len(calc.obtener_historial()) == 0

# ========== TESTS PARAMETRIZADOS ==========
@pytest.mark.parametrize("a,b,esperado", [
    (1, 1, 2),
    (10, 5, 15),
    (-3, 3, 0),
    (100, 200, 300),
    (0, 0, 0),
])
def test_sumar_parametrizado(calc, a, b, esperado):
    assert calc.sumar(a, b) == esperado

@pytest.mark.parametrize("a,b,esperado", [
    (10, 2, 5),
    (9, 3, 3),
    (7, 2, 3.5),
    (-10, 2, -5),
])
def test_dividir_parametrizado(calc, a, b, esperado):
    assert calc.dividir(a, b) == esperado

@pytest.mark.parametrize("base,exp,esperado", [
    (2, 3, 8),
    (5, 2, 25),
    (10, 0, 1),
    (2, 10, 1024),
])
def test_potencia_parametrizado(calc, base, exp, esperado):
    assert calc.potencia(base, exp) == esperado
