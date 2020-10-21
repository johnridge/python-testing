import argparse
from operator import itemgetter
from math import sin, cos, radians, trunc
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lombscargle, find_peaks
from mcssa import mcssa

def evaluateBooleanArg(argument):
    if argument == True or argument == 'True' or argument == 'true' or argument == 'Yes' or argument == 'yes' or argument == 'Y' or argument == 'y':
        argument = True
    elif argument == False or argument == 'False' or argument == 'false' or argument == 'No' or argument == 'no' or argument == 'N' or argument == 'n':   
        argument = False
    return argument

def main(lightCurveFile, freqInterval, resolution, preCenter, maxPeaks, phase, plot, verbose):
    def openFile(file):
        data = list(open(file).read().splitlines())
        data = [x.split() for x in data]
        data = [[float(n) for n in x] for x in data]
        return data
        
    def phaseLightCurve(lightCurve, period):
        phasedLightCurve = [(x[0]) / period for x in lightCurve]
        phasedLightCurve = [x - trunc(x) + 1 if x < 0 else x - trunc(x) for x in phasedLightCurve]
        phasedLightCurve = [[phasedLightCurve[x], lightCurve[x][1], lightCurve[x][2]] for x in range(len(lightCurve))]
        for x in range(len(phasedLightCurve)):
            phasedLightCurve.append([phasedLightCurve[x][0] + 1, phasedLightCurve[x][1], phasedLightCurve[x][2]])
        phasedLightCurve.sort(key = itemgetter(0))
        return phasedLightCurve
    
    def plotPeriodogram(pgram, freqRange, perRange, peaks):
        fig, axs = plt.subplots(2)
        ax1, ax2 = axs
        ax1.set_title('Lomb-Scargle Periodogram')
        ax1.plot(freqRange, pgram, color = 'tab:blue', label = 'Frequency spectrum')
        ax1.plot(freqRange[peaks], pgram[peaks], 'x', color = 'tab:orange')
        ax1.set(xlabel = 'Frequency ($\mathrm{days}^{-1}$)')
        ax1.set(ylabel = 'Amplitude')
        ax1.grid(axis = 'both', alpha = 0.75)
        ax1.legend()
        ax2.plot(perRange, pgram, color = 'tab:blue', label = 'Period spectrum')
        ax2.plot(perRange[peaks], pgram[peaks], 'x', color = 'tab:orange')
        ax2.set(xlabel = 'Period (days)')
        ax2.set(ylabel = 'Amplitude')
        ax2.grid(axis = 'both', alpha = 0.75)
        ax2.legend()

    def plotPhasedLightCurves(phasedLightCurves, periods):
        fig, axs = plt.subplots(3, sharex = True, sharey = True)
        axs[0].set_title('Phased Light Curves')
        axs[0].invert_yaxis()
        axs[-1].set(xlabel = 'Phase')
        for x in range(len(axs)):
            axs[x].errorbar([n[0] for n in phasedLightCurves[x]], [n[1] for n in phasedLightCurves[x]], yerr = [n[2] for n in phasedLightCurves[x]], fmt='o', label = f'Period: {periods[x]:.6f} days')
            axs[x].set(ylabel = 'Magnitude')
            axs[x].grid(axis = 'both', alpha = 0.75)
            axs[x].legend(loc = 'upper right')

    lightCurve = openFile(lightCurveFile)
    time = [x[0] for x in lightCurve]
    mag = [x[1] for x in lightCurve]
    freqRange = np.linspace(freqInterval[0], freqInterval[1], num = resolution)
    perRange = 1 / freqRange
    pgram = lombscargle(time, mag, freqRange, precenter = preCenter)
    allPeaks, a = find_peaks(pgram)
    peaks = np.sort(pgram[allPeaks])[-maxPeaks:]
    peaks = [np.where(pgram == x) for x in peaks]
    peaks = np.sort(np.array([x[0][0] for x in peaks]))
    ssa = mcssa.SSA(mag)
    print('Top Hits- \nFrequency Period Amplitude')
    for x in peaks:
        print(f'{freqRange[x]:.6f} {perRange[x]:.6f} {pgram[x]:.6f}')
    if phase:
        phasedLightCurves = [phaseLightCurve(lightCurve, perRange[x]) for x in peaks]
    if plot:
        plotPeriodogram(pgram, freqRange, perRange, peaks)
        if phase:
            plotPhasedLightCurves(phasedLightCurves, perRange[peaks])
    
    

    

parser = argparse.ArgumentParser()
parser.add_argument('--lightCurve', '-lc')
parser.add_argument('--freqInterval', '-f', type = float, nargs = '+')
parser.add_argument('--resolution', '-r', type = int, default = 100000)
parser.add_argument('--preCenter', '-c')
parser.add_argument('--maxPeaks', '-m', type = int, default = 1)
parser.add_argument('--phase', '-ph', default = True)
parser.add_argument('--plot', '-p', default = True)
parser.add_argument('--verbose', '-v', default = False)
args = parser.parse_args()
lightCurveFile = args.lightCurve
freqInterval = args.freqInterval
resolution = args.resolution
preCenter = evaluateBooleanArg(args.preCenter)
maxPeaks = args.maxPeaks
phase = evaluateBooleanArg(args.phase)
plot = evaluateBooleanArg(args.plot)
verbose = evaluateBooleanArg(args.verbose)
main(lightCurveFile, freqInterval, resolution, preCenter, maxPeaks, phase, plot, verbose)
plt.show()
