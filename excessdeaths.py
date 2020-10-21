import csv
import datetime
import argparse
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import scipy.stats as st
import numpy as np

def main(datafile):
    csv_reader = csv.reader(open(datafile), delimiter = ',')
    data = [x for x in csv_reader]
    totalDates = [x[0] for x in data[1:] if x[0]]
    pDates = [x[3] for x in data[1:] if x[4]] 
    totalDates = [datetime.datetime.strptime(x,'%m/%d/%Y').date() for x in totalDates]
    pDates = [datetime.datetime.strptime(x,'%m/%d/%Y').date() for x in pDates]
    totalObserved = [int(x[1]) for x in data[1:] if x[1]] 
    totalExpected = [int(x[2]) for x in data[1:] if x[1]]
    totalExcess = int(sum([totalObserved[x] - totalExpected[x] for x in range(len(totalObserved)) if totalObserved[x] > totalExpected[x]]))
    pObserved = [int(x[4]) for x in data[1:] if x[4]]
    pExpected = [[int(n) for n in x[5:10]] for x in data[1:] if x[4]]
    pUpperQuartile = [max(x) - int(sum(x) / 5) for x in pExpected]
    pLowerQuartile = [int(sum(x) / 5) - min(x) for x in pExpected]
    pExpected = [sum(x) / 5 for x in pExpected]
    pExcess = int(sum([pObserved[x] - pExpected[x] for x in range(len(pObserved)) if pObserved[x] > pExpected[x]]))
    fig, axs = plt.subplots(2, 1)
    axs[0].xaxis.set_major_formatter(mdates.DateFormatter("%b. %d"))
    axs[0].xaxis.set_major_locator(mdates.DayLocator(interval = 14))
    axs[0].plot(totalDates, totalExpected, linestyle='-', marker='o', color = 'tab:blue', label = f'2015-2019 Mean ({sum(totalExpected)} total deaths)')
    axs[0].plot(totalDates, totalObserved, linestyle='-', marker='o', color = 'tab:red', label = f'2020 ({sum(totalObserved)} total deaths)')
    axs[0].plot([], [], ' ', label = f'{totalExcess} excess deaths')
    axs[0].grid(axis = 'both', alpha = 0.75)
    axs[0].set(xlabel = 'Week')
    axs[0].set(ylabel = 'Weekly Deaths')
    axs[0].legend(loc = 'upper right')
    axs[0].set_title('US Weekly Deaths: 2020 vs 2015-2019 Historical Mean')
    axs[1].xaxis.set_major_formatter(mdates.DateFormatter("%b. %d"))
    axs[1].xaxis.set_major_locator(mdates.DayLocator(interval = 14))
    axs[1].errorbar(pDates, pExpected, yerr = np.array([pUpperQuartile, pLowerQuartile]), capsize = 2.5, linestyle='-', marker='o', color = 'tab:blue', label = f'2015-2019 Mean ({int(sum(pExpected))} total deaths)')
    axs[1].plot(pDates, pObserved, linestyle='-', marker='o', color = 'tab:red', label = f'2020 ({int(sum(pObserved))} total deaths)')
    axs[1].plot([], [], ' ', label = f'{pExcess} excess deaths')
    axs[1].grid(axis = 'both', alpha = 0.75)
    axs[1].set(xlabel = 'Week')
    axs[1].set(ylabel = 'Weekly Deaths')
    handles, labels = axs[1].get_legend_handles_labels()
    axs[1].legend([handles[2], handles[0], handles[1]], [labels[2], labels[0], labels[1]], loc = 'upper right')
    axs[1].set_title('US Weekly Pneumonia Deaths: 2020 vs 2015-2019 Historical Mean')
    #plt.tight_layout()

parser = argparse.ArgumentParser()
parser.add_argument('--file', '-f')
args = parser.parse_args()
datafile = args.file
main(datafile)
plt.show()