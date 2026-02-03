import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import *

Fs = 2.5e3; # Fréquence d'échantillonnage
Fs2 = 1.5e3; # Fréquence d'échantillonnage
B = 1e3;    # Largeur de Bande
T = 5e-1;   # Durée d'impulsion

time = np.linspace(0,T,int(Fs*T));
time2 = np.linspace(0,T,int(Fs2*T));
chirp = np.exp(1j*np.pi*B/T*time**2);
chirp2 = np.exp(1j*np.pi*B/T*time2**2);
spectre = np.fft.fftshift(np.fft.fft(chirp));
spectre2 = np.fft.fftshift(np.fft.fft(chirp2));
freq = np.linspace(-Fs/2,Fs/2,int(Fs*T));
freq2 = np.linspace(-Fs2/2,Fs2/2,int(Fs2*T));

plt.close("all")
plt.subplot(2, 1, 1)
plt.plot(freq,20*np.log10(abs(spectre)))
plt.xlabel('Fréquence [Hz]')
plt.ylabel('Magnitude [dB]')
plt.title('Spectre - B=1kHz, F_s=2.5kHz')
plt.xlim([-Fs/2, Fs/2])
plt.ylim([0, 80])
plt.tight_layout()

plt.subplot(2, 1, 2)
plt.plot(freq2,20*np.log10(abs(spectre2)))
plt.xlabel('Fréquence [Hz]')
plt.ylabel('Magnitude [dB]')
plt.title('Spectre - B=1kHz, F_s=1.5kHz - Sous-échantillonné')
plt.xlim([-Fs2/2, Fs2/2])
plt.ylim([0, 80])
plt.tight_layout()