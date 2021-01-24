#from Decimal import Decimal
import numpy as np
import matplotlib.pyplot as plt
import argparse
import csv

def str2bool(argument):
    if isinstance(argument, bool):
        pass
    elif argument == 'True' or argument == 'true' or argument == 'Yes' or argument == 'yes' or argument == 'Y' or argument == 'y':
        argument = True
    elif argument == 'False' or argument == 'false' or argument == 'No' or argument == 'no' or argument == 'N' or argument == 'n':   
        argument = False
    return argument

def trueRound(num, dec=0):
    num = str(num)[:str(num).index('.')+dec+2]
    if num[-1]>='5':
        return float(num[:-2-(not dec)]+str(int(num[-2-(not dec)])+1))
    return float(num[:-1])

class Region():
    def __init__(self, name, isState, isCapital, population, houseSeats):
        self.name = name
        self.isState = isState
        if self.isState == 'TRUE':
            self.isState = True
        else:
            self.isState = False
        self.isCapital = isCapital
        if self.isCapital == 'TRUE':
            self.isCapital = True
        else:
            self.isCapital = False
        self.population = population
        self.percentPopulation = None
        self.houseSeats = houseSeats
        self.senateSeats = 2
        self.percentHouseSeats = None
        self.percentSenateSeats = None
    
    def getElectoralVotes(self):
        return self.__houseSeats + self.__senateSeats
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def isState(self):
        return self.__isState
    @isState.setter
    def isState(self, isState):
        self.__isState = isState
    
    @property
    def isCapital(self):
        return self.__isCapital
    @isCapital.setter
    def isCapital(self, isCapital):
        self.__isCapital = isCapital

    @property
    def population(self):
        return self.__population
    @population.setter
    def population(self, population):
        self.__population = population

    @property
    def percentPopulation(self):
        return self.__percentPopulation
    @percentPopulation.setter
    def percentPopulation(self, percentPopulation):
        self.__percentPopulation = percentPopulation

    @property
    def houseSeats(self):
        return self.__houseSeats
    @houseSeats.setter
    def houseSeats(self, houseSeats):
        self.__houseSeats = houseSeats
    
    @property
    def senateSeats(self):
        return self.__senateSeats
    @senateSeats.setter
    def senateSeats(self, senateSeats):
        self.__senateSeats = senateSeats
    
    @property
    def percentHouseSeats(self):
        return self.__percentHouseSeats
    @percentHouseSeats.setter
    def percentHouseSeats(self, percentHouseSeats):
        self.__percentHouseSeats = percentHouseSeats
    
    @property
    def percentSenateSeats(self):
        return self.__percentSenateSeats
    @percentSenateSeats.setter
    def percentSenateSeats(self, percentSenateSeats):
        self.__percentSenateSeats = percentSenateSeats

def getPercents(regions):
    totalPopulation = sum([x.population for x in regions])
    totalHouseSeats = sum([x.houseSeats for x in regions])
    totalSenateSeats = sum([x.senateSeats for x in regions])
    for x in regions:
        x.percentPopulation = x.population / totalPopulation * 100
        x.percentHouseSeats = x.houseSeats / totalHouseSeats * 100
        x.percentSenateSeats = x.senateSeats / totalSenateSeats * 100
    return regions

def main(demographics, capital, territories):
    csv_reader = csv.reader(open(demographics), delimiter = ',')
    data = [x for x in csv_reader]
    regions = [Region(x[0], x[1], x[2], int(x[3]), int(x[4])) for x in data[1:]]
    if not capital:
        regions = [x for x in regions if not x.isCapital]
    if not territories:
        regions = [x for x in regions if x.isState or x.isCapital]


parser = argparse.ArgumentParser()
parser.add_argument('demographics')
parser.add_argument('--capital', '-c', default = True)
parser.add_argument('--territories', '-t', default = False)
args = parser.parse_args()
demographics = args.demographics
capital = str2bool(args.capital)
territories = str2bool(args.territories)
main(demographics, capital, territories)