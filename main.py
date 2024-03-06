import sys
from pathlib import Path
import ffmpeg

args = sys.argv
# Get Input from Arguments
input = args[1]

filename = Path(input).stem
print(filename)

stems = ["vocal","hihat","bass",'instruments','kick']

for stem in enumerate(stems):
    stream = ffmpeg.input(input)
    stream = ffmpeg.output(stream, f'{filename}_{stem[1]}.wav', map = f'0:{stem[0]}')
    ffmpeg.run(stream)