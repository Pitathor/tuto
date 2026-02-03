from ipywidgets import *
import numpy as np
import matplotlib.pyplot as plt

Fs = 200e6; # Fréquence d'échantillonnage
B = 1e6;    # Largeur de Bande
T = 5e-5;   # Durée d'impulsion

time = np.linspace(0,T,int(Fs*T));
freq = np.linspace(-Fs/2,Fs/2,int(Fs*T));

fig = plt.figure()
ax = fig.add_subplot(2, 1, 1)
line, = ax.plot(time, np.real(np.exp(1j*np.pi*B/T*time**2)))
plt.xlabel('Temps [s]')
plt.ylabel('Amplitude')
plt.title('Oscillogramme - Signal temporel')

ax2 = fig.add_subplot(2, 1, 2)
line2, = ax2.plot(freq, np.fft.fftshift(np.fft.fft(np.exp(1j*np.pi*B/T*time**2))))
plt.xlabel('Fréquence [Hz]')
plt.ylabel('Magnitude [dB]')
plt.title('Spectre')

plt.tight_layout()

def update(B = 1):
    line.set_ydata(np.real(np.exp(1j*np.pi*(B*1e6)/(T)*time**2)))
    fig.canvas.draw_idle()

    line2.set_ydata(20*np.log10(np.abs(np.fft.fftshift(np.fft.fft(np.exp(1j*np.pi*(B*1e6)/(T)*time**2))))))
    plt.xlim([-1e6, Fs/3])
    plt.ylim([20, 80])
    fig.canvas.draw_idle()
    
interact(update, B = (0.5,50));