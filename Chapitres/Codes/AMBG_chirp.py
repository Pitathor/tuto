import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import *
from Function_dir import *

Fs = 200e6; # Fréquence d'échantillonnage
B = 100e6;    # Largeur de Bande
T = 5e-5;   # Durée d'impulsion
N = int(Fs*T); # Nombre de points
Ndop = 1000 ;

time = np.linspace(0,T,int(Fs*T));           # Vecteur temps
chirp = chirp_creator(time,B,T);             # Vecteur signal temporel

doppler = np.linspace(-B, B, Ndop);

Mat_chirpconj = np.zeros([Ndop,2*N]);
for k in range(1,Ndop):
    Mat_chirpconj[k,:] = np.conj(chirp)*np.exp(2j*np.pi*time*doppler[k]);



