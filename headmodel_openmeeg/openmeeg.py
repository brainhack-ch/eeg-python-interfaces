#!/usr/bin/env python

"""Compute the 5 types of leadfields supported by OpenMEEG.

- EEG
- MEG
- EIT
- Internal Potential for dipolar source
- Internal Potential for boundary injected current
"""
#https://github.com/openmeeg/openmeeg_sample_data/blob/master/compute_leadfields.py
from __future__ import print_function

import openmeeg as om
from os import path as op

print(__doc__)

###############################################################################
# Load data

path = 'D:\\projects\\brainhack\\openmeeg\\openmeeg_sample_data-master\\'

geom_file = path + 'data\\model\\head_model.geom'
cond_file = path + 'data\\model\\head_model.cond'
dipoles_file = path + 'data/model/cortex_dipoles.txt'
squids_file = path + 'data/model/meg_channels_locations.squids'
eeg_electrodes_file = path + 'data/model/eeg_channels_locations.txt'
eit_electrodes_file = path + 'data/model/eit_locations.txt'
ecog_electrodes_file = path + 'data/model/ecog_electrodes_locations.txt'
internal_electrodes_file = path + 'data/model/internal_electrodes_locations.txt'

print(geom_file)

geom = om.Geometry(geom_file, cond_file)

print(geom)

dipoles = om.Matrix(dipoles_file)

eeg_electrodes = om.Sensors(eeg_electrodes_file)

###############################################################################
# create a dir for leadfields and tmp
if not op.exists("tmp"):
    import os
    os.mkdir('tmp')
if not op.exists("leadfields"):
    import os
    os.mkdir('leadfields')

# Compute Leadfields
gauss_order = 3
use_adaptive_integration = True
dipole_in_cortex = True

if op.exists("tmp/hmi.mat"):
    hminv = om.SymMatrix("tmp/hmi.mat")
    print("HM inverse loaded from ", "tmp/hmi.mat")
else:
    hm = om.HeadMat(geom, gauss_order)
    hm.invert()
    hm.save("tmp/hmi.mat")
    hminv = hm
    # hminv = hm.inverse() # to also test the adjoint method: comment the 3
    # previous lines, and uncomment this line, and the two others containing
    # 'adjoint'

if op.exists("tmp/dsm.mat"):
    dsm = om.Matrix("tmp/dsm.mat")
    print("DSM loaded from ", "tmp/dsm.mat")
else:
    dsm = om.DipSourceMat(geom, dipoles, gauss_order,
                          use_adaptive_integration, "Brain")
    dsm.save("tmp/dsm.mat")

# For EEG
h2em = om.Head2EEGMat(geom, eeg_electrodes)

'''
# For ECoG
h2ecogm = om.Head2ECoGMat(geom, ecog_electrodes, "Cortex")

# For MEG
ds2mm = om.DipSource2MEGMat(dipoles, meg_sensors)
h2mm = om.Head2MEGMat(geom, meg_sensors)

# For EIT
eitsm = om.EITSourceMat(geom, eit_electrodes, gauss_order)
'''
'''
# For Internal Potential
iphm = om.Surf2VolMat(geom, int_electrodes)
ipsm = om.DipSource2InternalPotMat(geom, dipoles, int_electrodes)
'''
eeg_leadfield = om.GainEEG(hminv, dsm, h2em)

# eeg_leadfield_adjoint = om.GainEEGadjoint(geom,dipoles,hm, h2em)

print("hminv          : %d x %d" % (hminv.nlin(), hminv.ncol()))
print("dsm            : %d x %d" % (dsm.nlin(), dsm.ncol()))
print("h2em           : %d x %d" % (h2em.nlin(), h2em.ncol()))
print("h2ecogm        : %d x %d" % (h2ecogm.nlin(), h2ecogm.ncol()))
print("ds2mm          : %d x %d" % (ds2mm.nlin(), ds2mm.ncol()))
print("h2mm           : %d x %d" % (h2mm.nlin(), h2mm.ncol()))
print("eeg_leadfield  : %d x %d" % (eeg_leadfield.nlin(),
                                    eeg_leadfield.ncol()))
print("ecog_leadfield : %d x %d" % (ecog_leadfield.nlin(),
                                    ecog_leadfield.ncol()))
print("meg_leadfield  : %d x %d" % (meg_leadfield.nlin(),
                                    meg_leadfield.ncol()))
print("eit_leadfield  : %d x %d" % (eit_leadfield.nlin(),
                                    eit_leadfield.ncol()))
print("ip_leadfield   : %d x %d" % (ip_leadfield.nlin(),
                                    ip_leadfield.ncol()))
print("eitip_leadfield  : %d x %d" % (eitip_leadfield.nlin(),
                                      eitip_leadfield.ncol()))

eeg_leadfield.save('leadfields/eeg_leadfield.mat')
# eeg_leadfield_adjoint.save('leadfields/eeg_leadfield_adjoint.mat')