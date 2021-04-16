from gtts import gTTS
import sys
import os


if len(sys.argv) < 2:
    sys.exit(0)

with open(sys.argv[1]) as f:
    script = f.read()
    script = script.split('.')

snd_dir = os.getcwd() + '\\' + sys.argv[1] + '.sound'

if not os.path.isdir(snd_dir):
    os.mkdir(snd_dir)
    os.chdir(snd_dir)

    n = 0
    for s in script:
        print(s)
        try:
            sound = gTTS(text=s, lang='en', slow=False)
            sound.save(str(n) + '.wav')
            n += 1
        except:
            pass


