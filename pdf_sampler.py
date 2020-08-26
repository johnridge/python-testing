import numpy as np
import scipy
from scipy import stats as st
import matplotlib.pyplot as plt
from celluloid import Camera
import argparse

def func(mean, deviation, sample_size, sample_step):
    fig = plt.figure()
    camera = Camera(fig)
    sample = []
    plt.title(f'Probability Density \n $n = {sample_size}$, $\mu = {mean}$, $\sigma = {deviation}$')
    while len(sample) < sample_size:
        sample.extend(np.random.normal(loc = mean, scale = deviation, size = sample_step))
        count, bins, ignored = plt.hist(sample, bins = 'auto', density = True, edgecolor = 'k', color = 'tab:blue')
        sample_mean = np.mean(sample)
        sample_deviation = np.std(sample)
        a = plt.plot(bins, 1 / (sample_deviation * np.sqrt(2 * np.pi)) * np.exp( - (bins - sample_mean) ** 2 / (2 * sample_deviation ** 2) ), linewidth=2, color='tab:green')
        def gaussian(x, mean, deviation): # Gaussian function used to compute probabilities for each bin
            return (1 / (deviation * (2 * np.pi) ** 0.5)) * (np.e ** (-0.5 * ((x - mean) / deviation) ** 2))
        expected = [scipy.integrate.quad(gaussian, bins[i], bins[i + 1], args = (mean, deviation)) for i in range(len(bins) - 1)] # Integrates Gaussian function over each bin to compute each bin's probability
        expected = [len(count) * x[0] for x in expected] # Computes expected number of observations in each bin
        chisq, pval = st.chisquare(count, expected, 1) # Computes chi-square statistic and p-value
        chisq = chisq / ((len(bins) - 1) - 2) # Computes reduced chi-square statistic (chi-square per degree of freedom)
        plt.ylabel('Probability Density')
        plt.legend(a, [f'$n_s = {len(sample)}$, $\mu_s = {round(sample_mean, 3)}$, $\sigma_s = {round(sample_deviation, 3)}$, $\chi^2_\\nu = {round(chisq, 3)}$, $p = {round(pval, 3)}$'], loc = 'upper right')
        camera.snap()
    animation = camera.animate()
    animation.save('pdf.gif', writer = 'imagemagick')


parser = argparse.ArgumentParser()
parser.add_argument('mean', type = float)
parser.add_argument('deviation', type = float)
parser.add_argument('sample_size', type = int)
parser.add_argument('sample_step', type = int)
args = parser.parse_args()
mean = args.mean
deviation = args.deviation
sample_size = args.sample_size
sample_step = args.sample_step
func(mean, deviation, sample_size, sample_step)