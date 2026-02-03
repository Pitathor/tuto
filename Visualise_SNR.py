from ipywidgets import *
import numpy as np 
import matplotlib.pyplot as plt


T = 1e-4;
Fs = 5e6;
time = np.linspace(0,T,int(Fs*T))

np.random.seed(9001)
Snr1 = 0; Snr2 = 20
Ps = np.sum(np.abs(np.sin(2*np.pi*1e4*time)))/len(time)
Pb1 = np.sqrt(Ps/(10**(Snr1/10))); Pb2 = np.sqrt(Ps/(10**(Snr2/10))),
noise = np.random.rand(len(time))

plt.close()
fig = plt.figure(8)
ax = fig.add_subplot(2, 1, 1)
line, = plt.plot(time*1e3,np.sin(2*np.pi*1e4*time)+Pb1*noise)
plt.xlabel('Temps [ms]')
plt.ylabel('Amplitude')
plt.title('Oscillogramme - SNR = 0dB')

ax = fig.add_subplot(2, 1, 2)
line, = plt.plot(time*1e3,np.sin(2*np.pi*1e4*time)+Pb2*noise)
plt.xlabel('Temps [ms]')
plt.ylabel('Amplitude')
plt.title('Oscillogramme - SNR = 20dB')
plt.tight_layout()