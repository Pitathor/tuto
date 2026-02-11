import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import *
from Function_dir import *

Fs = 250e6; # Fréquence d'échantillonnage
B = 100e6;    # Largeur de Bande
T = 5e-5;   # Durée d'impulsion
N = int(Fs*T) # Nombre de points

time = np.linspace(0,T,N);
chirp = chirp_creator(time,B,T);

plt.figure(2)
plt.clf()
plt.specgram(chirp,Fs=Fs,sides='onesided')
cbar = plt.colorbar()
cbar.set_label('Magnitude [dB]')
plt.xlabel('Temps [s]')
plt.ylabel('Fréquence [Hz]')
plt.title(' Spectrogramme - Chirp')