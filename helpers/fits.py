import os
from pathlib import Path
from astropy.io import fits
import numpy as np

def get_hdus(path):
    hdus = []
    files = Path(path).glob('./L22*_PH*.fits')
    for file in files:
        hdus += [fits.open(file)]
    if len(hdus) == 0:
        raise FileExistsError(f"No fits data found in the current directory: {os.path.abspath(path)}")
    return hdus

def extend(pulses):
    return np.append(pulses, [pulse + 1 for pulse in pulses])

def merge(key, hdus):
    datas = np.array([])
    for hdu in hdus:
        datas = np.append(datas, hdu[1].data[key])
    return datas

def filter_background(_array, ceil):
    array = np.array(_array)
    offset = np.max(_array)
    while (np.std(array) > ceil):
        max = np.max(array)
        offset = np.mean(array)
        array = [value for value in array if value < max]
    return [value - offset for value in _array]

def spectrum(E, N):
    dN = [(N[i + 1] - N[i]) / (E[i + 1] - E[i] + 0.00000001) for i in range(len(N) - 1)]
    return (dN, E[0:-1])

def get_inter(bins, counts):
    _bins = bins[:]
    _counts = counts[:]
    middle = int(len(_bins) / 2)
    y_max = np.max(_counts[:middle])
    y_min = np.min(_counts[middle:])
    x_max = _bins[np.where(_counts == y_max)[0][0]]
    x_min = _bins[np.where(_counts == y_min)[0][0]]
    return ([x_min, x_max], [y_min, y_max])

def filter_energy(N, E, inter):
    _E = np.array([])
    _N = np.array([])
    for i in range(len(N)):
        if not inter[1] < N[i] < inter[0]:
            _E = np.append(_E, E[i])
            _N = np.append(_N, N[i])
    return (_N, _E)

def get_efficiency(hdus, counts, inter, bg_efficiency):
    def eff(a, b, c):
        return 1

    _counts = counts[:]
    _energy = np.array([])
    energy = merge('ENERGY', hdus)
    time = merge('TIME', hdus)
    phi = merge('PHI', hdus)
    theta = merge('THETA', hdus)

    for i in range(len(_counts)):
        if not inter[1] < counts[i] < inter[0]:
            energy = np.append(energy, energy[i] * bg_efficiency * eff(time[i], phi[i], theta[i]))
            _counts = np.append(_counts, counts[i])
    
    return (_counts, energy)