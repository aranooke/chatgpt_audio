import speech_recognition as sr
from langdetect import detect;
def recognize_speech(audio_file = 'main.wav',lang = 'en-US'):
    # Create a Recognizer instance
    recognizer = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(audio_file) as source:
        # Read the entire audio file
        audio = recognizer.record(source)

    try:
        # Use Google Speech Recognition to recognize the speech
        text = recognizer.recognize_google(audio,language=lang);
        return text
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

def detect_language(text):
    if text != "":
        try:
            languages = ["ru","en","ua"];
            res_langs= ["-RU","-US","-UA"];
            detected_text = detect(text);
            for i,value in enumerate(languages):
                if i in detected_text:
                    detected_text+=value;
            print(detected_text);
            return detected_text;
        except Exception:
            return "Error with detecting language";