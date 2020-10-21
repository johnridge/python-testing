import argparse
import numpy as np
import scipy.constants
import matplotlib.pyplot as plt
from celluloid import Camera

def main(velocity, mass, filename):
    momentum = mass * velocity
    energy = 1 / 2 * mass * velocity ** 2
    waveNumber = momentum / scipy.constants.hbar
    initialWaveNumber = waveNumber
    angularFrequency = energy / scipy.constants.hbar
    phaseVelocity = angularFrequency / waveNumber
    print(initialWaveNumber)
    print(angularFrequency)
    def wave(x, t):
        wave = np.sin(waveNumber * x - angularFrequency * t)
        return wave
    def amplitude():
        pass

    def testWave(x, t):
        value = np.exp(-(x - phaseVelocity * t) ** 2) * (np.cos(waveNumber * x - angularFrequency * t) + 1j * np.sin(waveNumber * x - angularFrequency * t))
        return value

    def dispersiveWave():
        

    xDimension = np.linspace(-10, 10, 1000)
    tDimension = np.linspace(0, 5, 100)
    for t in tDimension:
        for x in xDimension:
            pass
    totalWave = [[testWave(x, t) for x in xDimension] for t in tDimension]
    realWave = [[np.real(n) for n in x] for x in totalWave]
    imaginaryWave = [[np.imag(n) for n in x] for x in totalWave]
    probabilityWave = [[np.abs(n) ** 2 for n in x] for x in totalWave]
    fig, axs = plt.subplots(2)
    camera = Camera(fig)
    for t in range(len(tDimension)):
        labelA = axs[0].plot(xDimension, realWave[t][:], color = 'tab:red', label = 'Re')
        labelB = axs[0].plot(xDimension, imaginaryWave[t][:], color = 'tab:blue', label = 'Im')
        axs[0].set(ylabel = '$\psi(x, t)$')
        axs[0].set(xlabel = 'x')
        axs[0].grid(axis='both', alpha=0.75)
        #axs[0].legend([labelA, labelB], ['$Re($\psi(x, t))$', '$Im($\psi(x, t))$'])
        axs[1].plot(xDimension, probabilityWave[t][:], color = 'tab:green')
        axs[1].set(ylabel = '$|\Psi(x, t)|^2$')
        axs[1].set(xlabel = 'x')
        axs[1].grid(axis='both', alpha=0.75)
        #plt.show()
        camera.snap()
    animation = camera.animate()
    animation.save(f'{filename}.gif', writer = 'imagemagick')

parser = argparse.ArgumentParser()
parser.add_argument('--velocity', '-v', type = float)
parser.add_argument('--mass', '-m', type = float, default = 10 ** -33)
parser.add_argument('--filename', '-f', type = str, default = 'WaveFuncAnim')
args = parser.parse_args()
velocity = args.velocity
mass = args.mass
filename = args.filename
main(velocity, mass, filename)
