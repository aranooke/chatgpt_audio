import pyttsx3
from pydub import AudioSegment

def text_to_speech(text, output_file):
    # Инициализация движка озвучивания
    engine = pyttsx3.init()
    
    # Озвучивание текста
    engine.save_to_file(text, output_file)
    engine.runAndWait()

# Пример использования
text = "Привет, как дела?"
output_file = "output.wav"

text_to_speech(text, output_file)
