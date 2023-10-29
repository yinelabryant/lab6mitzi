# Importa las bibliotecas necesarias
import secrets  # Para generar contraseñas seguras
import string   # Para obtener caracteres especiales y alfabéticos
from flask import Flask, jsonify, request  # Para crear una API web y devolver respuestas JSON
import re

# Crea la instancia de la aplicación Flask
app = Flask(__name__)

# Función para generar una contraseña aleatoria con una longitud predeterminada de 12 caracteres
def generate_password(length=12):
    # Define el conjunto de caracteres permitidos en la contraseña
    alphabet = string.ascii_letters + string.digits + string.punctuation
    # Genera una contraseña aleatoria seleccionando caracteres del conjunto
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

def VerifyPassword(password):
    score = 0

    if len(password) >= 16:
        score += 2
    elif len(password) >=8:
        score += 1
    else:
        score += 0
    
    if re.search(r'[A-Z]', password):
        score += 2
    
    if re.search(r'[a-z]', password):
        score += 2

    if re.search(r'[0-9]', password):
        score += 2
    
    if re.search(r'[-!@#$%^&*()_+{}:<>?]', password):
        score += 2
    
    return score
    
# Define una ruta para la generación de contraseñas
@app.route('/generate_password', methods=['GET'])
def generate_password_endpoint():
    # Llama a la función generate_password para obtener una contraseña aleatoria
    password = generate_password()
    # Devuelve la contraseña generada como una respuesta JSON
    return jsonify({'password': password})

@app.route('/verify_password', methods=['GET'])
def verify_password_endpoint():
    password = request.args.get("password")
    score = VerifyPassword(password)
    if score >= 8:
        return ({"puntaje": score, "mensaje": "Tu contrasena es excelente!"})
    elif score >= 5:
        return ({"puntaje": score, "mensaje": "Tu contrasena es buena, pero puede mejorar!"})
    else:
        return ({"puntaje": score, "mensaje": "Tu contrasena es mala, deberias cambiarla inmediatamente!"})


# Inicia la aplicación Flask 
if __name__ == '__main__':
    app.run()
