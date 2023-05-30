import sounddevice as sd
import soundfile as sf
import pydub

def record_audio(duration, output_file):
    # Запись звука
    sample_rate = 44100  # Частота дискретизации
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()

    # Сохранение в формате WAV
    sf.write(output_file, recording, sample_rate)

    # Конвертация в MP3
    sound = pydub.AudioSegment.from_wav(output_file)
    sound.export(output_file, format="mp3")

# Пример использования
record_duration = 5  # Продолжительность записи в секундах
output_filename = "recorded_audio.mp3"  # Имя выходного файла

record_audio(record_duration, output_filename)
