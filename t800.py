import speech_recognition as sr
from playsound import playsound
import os

# Ruta donde se encuentran los archivos de audio (relativa al directorio del script)
current_dir = os.path.dirname(os.path.abspath(__file__))
ruta_archivos = os.path.join(current_dir, 'T800')

# Diccionario de preguntas y respuestas asociadas a archivos de audio
respuestas = {
    "T800 qué modelo eres": "Cyberdine.mp3",
    "T800 de qué estas hecho": "human_esqueleton.mp3",
    "T800 quién te envia": "35years.mp3",
    "despidete": "sayonara.mp3",
    "descansa": "beback.mp3",
    "cómemela": "calmdown.mp3"
}

# Inicializar el reconocedor de voz
recognizer = sr.Recognizer()

# Función para obtener la pregunta del usuario y reproducir la respuesta
def obtener_respuesta():
    while True:
        with sr.Microphone() as source:
            print("Di tu pregunta ('T800 qué modelo eres', 'T800 de qué estas hecho', etc.):")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            # Reconocer la pregunta del usuario utilizando Google Speech Recognition
            pregunta = recognizer.recognize_google(audio, language="es-ES")
            print(f"Pregunta reconocida: {pregunta}")

            # Verificar si la pregunta está en el diccionario de respuestas
            if "T800" in pregunta:
                if pregunta in respuestas:
                    archivo_respuesta = respuestas[pregunta]
                    ruta_completa = os.path.join(ruta_archivos, archivo_respuesta)
                    print(f"Respuesta: {ruta_completa}")
                    # Verificar si el archivo de audio existe antes de reproducirlo
                    if os.path.exists(ruta_completa):
                        try:
                            playsound(ruta_completa)
                        except UnicodeDecodeError as e:
                            print(f"Error al reproducir el archivo de audio: {e}")
                    else:
                        print(f"El archivo de audio {ruta_completa} no existe.")
                else:
                    print("Lo siento, no tengo una respuesta para esa pregunta.")
            else:
                print("Por favor, asegúrate de incluir 'T800' en tu pregunta.")

        except sr.UnknownValueError:
            print("No se pudo entender la pregunta.")
        except sr.RequestError:
            print("Error al realizar la solicitud de reconocimiento de voz.")

# Ejecutar la función para obtener la pregunta y reproducir la respuesta
obtener_respuesta()
