import odas
import numpy as np

# Load the audio signals from the microphones
x = np.array([load_audio_file("mic1.wav"),
              load_audio_file("mic2.wav"),
              load_audio_file("mic3.wav"),
              load_audio_file("mic4.wav")])

def closest_microphone(x):
	# Set the sampling frequency (in Hz)
	fs = 44100

	# Set the distance between microphones (in meters)
	d = 0.035

	# Estimate the distance of the sound source from each microphone using the GCC algorithm
	z = odas.gcc(x, fs)
	distance_mic1 = z[0] * fs * 0.5 * d
	distance_mic2 = z[1] * fs * 0.5 * d
	distance_mic3 = z[2] * fs * 0.5 * d
	distance_mic4 = z[3] * fs * 0.5 * d
	return min(distance_mic1, distance_mic2, distance_mic3, distance_mic4)

print(closest_microphone(x))

