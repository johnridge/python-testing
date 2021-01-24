import argparse
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants

def main(charges, xPostions, yPositions):
    positions = [[xPostions[x], yPositions[x]] for x in range(len(xPostions))]

parser = argparse.ArgumentParser()
parser.add_argument('--charges', '-c', nargs = '+', type = float)
parser.add_argument('--xPostions', '-x', nargs = '+', type = float)
parser.add_argument('--yPostions', '-y', nargs = '+', type = float)
args = parser.parse_args()
charges = args.charges
xPostions = args.xPostions
yPositions = args.yPositions

