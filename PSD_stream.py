# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 14:12:24 2016

@author: DucMinh
"""


import sounddevice as sd
import numpy as np
from numpy.fft import fft
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PyQt4 import QtGui

fs=44100
buff=50

def DSP(donne, sample_rate):
    N =len(donne)
    freq = np.arange(N)*float(sample_rate)/N
    dsp = np.abs(fft(donne)**2/(N*sample_rate))
    return freq[:N//2], 2*dsp[:N//2]


def callback(indata, frames, time, status ):
    global data
    data=indata[:,0]
    
def animate(frameno):

    freq1, dsp1= DSP(data,fs)
    sub1.clear()
    sub1.set_ylim(1e-19, 1e-10)
    sub1.semilogy(freq1[:], dsp1[:])

fig=plt.figure()
sub1= fig.add_subplot(111)
sub1.set_yscale('log')
sub1.set_ylim(1e-19, 1e-12)


stream= sd.InputStream(samplerate=fs,blocksize=int(buff*fs/1000), channels=2, callback=callback)  
ani= animation.FuncAnimation(fig,animate, blit=False, interval=(buff*1000+10))
with stream:
    plt.show()
    
        
        
        
        

