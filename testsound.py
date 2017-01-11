# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 11:42:28 2016

@author: DucMinh
"""

"""
Show DSP in real-time
"""
import sounddevice as sd
#from scipy.io.wavfile import read
import numpy as np
from numpy.fft import fft
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def DSP(data, sample_rate):
    N =len(data)
    freq = np.arange(N)*float(sample_rate)/N
    dsp = np.abs(fft(data)**2/(N*sample_rate))
    return freq[:N//2], 2*dsp[:N//2]


#rate,data=read('C:\Users\DucMinh\Google Drive\LuMi_Document\Signal et Bruit info\data\\2016-03-02-22_07_11.wav')
fs=44100
buff=0.1

def animate(frameno):
    duration = buff
    mywave= sd.rec(int(duration*fs), samplerate=fs, channels=2)
    sd.wait()
    freq1, dsp1= DSP(mywave[:,0],fs)
    sub1.clear()
    sub1.set_ylim(1e-19, 1e-5)
    sub1.loglog(freq1[:], dsp1[:])

fig=plt.figure()
sub1= fig.add_subplot(111)
sub1.set_yscale('log')
sub1.set_ylim(1e-19, 1e-5)
    
ani= animation.FuncAnimation(fig,animate, blit=False, interval=(buff*1000+10))

plt.show()

#scipy.signal periodogram
#mywave= sd.rec(buff*fs, samplerate=fs, channels=2)
#sd.wait()
#freq1, dsp1= DSP(mywave[:,0],fs)
#plt.figure()
#plt.semilogy(freq1,dsp1)