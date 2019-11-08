#!/usr/bin/env python
# Preprocessing pipeline for EEG using MNE

# Starting from BIDS-compatible EEG dataset (EEG-fMRI)
# available at : https://osf.io/dvmrb/
# Pernet, C. R., Clayden, J. D., & Deligianni, F. (2019, July 4). BIDS ready data. https://doi.org/10.17605/OSF.IO/DVMRB

# NB: conversion of MNE datasets to BIDS format can be done using MNE-BIDS
# See https://mne.tools/mne-bids/auto_examples/convert_mne_sample.html

# ===== INPUTS =====
InputVHDRfilepath = './Part2_sub-32-35-36-37-38-39/sub-32/eeg/sub-32_task-rest_eeg.vhdr'
LineNoiseFreq = 50
HighFreq = 45.
LowFreq = 1
DownSampFreq = 250
OutputDirPath = '/Users/renaudmarquis/Vbox_shared/EEGinCMP/derivatives/sub-32/eeg'
OutputFIFfilepath = '/Users/renaudmarquis/Vbox_shared/EEGinCMP/derivatives/sub-32/eeg/sub-32_task-rest_eeg.fif'

# ===== PROCESSING =====

# ===== Import packages =====
import os
import numpy as np
import mne
import math

# ===== Load data =====
EEG = mne.io.read_raw_brainvision(InputVHDRfilepath,preload=True)
# print(EEG)
# print(EEG.info)

# ===== Notch filtering =====
# EEG.plot_psd(area_mode='range', tmax=10.0)
EEG.notch_filter(np.arange(LineNoiseFreq, EEG.info['sfreq']/2, LineNoiseFreq), filter_length='auto',
                 phase='zero')

# ===== Bandpass filtering =====
# EEG.plot_psd(area_mode='range', tmax=10.0)
EEG.filter(LowFreq, HighFreq, l_trans_bandwidth='auto', h_trans_bandwidth='auto',
           filter_length='auto', phase='zero')

# ===== Downsampling =====
EEG.resample(DownSampFreq, npad="auto")

## ===== ICA cleaning =====
#n_comp = math.ceil(math.sqrt(len(EEG.times)/30))
#method = 'fastica'  # for comparison with EEGLAB try "extended-infomax" here
#ICA = mne.preprocessing.ICA(n_components=min(EEG.info['nchan'],n_comp), method=method)
#print(ICA)
#ICA.fit(EEG)
#ICA.plot_components() # Need digitization points (channel locations)
## Plot the first component (0):
#ica.plot_properties(raw, picks=0) # Need digitization points (channel locations)

# ===== Saving preprocessed data =====
# Export to format preferred by BIDS (BrainVision) not currently available, save as FIF instead.
os.makedirs(OutputDirPath)
EEG.save(OutputFIFfilepath)


