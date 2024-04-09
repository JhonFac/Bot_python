import os

import google.generativeai as genai
import PIL.Image
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS

load_dotenv()


# Configura el modelo y la API KEY
GOOGLE_API_KEY = 'AIzaSyCQ-pNzRJ0SaE-zcvDFJZZ2Oj3UX_ClyiA'
genai.configure(api_key=GOOGLE_API_KEY)
modelo = genai.GenerativeModel('gemini-pro-vision')

app = Flask(__name__)
CORS(app, resources={r"/": {"origins": ""}}, supports_credentials=True)  # Configuración CORS para permitir cualquier origen

@app.route('/analizar', methods=['POST'])
def analizar_imagen():
    # Verificar si se ha enviado algún archivo en la solicitud
    if 'imagen' not in request.files:
        print(request.files)
        return jsonify({'mensaje': 'No se ha enviado ninguna imagen'}), 200
    
    imagen = request.files['imagen']
    
    # Comprobar si el archivo tiene un nombre y si es una imagen válida
    if imagen.filename == '' or not imagen.filename.endswith(('.jpg', '.jpeg', '.png')):
        return jsonify({'error': 'Archivo de imagen no válido'}), 400
    
    # Si se ha recibido una imagen, procesarla como lo hacías antes
    img = PIL.Image.open(imagen)
    
    respuesta = modelo.generate_content(['Analiza la imagen y dime el estado de animo de la mascota, respuestas asi: Estado de Animo : ?, Tipo de Raza o nombre real: ? ,  como identificaste el estado de animo, se especifico y explicalo bien:?,   recomendaciones : ? ,  respuestas en español , entregame las respuestas siempre en un JSON ,', img], stream=True)
    respuesta.resolve()  # Esperar a que la generación se complete
    respuesta = respuesta.text.replace('json','').replace('','')    
    return (respuesta)


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
