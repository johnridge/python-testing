import argparse
import numpy as np
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

class Distribution(ABC):
    def __init__(self, size):
        self.size = size
        self.sample = []
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, size):
        self.__size = size
    @property
    def sample(self):
        return self.__sample
    @sample.setter
    def sample(self, sample):
        self.__sample = sample
    @abstractmethod
    def generateSample(self):
        pass
    
class Normal(Distribution):
    def __init__(self, size):
        super().__init__(size)
    def generateSample(self):
        self.sample = np.random.normal()
