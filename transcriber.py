from pathlib import Path
import speech_recognition as sr

# obtain path to "english.wav" in the same folder as this script
from os import path

# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "test.flac")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

text_file = open("galaxy_explorer_transcribed.txt", "w+")

for path in Path('audio').rglob('*.flac'):
    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(str(path)) as source:
        audio = r.record(source)  # read the entire audio file

    text_file.write(str(path)+":\n")

    # recognize speech using Sphinx
    try:
        recognise_audio = r.recognize_sphinx(audio)
        text_file.write(recognise_audio + "\n\n")
        print("transcribed: " + recognise_audio)
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

text_file.close()
