"""Tests de integracion para Flask usando test_client + assert"""
import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, reset_db

@pytest.fixture
def client():
    """Fixture que crea un cliente de pruebas y resetea la DB"""
    app.config['TESTING'] = True
    reset_db()
    with app.test_client() as client:
        yield client
    reset_db()

def test_index(client):
    resp = client.get('/')
    assert resp.status_code == 200
    data = resp.get_json()
    assert data['status'] == 'ok'
    assert 'mensaje' in data
    assert 'Flask' in data['mensaje']

def test_salud(client):
    resp = client.get('/salud')
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "healthy"}

# ========== TEST /api/suma ==========
def test_suma_ok(client):
    resp = client.get('/api/suma?a=5&b=3')
    assert resp.status_code == 200
    data = resp.get_json()
    assert data['resultado'] == 8
    assert data['a'] == 5.0
    assert data['b'] == 3.0

def test_suma_negativos(client):
    resp = client.get('/api/suma?a=-10&b=5')
    assert resp.status_code == 200
    assert resp.get_json()['resultado'] == -5

def test_suma_sin_params(client):
    resp = client.get('/api/suma')
    assert resp.status_code == 200
    assert resp.get_json()['resultado'] == 0

def test_suma_params_invalidos(client):
    resp = client.get('/api/suma?a=hola&b=3')
    assert resp.status_code == 400
    assert 'error' in resp.get_json()

# ========== TEST /api/usuarios CRUD ==========
def test_listar_usuarios_vacio(client):
    resp = client.get('/api/usuarios')
    assert resp.status_code == 200
    assert resp.get_json() == []

def test_crear_usuario_ok(client):
    nuevo = {"nombre": "Frank", "email": "frank@test.com", "edad": 25}
    resp = client.post('/api/usuarios', json=nuevo)
    assert resp.status_code == 201
    data = resp.get_json()
    assert data['id'] == 1
    assert data['nombre'] == "Frank"
    assert data['email'] == "frank@test.com"
    assert data['edad'] == 25

def test_crear_usuario_sin_nombre(client):
    resp = client.post('/api/usuarios', json={"email": "a@a.com"})
    assert resp.status_code == 400
    assert 'error' in resp.get_json()
    assert 'nombre' in resp.get_json()['error']

def test_crear_usuario_email_invalido(client):
    resp = client.post('/api/usuarios', json={"nombre": "Test", "email": "invalido"})
    assert resp.status_code == 400
    assert 'Email' in resp.get_json()['error'] or 'email' in resp.get_json()['error'].lower()

def test_crear_usuario_sin_json(client):
    resp = client.post('/api/usuarios', data="no json", content_type='text/plain')
    # Flask puede retornar 415 Unsupported Media Type o 400 según versión
    assert resp.status_code in (400, 415)

def test_obtener_usuario_ok(client):
    client.post('/api/usuarios', json={"nombre": "Ana", "email": "ana@test.com"})
    resp = client.get('/api/usuarios/1')
    assert resp.status_code == 200
    assert resp.get_json()['nombre'] == "Ana"

def test_obtener_usuario_no_existe(client):
    resp = client.get('/api/usuarios/999')
    assert resp.status_code == 404
    assert 'error' in resp.get_json()

def test_eliminar_usuario(client):
    client.post('/api/usuarios', json={"nombre": "Borrar", "email": "borrar@test.com"})
    resp = client.delete('/api/usuarios/1')
    assert resp.status_code == 200
    assert resp.get_json()['mensaje'] == "Usuario eliminado"
    # Verificar que ya no existe
    resp2 = client.get('/api/usuarios/1')
    assert resp2.status_code == 404

def test_eliminar_usuario_no_existe(client):
    resp = client.delete('/api/usuarios/999')
    assert resp.status_code == 404

def test_flujo_completo_usuarios(client):
    # Crear 2 usuarios
    client.post('/api/usuarios', json={"nombre": "User1", "email": "u1@test.com"})
    client.post('/api/usuarios', json={"nombre": "User2", "email": "u2@test.com"})
    # Listar
    resp = client.get('/api/usuarios')
    assert resp.status_code == 200
    assert len(resp.get_json()) == 2
    # Obtener segundo
    resp = client.get('/api/usuarios/2')
    assert resp.get_json()['nombre'] == "User2"
