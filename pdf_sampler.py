import numpy as np
import scipy
from scipy import stats as st
import matplotlib.pyplot as plt
from celluloid import Camera
import argparse

def main(mean, deviation, samples, sample_size, filename):
    fig = plt.figure()
    camera = Camera(fig)
    sample = []
    plt.title(f'Probability Density \n $n = {samples}$, $n_i = {sample_size}$, $\mu = {mean}$, $\sigma = {deviation}$')
    for n in range(samples):
        sample.extend(np.random.normal(loc = mean, scale = deviation, size = sample_size))
        count, bins, ignored = plt.hist(sample, bins = 'auto', density = True, linewidth = 1, edgecolor = 'k', color = 'tab:blue')
        sample_mean = np.mean(sample)
        sample_deviation = np.std(sample)
        x_d = np.linspace(plt.xlim()[0], plt.xlim()[1], 1000)
        density = sum(st.norm(x).pdf(x_d) for x in sample)
        plt.fill_between(x_d, density, alpha=0.5)
        plt.plot(sample, np.full_like(sample, -0.1), '|k', markeredgewidth=1)
        a = plt.plot(bins, 1 / (sample_deviation * np.sqrt(2 * np.pi)) * np.exp( - (bins - sample_mean) ** 2 / (2 * sample_deviation ** 2) ), linewidth=1.5, color='tab:green')
        def gaussian(x, mean, deviation):
            return (1 / (deviation * (2 * np.pi) ** 0.5)) * (np.e ** (-0.5 * ((x - mean) / deviation) ** 2))
        expected = [scipy.integrate.quad(gaussian, bins[i], bins[i + 1], args = (mean, deviation)) for i in range(len(bins) - 1)]
        expected = [len(count) * x[0] for x in expected] 
        chisq, pval = st.chisquare(count, expected, 1) 
        chisq = chisq / ((len(bins) - 1) - 2) 
        plt.ylabel('Probability Density')
        plt.grid(axis='both', alpha=0.75, zorder = 0)
        plt.legend(a, [f'$n_s = {len(sample)}$, $\mu_s = {round(sample_mean, 3)}$, $\sigma_s = {round(sample_deviation, 3)}$, $\chi^2_\\nu = {round(chisq, 3)}$, $p = {round(pval, 3)}$'], loc = 'upper right')
        camera.snap()
    animation = camera.animate()
    animation.save(f'{filename}.gif', writer = 'imagemagick')


parser = argparse.ArgumentParser()
parser.add_argument('--mean', '-m', type = float, default = 0)
parser.add_argument('--deviation', '-d', type = float, default = 1)
parser.add_argument('--samples', '-s', type = int, default = 50)
parser.add_argument('--sample_size', '-ss', type = int, default = 100)
parser.add_argument('--filename', '-f', default = 'pdf')
args = parser.parse_args()
mean = args.mean
deviation = args.deviation
samples = args.samples
sample_size = args.sample_size
filename = args.filename
main(mean, deviation, samples, sample_size, filename)