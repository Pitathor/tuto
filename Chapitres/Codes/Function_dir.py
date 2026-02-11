import numpy as np

def chirp_creator(t,B,T):
    """Permet de simuler un chirp avec les paramètres d'entrés suivants :
    - t : le vecteur temps
    - B : la largeur de bande [Hz]
    - T : la durée d'impulsion [s]
    """
    Vec_impulsion = [1 if t[k]>=0 and t[k]<=T else 0 for k in range(len(t))]
    return(np.exp(1j*np.pi*B/T*t**2)*Vec_impulsion)

def Spectrum(s):
    """Permet de calculer le spectre d'un signal s donné.
    """
    return(np.fft.fftshift(np.fft.fft(s)))