import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import *
from Function_dir import *

Fs = 2.5e3; # Fréquence d'échantillonnage
Fs2 = 1.5e3; # Fréquence d'échantillonnage
B = 1e3;    # Largeur de Bande
T = 5e-1;   # Durée d'impulsion
N = int(Fs*T) # Nombre de points
N2 = int(Fs2*T) # Nombre de points

# Vecteurs temps
time = np.linspace(0,T,N);
time2 = np.linspace(0,T,N2);

# Vecteurs signaux
chirp = chirp_creator(time,B,T);
chirp2 = chirp_creator(time2,B,T);

# Vecteurs spectres
spectre = Spectrum(chirp);
spectre2 = Spectrum(chirp2);
freq = np.linspace(-Fs/2,Fs/2,N);
freq2 = np.linspace(-Fs2/2,Fs2/2,N2);

plt.close("all")
plt.subplot(2, 1, 1)
plt.plot(freq,20*np.log10(abs(spectre)))
plt.xlabel('Fréquence [Hz]')
plt.ylabel('Magnitude [dB]')
plt.title('Spectre - B=1kHz, $F_s$=2.5kHz')
plt.xlim([-Fs/2, Fs/2])
plt.ylim([0, 80])
plt.tight_layout()

plt.subplot(2, 1, 2)
plt.plot(freq2,20*np.log10(abs(spectre2)))
plt.xlabel('Fréquence [Hz]')
plt.ylabel('Magnitude [dB]')
plt.title('Spectre - B=1kHz, $F_s$=1.5kHz - Sous-échantillonné')
plt.xlim([-Fs2/2, Fs2/2])
plt.ylim([0, 80])
plt.tight_layout()