from pathlib import Path
from pydub import AudioSegment

# find all wav files
for path in Path('audio').rglob('*.wav'):
    # convert file´from wav to flac format
    path_split = str(path).split("/")
    path_folders = "/".join(path_split[:2])
    file_name = path_split[-1].split(".")[0]

    new_path = path_folders + "/" + file_name + ".flac"

    song = AudioSegment.from_wav(path)
    song.export(new_path, format = "flac")
    print("Converted", path)
