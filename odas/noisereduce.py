import odas
import numpy as np

# Audio signal with noise

def noise_reduce(x):
	# Set the sampling frequency (in Hz)
	fs = 44100

	# Perform noise reduction using the FFT algorithm
	y = odas.odas_denoise(x, fs)

	return y
