# https://bugra.github.io/work/notes/2014-03-31/outlier-detection-in-time-series-signals-fft-median-filtering/

import numpy as np
import scipy
import matplotlib.pyplot as plt
import random
COLOR_PALETTE = [    
               "#348ABD",
               "#A60628",
               "#7A68A6",
               "#467821",
               "#CF4457",
               "#188487",
               "#E24A33"
              ]

# --------------------- example 1: Filtering Noise via FFT from Periodic Signals ---------------------
# Signal Parameters
number_of_samples  = 1000
frequency_of_signal  = 5  
sample_time = 0.001
amplitude = 1   
# Noise Parameters
mu = 0
sigma = 1

signal = [amplitude * np.sin((2 * np.pi) * frequency_of_signal * ii * sample_time) for ii in range(number_of_samples)]
s_time = [ii * sample_time for ii in range(number_of_samples)]
noise = [random.gauss(mu, sigma) for _ in range(number_of_samples)]
signal_with_noise = [ii + jj for ii, jj in zip(signal, noise)]

plt.figure(figsize=(12, 6));
plt.plot(signal);
plt.title('Original Signal');

plt.figure(figsize=(12, 6));
plt.plot(signal_with_noise);
plt.title('Signal with Noise');


fft_of_signal_with_noise = np.fft.fft(signal_with_noise)
f = np.fft.fftfreq(len(fft_of_signal_with_noise),sample_time)

def bandpass_filter(x, freq, frequency_of_signal=frequency_of_signal, band = 0.05):
    if (frequency_of_signal - band) < abs(freq) < (frequency_of_signal + band):
        return x
    else:
        return 0
    
F_filtered = np.asanyarray([bandpass_filter(x,freq) for x,freq in zip(fft_of_signal_with_noise, f)]);
filtered_signal = np.fft.ifft(F_filtered);

plt.figure(figsize=(12, 6));
plt.semilogy(f, abs(fft_of_signal_with_noise), 'o', c=COLOR_PALETTE[4]);
plt.title('Frequency response of Signal with noise');

figure = plt.figure(figsize=(16, 16));
plt.subplot(4,1,1);
plt.plot(s_time, signal, COLOR_PALETTE[0]);
plt.ylabel('Original Signal');
 
plt.subplot(4,1,2);
plt.plot(s_time, signal_with_noise, COLOR_PALETTE[1]);
plt.ylabel('Signal with Noise');

plt.subplot(4,1,3);
plt.plot(s_time, filtered_signal, COLOR_PALETTE[2]);
plt.ylabel('Filtered Signal');
plt.ylim([-amplitude, amplitude]);

plt.subplot(4,1,4);
plt.semilogy(f, abs(F_filtered), 'o');
# Frequency response will be symmetric, no need to get the negative component
plt.title('Frequency Spectrum of Filtered Signal')
plt.xlim([0, 50]); 
plt.xlabel('frequency(Hz)');


# --------------------- example 2 ---------------------
a = 1
x = np.arange(1,51,.5)
y = np.sin(-1/x) * np.sin(x)

y_with_outlier = np.copy(y)

for i in np.arange(len(x)/10, len(x), len(x)/10.):
    ii = int(i)
    y_with_outlier[ii]= 4*(random.random()-.5) + y[ii]

plt.figure(figsize=(12, 6));
plt.scatter(x, y, c=COLOR_PALETTE[-1]);
plt.xlim([0, 50]);
plt.title('Original (Smooth) Signal');

plt.figure(figsize=(12, 6));
plt.scatter(x, y_with_outlier, c=COLOR_PALETTE[-1]);
plt.xlim([0, 50]);
plt.title('Signal with Outliers');

# Median Filtering Approach
def get_median_filtered(signal, threshold = 3):
    """
    signal: is numpy array-like
    returns: signal, numpy array 
    """
    difference = np.abs(signal - np.median(signal))
    median_difference = np.median(difference)
    s = 0 if median_difference == 0 else difference / float(median_difference)
    mask = s > threshold
    signal[mask] = np.median(signal)
    return signal

plt.figure(figsize=(12, 6))
window_size = 20
outlier_s = y_with_outlier.tolist()
median_filtered_signal = []

for ii in range(0, y_with_outlier.size, window_size):
    median_filtered_signal += get_median_filtered(np.asanyarray(outlier_s[ii: ii+20])).tolist() 

plt.subplot(2,1,1);
plt.scatter(range(len(median_filtered_signal)), median_filtered_signal, c=COLOR_PALETTE[-1])
# plt.ylim([-1.5, 1.5])
plt.xlim([0, 100])
plt.title('Median Filtered Signal')

plt.subplot(2,1,2);
plt.scatter(range(len(y)), y, c=COLOR_PALETTE[-1])
# plt.ylim([-1, 1])
plt.xlim([0, 100])
plt.title('Original Signal')


# FFT(Fast Fourier Transform) Approach

def detect_outlier_position_by_fft(signal, threshold_freq=.1, frequency_amplitude=.01):
    fft_of_signal = np.fft.fft(signal)
    outlier = np.max(signal) if abs(np.max(signal)) > abs(np.min(signal)) else np.min(signal)
    if np.any(np.abs(fft_of_signal[threshold_freq:]) > frequency_amplitude):
        index_of_outlier = np.where(signal == outlier)
        return index_of_outlier[0]
    else:
        return None

outlier_positions = []
for ii in range(10, y_with_outlier.size, 5):
    outlier_position = detect_outlier_position_by_fft(y_with_outlier[ii-5:ii+5])
    if outlier_position is not None:
        outlier_positions.append(ii + outlier_position[0] - 5)
outlier_positions = list(set(outlier_positions))

plt.figure(figsize=(12, 6));
plt.scatter(range(y_with_outlier.size), y_with_outlier, c=COLOR_PALETTE[0], label='Original Signal');
plt.scatter(outlier_positions, y_with_outlier[np.asanyarray(outlier_positions)], c=COLOR_PALETTE[-1], label='Outliers');
plt.legend();






