"""Ejemplo con unittest (clase TestCase) + assertEqual, assertTrue, etc."""
import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calculator import sumar, dividir, factorial
from app import app, reset_db

class TestCalculatorUnittest(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)
        self.assertNotEqual(sumar(2, 2), 5)
    
    def test_dividir(self):
        self.assertAlmostEqual(dividir(10, 3), 3.3333, places=3)
        self.assertEqual(dividir(10, 2), 5)
    
    def test_dividir_por_cero_lanza_error(self):
        with self.assertRaises(ValueError):
            dividir(5, 0)
    
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertTrue(factorial(5) > 100)
        self.assertFalse(factorial(3) == 10)

class TestFlaskUnittest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        reset_db()

    def tearDown(self):
        reset_db()

    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertIn('mensaje', resp.get_json())

    def test_crear_y_listar_usuario(self):
        resp = self.client.post('/api/usuarios', json={"nombre": "Unittest", "email": " unit@test.com "})
        # El email con espacios se hace strip en app.py, pero debe tener @
        self.assertEqual(resp.status_code, 201)
        resp2 = self.client.get('/api/usuarios')
        self.assertEqual(len(resp2.get_json()), 1)

if __name__ == '__main__':
    unittest.main()
