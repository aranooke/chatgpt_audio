from pathlib import Path
import soundfile as sf

def convert(file='main.mp3'):
    mp3_file = Path(file).resolve()
    wav_file = Path("file.wav").resolve()
    print(mp3_file)

    # Convert MP3 to WAV
    mp3_audio, sr = sf.read(mp3_file)
    sf.write(wav_file, mp3_audio, sr)

 # Call the function to convert the MP3 file to WAV
def convert_ogg_to_wav(file= 'main.ogg'):
    ogg_file = Path(file).resolve()
    wav_file = Path("main.wav").resolve()
    print(ogg_file)

    # Convert ogg to wav
    ogg_audio, sr = sf.read(ogg_file)
    sf.write(wav_file, ogg_audio, sr)