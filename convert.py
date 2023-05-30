from pathlib import Path
import soundfile as sf
from pydub import AudioSegment
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
def convert_to_mp3(input_file, output_file):
    # Load the audio file
    audio = AudioSegment.from_file(input_file)

    # Ensure the output file has the .mp3 extension
    if not output_file.endswith('.mp3'):
        output_file += '.mp3'

    # Export the audio to MP3 format
    audio.export(output_file, format='mp3')