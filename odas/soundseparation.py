import odas
import scipy.io.wavefile

def sound_separation(audio_data, fs):
	sources = odas.doa(audio_data, fs)
	loudest_sources = sorted(sources, key=lambda x: x.energy, reverse=True)[:4]
	return loudest_sources
