import numpy as np
import scipy
from scipy import stats as st
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from celluloid import Camera
import argparse

def main(mean, deviation, samples, sample_size, seed, filename):
    figs, axs = plt.subplots(2, figsize = [19.2, 10.8])
    camera = Camera(figs)
    sample = []
    if seed != None:
        np.random.seed(seed)
    for n in range(samples):
        sample.extend(np.random.normal(loc = mean, scale = deviation, size = sample_size))
        sample_mean = np.mean(sample)
        sample_deviation = np.std(sample)
        count, bins, ignored = axs[0].hist(sample, bins = 'auto', density = True, linewidth = 1, edgecolor = 'k', color = 'tab:blue', label = f'Expected: $\mu = {mean}$, $\sigma = {deviation}$')
        x_range = np.linspace(bins[0], bins[-1], 2000)
        density = st.gaussian_kde(sample)
        c = axs[1].plot(x_range, density(x_range), color = 'tab:blue')
        def gaussian(x, mean, deviation):
            return (1 / (deviation * (2 * np.pi) ** 0.5)) * (np.e ** (-0.5 * ((x - mean) / deviation) ** 2))
        expected = [scipy.integrate.quad(gaussian, bins[i], bins[i + 1], args = (mean, deviation)) for i in range(len(bins) - 1)]
        expected = [len(count) * x[0] for x in expected] 
        chisq, pval = st.chisquare(count, expected, 1) 
        chisq = chisq / ((len(bins) - 1) - 2) 
        b = axs[0].plot(x_range, 1 / (deviation * np.sqrt(2 * np.pi)) * np.exp( - (x_range - mean) ** 2 / (2 * deviation ** 2)), linewidth=1.5, color='tab:green')
        d = axs[1].plot(x_range, 1 / (deviation * np.sqrt(2 * np.pi)) * np.exp( - (x_range - mean) ** 2 / (2 * deviation ** 2)), linewidth=1.5, color='tab:green')
        #plt.suptitle(f'Probability Density \n $n = {samples}$')
        axs[0].set_title('Normalized Histogram')
        axs[0].set(ylabel = 'Probability Density')
        axs[0].grid(axis='both', alpha=0.75, zorder = 0)
        a = mpatches.Patch(color='tab:blue')
        axs[0].legend([a, b[0]], [f'Observed: $n_s = {len(sample)}$, $\mu_s = {round(sample_mean, 3)}$, $\sigma_s = {round(sample_deviation, 3)}$', f'Expected: $\mu = {mean}$, $\sigma = {deviation}$, $\chi^2_\\nu = {round(chisq, 3)}$, $p = {round(pval, 3)}$'], loc='upper right')
        axs[1].set_title('Kernel Density Estimatation')
        axs[1].set(ylabel = 'Probability Density')
        axs[1].grid(axis='both', alpha=0.75, zorder = 0)
        axs[1].legend([c[0], d[0]], [f'Observed: $n_s = {len(sample)}$, $\mu_s = {round(sample_mean, 3)}$, $\sigma_s = {round(sample_deviation, 3)}$', f'Expected: $\mu = {mean}$, $\sigma = {deviation}$, $\chi^2_\\nu = {round(chisq, 3)}$, $p = {round(pval, 3)}$'], loc = 'upper right')
        figs.tight_layout()
        camera.snap()
    animation = camera.animate()
    animation.save(f'{filename}.gif', writer = 'imagemagick')

parser = argparse.ArgumentParser()
parser.add_argument('--mean', '-m', type = float, default = 0)
parser.add_argument('--deviation', '-d', type = float, default = 1)
parser.add_argument('--samples', '-s', type = int, default = 25)
parser.add_argument('--sample_size', '-ss', type = int, default = 100)
parser.add_argument('--seed', '-sd', type = int, default = None)
parser.add_argument('--filename', '-f', default = 'pdf')
args = parser.parse_args()
mean = args.mean
deviation = args.deviation
samples = args.samples
sample_size = args.sample_size
seed = args.seed
filename = args.filename
main(mean, deviation, samples, sample_size, seed, filename)