import os
import sys
from pydub import AudioSegment
from pydub.playback import play

import time

if len(sys.argv) < 2:
    sys.exit(0)

os.chdir(sys.argv[1])

n = 0
while True:
    file_path = os.getcwd() + '\\' + str(n) + '.wav'
    if os.path.exists(file_path):
        sound = AudioSegment.from_file(file_path)
        t = sound.duration_seconds
        play(sound)
        time.sleep(t*1.2)
        n += 1
    else:
        break

