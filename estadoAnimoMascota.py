import google.generativeai as genai
import PIL.Image
from flask import Flask, request, jsonify


# Configura el modelo y la API KEY
GOOGLE_API_KEY = 'AIzaSyCQ-pNzRJ0SaE-zcvDFJZZ2Oj3UX_ClyiA'
genai.configure(api_key=GOOGLE_API_KEY)
modelo = genai.GenerativeModel('gemini-pro-vision')

app = Flask(__name__)

@app.route('/analizar', methods=['POST'])
def analizar_imagen():
    # Asegúrate de que la imagen se envíe como 'file' en el formulario
    if 'file' not in request.files:
        return jsonify({'error': 'No se ha enviado ninguna imagen'}), 400
    
    imagen = request.files['file']
    
    # Comprueba si el archivo tiene un nombre y si es una imagen válida
    if imagen.filename == '' or not imagen.filename.endswith(('.jpg', '.jpeg', '.png')):
        return jsonify({'error': 'Archivo de imagen no válido'}), 400
    
    # Abre la imagen con PIL
    img = PIL.Image.open(imagen)
    
    # Genera la respuesta del modelo
    respuesta = modelo.generate_content(['Analiza la imagen y dime el estado de animo de la mascota, respuestas asi: Estado de Animo: ?, Tipo de Raza o nombre real: ? ,  como identificaste el estado de animo, se especifico y explicalo bien:?,   recomendaciones : ? ,  respuestas en español , entregame las respuestas siempre en un JSON ,', img], stream=True)
    respuesta.resolve()  # Esperar a que la generación se complete
    respuesta = respuesta.text.replace('```json','').replace('```','')    
    return (respuesta)  

if __name__ == '__main__':
    app.run(debug=True)
