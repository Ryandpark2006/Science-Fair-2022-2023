import odas
import numpy as np

# Load the audio signal with noise
x = np.array(load_audio_file("noisy_signal.wav"))

# Set the sampling frequency (in Hz)
fs = 44100

# Perform noise reduction using the FFT algorithm
y = odas.odas_denoise(x, fs)

# Save the denoised audio signal to a file
save_audio_file(y, "denoised_signal.wav")
