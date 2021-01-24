from matplotlib.pyplot import sci
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy.ndimage.measurements import label
import scipy.signal
import csv
import datetime
import argparse

def riemannSum(series):
    terms = [series[0 + x] for x in range(len(series))]
    return [sum(terms[:x]) for x in range(len(terms))]

def finiteDifference(series):
    return [0] + [series[x] - series[x - 1] for x in range(1, len(series))]


def main(file, isoCode):
    csvReader = csv.reader(open(file), delimiter = ',')
    data = [x for x in csvReader]
    dates = [x[3] for x in data[1:] if x[0] == isoCode]
    dates = [datetime.datetime.strptime(x,'%Y-%m-%d').date() for x in dates]
    totalCases = [float(x[4]) if x[4] != '' else 0.0 for x in data[1:] if x[0] == isoCode]
    totalCasesCurve = scipy.signal.savgol_filter(totalCases, 51, 3)
    newCaseCurve = scipy.signal.savgol_filter(finiteDifference(totalCases), 51, 3)
    caseGrowthCurve = scipy.signal.savgol_filter(finiteDifference(finiteDifference(totalCases)), 51, 3)
    fig, axs = plt.subplots(3, sharex = True)
    axs[0].xaxis.set_major_formatter(mdates.DateFormatter("%b. %d"))
    axs[0].xaxis.set_major_locator(mdates.DayLocator(interval = 21))
    axs[0].plot(dates, totalCases, color = 'tab:blue', label = 'Raw')
    #axs[0].plot(dates, totalCasesCurve, color = 'tab:green', label = 'Filtered')
    #axs[0].set_yscale('log')
    axs[0].set(ylabel = 'Total confirmed cases')
    axs[0].grid(axis = 'both', alpha = 0.75)
    axs[0].legend(loc = 'upper left')
    axs[1].plot(dates, finiteDifference(totalCases), color = 'tab:blue', label = 'Raw')
    axs[1].plot(dates, newCaseCurve, color = 'tab:green', label = 'Filtered')
    #axs[1].set_yscale('log')
    axs[1].set(ylabel = 'New confirmed cases')
    axs[1].grid(axis = 'both', alpha = 0.75)
    axs[1].legend(loc = 'upper left')
    axs[2].plot(dates, caseGrowthCurve, color = 'tab:orange', label = 'Filtered')
    #axs[2].set_yscale('log')
    axs[2].set(xlabel = 'Date')
    axs[2].set(ylabel = 'Growth in new confirmed cases')
    axs[2].grid(axis = 'both', alpha = 0.75)
    axs[2].legend(loc = 'upper left')

parser = argparse.ArgumentParser()
parser.add_argument('--file', '-f')
parser.add_argument('--isoCode', '-i')
parser.add_argument('--smoothing', '-s', type = float)
args = parser.parse_args()
file = args.file
isoCode = args.isoCode
smoothing = args.smoothing
main(file, isoCode)
plt.show()