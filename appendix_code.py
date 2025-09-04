
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp, correlate
from scipy.stats import norm
import pandas as pd

np.random.seed(42)

fs = 4096.0
duration = 1.0
t = np.linspace(0, duration, int(fs*duration), endpoint=False)

f0, f1 = 30.0, 300.0
signal_amplitude, noise_std = 0.5, 0.5

template = chirp(t, f0=f0, f1=f1, t1=duration, method='linear')
template = template - template.mean()
template = template / np.sqrt(np.sum(template**2))

true_signal = signal_amplitude * template
noise = noise_std * np.random.randn(len(t))
data = true_signal + noise

correlation = correlate(data, template, mode='same')
max_idx = int(np.argmax(correlation))
estimated_time = t[max_idx]
snr = correlation[max_idx] / np.std(correlation)

residual = data - true_signal
mu_hat, sigma_hat = float(np.mean(residual)), float(np.std(residual))

# Save figures as in the main script (omitted here for brevity)
