import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
# import datetime
import random

freq = 44100
duration = 5
lower = 1
upper =1000

recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
# recordName = datetime.datetime.now()

# print(recordName.second)
sd.wait()

write(f" voice-{random.randint(lower,upper)}.wav ", freq, recording)

# wv.write("recording-1.wav", recording, freq, sampwidth=2)


