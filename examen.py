import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate


frecuencia440 = SinSignal(freq=440, amp=1, offset=0)
frecuencia622 = SinSignal(freq=622, amp=1, offset=0)

wave_440 = frecuencia440.make_wave(duration=0.5, start=0, framerate=44100)
wave_622 = frecuencia622.make_wave(duration=0.5, start=0.5, framerate=44100)

wave_sonido = wave_440 + wave_622

wave_sonido.write("output.wav")
