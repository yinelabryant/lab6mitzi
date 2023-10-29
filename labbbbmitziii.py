# Importa las bibliotecas necesarias
import secrets  # Para generar contraseñas seguras
import string   # Para obtener caracteres especiales y alfabéticos
from flask import Flask, jsonify  # Para crear una API web y devolver respuestas JSON

# Crea la instancia de la aplicación Flask
app = Flask(__name__)

# Función para generar una contraseña aleatoria con una longitud predeterminada de 12 caracteres
def generate_password(length=12):
    # Define el conjunto de caracteres permitidos en la contraseña
    alphabet = string.ascii_letters + string.digits + string.punctuation
    # Genera una contraseña aleatoria seleccionando caracteres del conjunto
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

# Define una ruta para la generación de contraseñas
@app.route('/generate_password', methods=['GET'])
def generate_password_endpoint():
    # Llama a la función generate_password para obtener una contraseña aleatoria
    password = generate_password()
    # Devuelve la contraseña generada como una respuesta JSON
    return jsonify({'password': password})

# Define una ruta de prueba
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Inicia la aplicación Flask 
if __name__ == '__main__':
    app.run()
