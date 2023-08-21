# Import necessary libraries
import numpy as np
from scipy.io.wavfile import write

# Open and read the content of 'input.txt'
with open('input.txt', 'r') as file:
    text = file.read()

# Convert the text into a binary string representation
binary_text = ' '.join(format(ord(char), '08b') for char in text)

# Define audio parameters
sampling_rate = 44100  # Samples per second
duration = 0.1  # Duration of each audio tone in seconds
freq_0 = 440  # Frequency of '0' bit tone in Hertz
freq_1 = 880  # Frequency of '1' bit tone in Hertz
amplitude = 0.5  # Amplitude of the audio tones

# Initialize an empty numpy array to store the audio data
audio_data = np.array([])

# Loop through each bit in the binary representation of the text
for bit in binary_text:
    if bit == '0':
        # Generate a sine wave for '0' bit
        tone = amplitude * np.sin(2 * np.pi * freq_0 * np.arange(0, duration, 1/sampling_rate))
    elif bit == '1':
        # Generate a sine wave for '1' bit
        tone = amplitude * np.sin(2 * np.pi * freq_1 * np.arange(0, duration, 1/sampling_rate))
    
    # Concatenate the generated tone to the audio data
    audio_data = np.concatenate((audio_data, tone))

# Write the audio data to an output WAV file
write('output.wav', sampling_rate, audio_data.astype(np.float32))
