import odas
import scipy.io.wavefile

audio_data, fs = odas.read()

sources = odas.doa(audio_data, fs)

loudest_sources = sorted(sources, key=lambda x: x.energy, reverse=True)[:4]

for i, source in enumerate(loudest_sources):
	scipy.io.wavefile.write('source{}.wav'.format(i+1), fs, source.signal)
