import speech_recognition as sr
from playsound import playsound
import os

# Ruta donde se encuentran los archivos de audio
current_dir = os.path.dirname(os.path.abspath(__file__))
sounds = os.path.join(current_dir, 'T800')


# Diccionario de preguntas y respuestas asociadas a archivos de audio
respuestas = {
    "T800 que modelo eres": "Cyberdine.mp3",
    "T800 de que estas hecho": "human_esqueleton.mp3",
    "T800 quien te envia": "35years.mp3",
    "despidete": "sayonara.mp3",
    "descansa": "beback.mp3",
    "comemela": "calmdown.mp3"
}

# Inicializar el reconocedor de voz
recognizer = sr.Recognizer()

# Funcion para obtener la pregunta del usuario y reproducir la respuesta
def obtener_respuesta():
    with sr.Microphone() as source:
        print("Di tu pregunta ('T800 que modelo eres', 'T800 de que estas hecho', etc.):")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Reconocer la pregunta del usuario utilizando Google Speech Recognition
        pregunta = recognizer.recognize_google(audio, language="es-ES")
        print(f"Pregunta: {pregunta}")

        # Verificar si la pregunta esta en el diccionario de respuestas
        if pregunta in respuestas:
            archivo_respuesta = respuestas[pregunta]
            ruta_completa = os.path.join(ruta_archivos, archivo_respuesta)
            print(f"Respuesta: {ruta_completa}")
            # Reproducir el archivo de audio asociado a la pregunta
            playsound(ruta_completa)
        else:
            print("Lo siento, no tengo una respuesta para esa pregunta.")

    except sr.UnknownValueError:
        print("No se pudo entender la pregunta.")
    except sr.RequestError:
        print("Error al realizar la solicitud de reconocimiento de voz.")

# Ejecutar la funcion para obtener la pregunta y reproducir la respuesta
obtener_respuesta()

