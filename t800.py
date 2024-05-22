import speech_recognition as sr
from playsound import playsound
import os
import unicodedata
import random

# Ruta donde se encuentran los archivos de audio (relativa al directorio del script)
current_dir = os.path.dirname(os.path.abspath(__file__))
ruta_archivos = os.path.join(current_dir, 'sounds')

# Verificar la ruta de archivos
print(f"Ruta de archivos: {ruta_archivos}")

# Diccionario de preguntas y respuestas asociadas a archivos de audio
respuestas = {
    "que modelo eres": ["Cyberdine.mp3"],
    "de que estas hecho": ["human_esqueleton.mp3"],
    "quien te envia": ["35years.mp3"],
    "despidete": ["sayonara.mp3"],
    "descansa": ["beback.mp3"],
    "comemela": ["calmdown.mp3"],
    "eres un organismo vivo": ["yes1.mp3", "correct.mp3", "yes2.mp3", "affirmative.mp3"]
}

# Inicializar el reconocedor de voz
recognizer = sr.Recognizer()

# Función para normalizar texto
def normalizar_texto(texto):
    return unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('ascii').lower()

# Función para obtener la pregunta del usuario y reproducir la respuesta
def obtener_respuesta():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Ajustando sensibilidad al ruido de fondo. Por favor, espera un momento...")
        
        while True:
            print("Di tu pregunta ('que modelo eres', 'de que estas hecho', etc.):")
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                
                # Reconocer la pregunta del usuario utilizando Google Speech Recognition
                pregunta = recognizer.recognize_google(audio, language="es-ES")
                print(f"Pregunta reconocida: {pregunta}")

                # Normalizar la pregunta reconocida
                pregunta_normalizada = normalizar_texto(pregunta)
                print(f"Pregunta normalizada: {pregunta_normalizada}")

                # Verificar si la pregunta está en el diccionario de respuestas
                if pregunta_normalizada in respuestas:
                    archivo_respuesta = random.choice(respuestas[pregunta_normalizada])
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

            # Salir del bucle y terminar el script si la pregunta es "descansa" o "despidete"
            if pregunta_normalizada == "descansa" or pregunta_normalizada == "despidete":
                print("Terminando el script.")
                break
            else:
                print("Lo siento, no tengo una respuesta para esa pregunta.")

    except sr.WaitTimeoutError:
        print("No se detectó ninguna frase. Por favor, intenta de nuevo.")
    except sr.UnknownValueError:
        print("No se pudo entender la pregunta. Por favor, intenta de nuevo.")
    except sr.RequestError as e:
        print(f"Error al realizar la solicitud de reconocimiento de voz: {e}")

# Ejecutar la función para obtener la pregunta y reproducir la respuesta
obtener_respuesta()
