import csv
import datetime
import argparse
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import scipy.stats as st
import numpy as np

def main(file, country, population):
    csvReader = csv.reader(open(file), delimiter = ',')
    data = [x for x in csvReader]
    dates = [x[0] for x in data[1:]]
    dates = [datetime.datetime.strptime(x,'%Y-%m-%d').date() for x in dates]
    countries = [x for x in data[0][1:]]
    cases = [x[1:] for x in data[1:]]
    cases = [[0 if n == '' else n for n in x] for x in cases]
    for x in cases:
        for n in x:
            if n == '':
                n = 0
    countryIndex = [countries.index(x) for x in country]
    countryCases = [[float(n[x]) for n in cases] for x in countryIndex]
    equivalentCases = [[population * n for n in x] for x in countryCases]
    fig, ax = plt.subplots(1)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b. %d"))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval = 21))
    ax.grid(axis = 'both', alpha = 0.75)
    ax.set(xlabel = 'Date')
    ax.set(ylabel = 'Equivalent Daily New Cases')
    for x in range(len(country)):
        ax.plot(dates, equivalentCases[x], label = f'{country[x]}', marker = 'o')
    ax.legend(loc = 'upper right')
    
parser = argparse.ArgumentParser()
parser.add_argument('--file', '-f')
parser.add_argument('--country', '-c', nargs = '+')
parser.add_argument('--population', '-p', type = float)
args = parser.parse_args()
file = args.file
country = args.country
population = args.population
main(file, country, population)
plt.show()