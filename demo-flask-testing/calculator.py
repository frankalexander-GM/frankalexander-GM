"""Modulo de logica pura - ideal para pruebas unitarias con assert"""

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def es_par(n):
    return n % 2 == 0

def factorial(n):
    if not isinstance(n, int):
        raise TypeError(" factorial solo acepta enteros")
    if n < 0:
        raise ValueError("factorial no definido para negativos")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def validar_email(email):
    """Validador simple para probar asserts"""
    if not isinstance(email, str):
        return False
    return '@' in email and '.' in email and len(email) > 5

def clasificar_edad(edad):
    if edad < 0:
        raise ValueError("Edad no puede ser negativa")
    if edad < 13:
        return "niño"
    elif edad < 18:
        return "adolescente"
    elif edad < 65:
        return "adulto"
    else:
        return "adulto mayor"
