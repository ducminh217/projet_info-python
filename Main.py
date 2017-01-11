# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 23:03:46 2016

@author: DucMinh
"""

import sounddevice as sd
import numpy as np
from numpy.fft import fft
import matplotlib.pyplot as plt
from PyQt4 import QtGui

fs=44100

class MainWindow(QtGui.QWidget):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.main_layout= QtGui.QVBoxLayout()
        self.sub_layout1= QtGui.QVBoxLayout()
        self.sub_layout2= QtGui.QVBoxLayout()
        self.main_layout.addLayout(self.sub_layout1)
        self.main_layout.addLayout(self.sub_layout2)
        self.label_rec=QtGui.QLabel('Enter duration and press START to start recording',self)
        self.sub_layout1.addWidget(self.label_rec)
        self.label_duration=QtGui.QLabel('Duration (s)', self)
        self.sub_layout1.addWidget(self.label_duration)
        self.text_duration=QtGui.QLineEdit(self)
        self.sub_layout1.addWidget(self.text_duration)
        self.button_rec=QtGui.QPushButton('START',self)
        self.sub_layout1.addWidget(self.button_rec)
        self.button_playback= QtGui.QPushButton('PLAYBACK', self)
        self.sub_layout1.addWidget(self.button_playback)
        
        self.label_dsp=QtGui.QLabel('Calculate PSD')
        self.sub_layout2.addWidget(self.label_dsp)
        self.button_dsp=QtGui.QPushButton('PLOT DSP',self)
        self.sub_layout2.addWidget(self.button_dsp)
        
        self.setLayout(self.main_layout)
        self.setWindowTitle('Record sound and calculate PSD')
        self.show()
        self.numdata=[]
        self.button_rec.clicked.connect(self.record_sound)
        self.button_playback.clicked.connect(self.playback)
        self.button_dsp.clicked.connect(self.plot_dsp)
        
    def record_sound(self):
        self.button_rec.setText('RESTART')
        duration=int(self.text_duration.text())
        self.numdata=sd.rec(duration*fs,samplerate=fs, channels=2,blocking=True)
        
    def playback(self):
        sd.play(self.numdata, samplerate=fs, blocking=True )
        
    def DSP(self):
        data=self.numdata[:,0]
        N =len(data)
        freq = np.arange(N)*float(fs)/N
        dsp = np.abs(fft(data)**2/(N*fs))
        return freq[:N//2], 2*dsp[:N//2]
    
    def plot_dsp(self):
        plt.figure()
        freq1, dsp1= self.DSP()
        plt.loglog(freq1, dsp1)
        plt.xlabel('Frequence (Hz)')
        plt.ylabel('Amplitude')
        
main=MainWindow()

    
        
        
        
        

