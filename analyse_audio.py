# https://ipython-books.github.io/116-applying-digital-filters-to-speech-sounds/
import os
import sys
import pydub
import tempfile
import numpy as np
import scipy.signal as sg
from scipy.io import wavfile

np.set_printoptions(threshold=100)
AUDIO_FILE = "audios/eUn7suerUXc-347d051.mp3"


def read(file):
    """MP3 to mono WAV to numpy array"""
    audio = pydub.AudioSegment.from_mp3(file)
    audio = audio.set_channels(1)
    with tempfile.TemporaryFile() as tf:
        audio.export(tf, format='wav')
        samplerate, data = wavfile.read(tf)

    return audio.frame_rate, np.float32(data)/2**15  # Normalizing


def write(file, fr, data):
    unnorm_data = np.int16(data * 2**15)
    wavfile.write(file, fr, unnorm_data)

# samples = data_filt.shape[0]
# duration = samples / fr
# print(duration)
# t_data = np.linspace(0, duration, samples)
# print(t_data)
# timeseries = np.dstack((t_data, data_filt))
# print(timeseries)
# print(timeseries[0][0][0])


def get_audio_mask(audio_file_path=AUDIO_FILE):
    fr, data = read(audio_file_path)

    # Butterworth low pass filter with cut-off freq 150Hz
    b, a = sg.butter(4, 200 / (fr / 2), 'low')
    data_filt = sg.filtfilt(b, a, data)
    write(os.path.join("generated", "low_pass.wav"), fr, data_filt)
    return data_filt


# get_audio_mask()
