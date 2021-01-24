import csv
import argparse

class State():
    def __init__(self, name, population):
        self.name = name
        self.population = population
        self.populationPercent = 0
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    @property
    def population(self):
        return self.__population
    @population.setter
    def population(self, population):
        self.__population = population
    @property
    def populationPercent(self):
        return self.__populationPercent
    @populationPercent.setter
    def populationPercent(self, populationPercent):
        self.__populationPercent = populationPercent
    def __str__(self):
        return f'State: {self.name}, Population: {self.population}, Relative Population: {self.populationPercent}'

def main(file):
    csvReader = csv.reader(open(file), delimiter = ',')
    data = [x for x in csvReader]
    states = [State(x[0][1:], int(''.join([n for n in x[-1] if n != ',']))) for x in data[9:60] if x[0] != 'District of Columbia']
    states.sort(key = lambda x : x.population)
    totalPopulation = sum([x.population for x in states])
    for x in states:
        x.populationPercent = x.population / totalPopulation * 100
    lower25 = sum([x.populationPercent for x in states[0:26]])
    print(lower25)
    print(sum([x.populationPercent for x in states[-9:]]))

parser = argparse.ArgumentParser()
parser.add_argument('--file', '-f')
args = parser.parse_args()
file = args.file
main(file)