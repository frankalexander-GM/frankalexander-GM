# Carpeta PRUEBAS - Aqui estan TODAS las pruebas con assert

Esta es una COPIA VISIBLE de `tests/` para que la encuentres rapido.

Archivos:
- `test_calculadora_clase.py` → 24 tests de la CLASE Calculadora con assert y pytest
- `test_calculator.py` → tests de funciones puras
- `test_app.py` → tests de API Flask con test_client

Ruta en CMD:
```
C:\Users\SENA\Documents\frankalexander-GM\demo-flask-testing\pruebas\
C:\Users\SENA\Documents\frankalexander-GM\demo-flask-testing\tests\
```

Ambas carpetas tienen lo mismo. La oficial es `tests/` (donde corre pytest).

Para correr:
```
pytest -v
pytest pruebas/test_calculadora_clase.py -v
pytest tests/test_calculadora_clase.py -v
```
