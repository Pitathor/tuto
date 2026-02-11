import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import *
from Function_dir import *

Fs = 200e6; # Fréquence d'échantillonnage
B = 1e6;    # Largeur de Bande
T = 5e-5;   # Durée d'impulsion
N = int(Fs*T) # Nombre de points

time = np.linspace(0,T,int(Fs*T));           # Vecteur temps
chirp = chirp_creator(time,B,T);             # Vecteur signal temporel
spectre =Spectrum(chirp);                    # Vecteur spectre
freq = np.linspace(-Fs/2,Fs/2,int(Fs*T));    # Vecteur fréquences

plt.close("all")
plt.subplot(2, 1, 1)
plt.plot(time,np.real(chirp))
plt.xlabel('Temps [s]')
plt.ylabel('Amplitude')
plt.title('Oscillogramme - Signal temporel')
plt.xlim([0, T])
plt.tight_layout()

plt.subplot(2, 1, 2)
plt.plot(freq,20*np.log10(abs(spectre)))
plt.xlabel('Fréquence [Hz]')
plt.ylabel('Magnitude [dB]')
plt.title('Spectre')
plt.xlim([-B, 1.5*B])
plt.ylim([0, 80])
plt.tight_layout()
