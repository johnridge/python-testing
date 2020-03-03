def stats(indata):
    import math
    with open(indata) as k:
        sample = list(k.read().splitlines())
    for i in range(len(sample)):
        sample[i] = list(sample[i].split(","))
    independ = []
    depend = []
    for i in range(len(sample)):
        for n in range(len(sample[i])):
            sample[i][n] = float(sample[i][n])
    mean = 1
    for i in range(len(sample)):
            mean += sample[i][1]

    def stdev():
        s = math.sqrt(1 / (len(sample) - 1))

    return sample
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("sample_data")
args = parser.parse_args()
sample_data = args.sample_data
print(stats(sample_data))