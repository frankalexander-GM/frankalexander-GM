from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de datos en memoria (ideal para pruebas)
usuarios_db = []
next_id = 1

@app.route('/')
def index():
    return jsonify({"mensaje": "Hola Mundo - API Flask para Pruebas", "status": "ok"}), 200

@app.route('/salud')
def salud():
    return jsonify({"status": "healthy"}), 200

@app.route('/api/suma')
def suma():
    """Endpoint para probar con query params: /api/suma?a=5&b=3"""
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        return jsonify({"a": a, "b": b, "resultado": a + b}), 200
    except (ValueError, TypeError):
        return jsonify({"error": "Parametros invalidos, deben ser numeros"}), 400

@app.route('/api/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios_db), 200

@app.route('/api/usuarios', methods=['POST'])
def crear_usuario():
    global next_id
    data = request.get_json()
    
    # Validaciones
    if not data:
        return jsonify({"error": "Se requiere JSON"}), 400
    if not data.get('nombre'):
        return jsonify({"error": "El campo 'nombre' es obligatorio"}), 400
    if not data.get('email') or '@' not in data.get('email'):
        return jsonify({"error": "Email invalido"}), 400
    
    usuario = {
        "id": next_id,
        "nombre": data['nombre'].strip(),
        "email": data['email'].strip(),
        "edad": data.get('edad', 0)
    }
    usuarios_db.append(usuario)
    next_id += 1
    return jsonify(usuario), 201

@app.route('/api/usuarios/<int:user_id>', methods=['GET'])
def obtener_usuario(user_id):
    usuario = next((u for u in usuarios_db if u['id'] == user_id), None)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(usuario), 200

@app.route('/api/usuarios/<int:user_id>', methods=['DELETE'])
def eliminar_usuario(user_id):
    global usuarios_db
    usuario = next((u for u in usuarios_db if u['id'] == user_id), None)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404
    usuarios_db = [u for u in usuarios_db if u['id'] != user_id]
    return jsonify({"mensaje": "Usuario eliminado"}), 200

# Funcion helper para resetear DB en tests
def reset_db():
    global usuarios_db, next_id
    usuarios_db = []
    next_id = 1

if __name__ == '__main__':
    app.run(debug=True, port=5000)
