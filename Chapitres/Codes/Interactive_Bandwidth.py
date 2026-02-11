from ipywidgets import *
import numpy as np
import matplotlib.pyplot as plt
from Function_dir import *

Fs = 200e6; # Fréquence d'échantillonnage
B = 1e6;    # Largeur de Bande
T = 5e-5;   # Durée d'impulsion
N = int(Fs*T) # Nombre de points

time = np.linspace(0,T,N);       # Vecteur temps
freq = np.linspace(-Fs/2,Fs/2,N);# Vecteur fréquence

fig = plt.figure()
ax = fig.add_subplot(3, 1, 1)
line, = ax.plot(time, np.real(chirp_creator(time,B,T)))
plt.xlabel('Temps [s]')
plt.ylabel('Amplitude')
plt.title('Oscillogramme - Signal temporel')

ax2 = fig.add_subplot(3, 1, 2)
line2, = ax2.plot(freq, 20*np.log10(abs(Spectrum(chirp_creator(time,B,T)))))
plt.xlabel('Fréquence [Hz]')
plt.ylabel('Magnitude [dB]')
plt.title('Spectre')
plt.xlim([-1e6, Fs/3])
plt.ylim([20, 80])

ax3 = fig.add_subplot(3, 1, 3)
line3, freqs, bins, im = ax3.specgram(chirp_creator(time,B,T),Fs=Fs,sides='onesided')
# plt.show()
# cbar = plt.colorbar()
# cbar.set_label('Magnitude [dB]')
plt.xlabel('Temps [s]')
plt.ylabel('Fréquence [Hz]')
plt.title(' Spectrogramme - Chirp')

plt.tight_layout()

def update(B = 1):
    line.set_ydata(np.real(chirp_creator(time,B*1e6,T)))
    fig.canvas.draw_idle()

    line2.set_ydata(20*np.log10(np.abs(Spectrum(chirp_creator(time,B*1e6,T)))))
    plt.xlim([-1e6, Fs/3])
    plt.ylim([20, 80])
    fig.canvas.draw_idle()

    line3, freqs, bins, im = ax3.specgram(chirp_creator(time,B*1e6,T),Fs=Fs,sides='onesided')
    # plt.show()
    plt.ylim([0, 50e6])
    fig.canvas.draw_idle()
    
interact(update, B = (0.5,50));