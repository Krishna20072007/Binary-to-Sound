import numpy as np
from scipy.io.wavfile import write

with open('input.txt', 'r') as file:
    text = file.read()

binary_text = ' '.join(format(ord(char), '08b') for char in text)

sampling_rate = 44100
duration = 0.1
freq_0 = 440
freq_1 = 880
amplitude = 0.5

audio_data = np.array([])

for bit in binary_text:
    if bit == '0':
        tone = amplitude * np.sin(2 * np.pi * freq_0 * np.arange(0, duration, 1/sampling_rate))
    elif bit == '1':
        tone = amplitude * np.sin(2 * np.pi * freq_1 * np.arange(0, duration, 1/sampling_rate))
    audio_data = np.concatenate((audio_data, tone))

write('output.wav', sampling_rate, audio_data.astype(np.float32))
