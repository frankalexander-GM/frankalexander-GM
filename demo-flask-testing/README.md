# Demo Flask Testing - Proyecto Pequeño para Pruebas de Software

Proyecto minimalista en **Flask** para practicar **pruebas de software** con `assert`, `pytest` y `unittest`.

## Estructura
```
demo-flask-testing/
├── app.py               # API Flask (endpoints / , /salud, /api/suma, /api/usuarios CRUD)
├── calculator.py        # Lógica pura (sumar, dividir, factorial, etc.)
├── requirements.txt
├── pytest.ini
└── tests/
    ├── test_calculator.py      # Tests unitarios con assert + pytest
    ├── test_app.py             # Tests de integración Flask test_client
    └── test_unittest_style.py  # Ejemplo con unittest.TestCase
```

## Instalación
```bash
pip install -r requirements.txt
```

## Correr la app
```bash
python app.py
# abre http://127.0.0.1:5000
```

## Correr pruebas

### Opción 1: pytest (recomendado)
```bash
pytest -v
# con coverage
pytest --cov=. --cov-report=term-missing
```

### Opción 2: unittest
```bash
python -m unittest discover -s tests -v
# o solo un archivo
python -m unittest tests/test_unittest_style.py
```

### Opción 3: pytest archivo específico
```bash
pytest tests/test_calculator.py -v
pytest tests/test_app.py -v
```

## Qué practicas con asserts?

| Tipo | Ejemplo |
|------|---------|
| `assert ==` | `assert sumar(2,3) == 5` |
| `assert not` | `assert not es_par(3)` |
| `assert raises` | `with pytest.raises(ValueError): dividir(10,0)` |
| `assert status_code` | `assert resp.status_code == 200` |
| `assert in` | `assert 'error' in data` |
| `unittest` | `self.assertEqual()`, `self.assertRaises()` |

## Endpoints para probar
- `GET /` -> mensaje
- `GET /salud` -> healthy
- `GET /api/suma?a=5&b=3` -> {"resultado": 8}
- `GET /api/usuarios` -> lista
- `POST /api/usuarios` -> crear {"nombre", "email", "edad"}
- `GET /api/usuarios/<id>` -> obtener
- `DELETE /api/usuarios/<id>` -> eliminar
# prueba movimiento 
