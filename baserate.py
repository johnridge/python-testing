import argparse
import math
import numpy as np
import matplotlib.pyplot as plt

def main(population, prevalence, sensitivity, specificity, retestPositives, retestNegatives):
    def truePositives(prevalence, sensitivity, retestPositives):
        return prevalence * sensitivity ** (1 + retestPositives)
    def falseNegatives(prevalence, sensitivity, retestNegatives):
        return prevalence * (1 - sensitivity) ** (1 + retestNegatives)
    def trueNegatives(prevalence, specificity, retestNegatives):
        return (1 - prevalence) * specificity ** (1 + retestNegatives)
    def falsePostives(prevalence, specificity, retestPositives):
        return (1 - prevalence) * (1 - specificity) ** (1 + retestPositives)
    def positivePredictiveValue(prevalence, sensitivity, specificity, retestPositives):
        return truePositives(prevalence, sensitivity, retestPositives) / (truePositives(prevalence, sensitivity, retestPositives) + falsePostives(prevalence, specificity, retestPositives))
    def negativePredictiveValue(prevalence, sensitivity, specificity, retestNegatives):
        return trueNegatives(prevalence, specificity, retestNegatives) / (trueNegatives(prevalence, specificity, retestNegatives) + falseNegatives(prevalence, sensitivity, retestNegatives))
    p = np.linspace(0, 1, 500)
    prevalence = prevalence / 100
    sensitivity = sensitivity / 100
    specificity = specificity / 100
    tp = truePositives(p, sensitivity, retestPositives)
    fn = falseNegatives(p, sensitivity, retestNegatives)
    tn = trueNegatives(p, specificity, retestNegatives)
    fp = falsePostives(p, specificity, retestPositives)
    ppv = positivePredictiveValue(p, sensitivity, specificity, retestPositives)
    npv = negativePredictiveValue(p, sensitivity, specificity, retestNegatives)
    accuracy = truePositives(prevalence, sensitivity, retestPositives) + trueNegatives(prevalence, specificity, retestNegatives)
    pt = (math.sqrt(sensitivity * (-specificity + 1)) + specificity - 1) / (sensitivity + specificity - 1)
    plt.plot(p, ppv, color = 'tab:blue', label = f'Positive Predictive Value ({positivePredictiveValue(prevalence, sensitivity, specificity, retestPositives):.2f})')
    plt.plot(p, npv, color = 'tab:red', label = f'Negative Predictive Value ({negativePredictiveValue(prevalence, sensitivity, specificity, retestNegatives):.2f})')
    plt.plot(prevalence, positivePredictiveValue(prevalence, sensitivity, specificity, retestPositives), 'o', color = 'tab:blue')
    plt.plot(prevalence, negativePredictiveValue(prevalence, sensitivity, specificity, retestNegatives), 'o', color = 'tab:red')
    plt.plot([], [], label = f'Accuracy: {accuracy:.2f}')
    plt.plot([], [], label = f'Prevalence Threshold: {pt:.2f}')
    #plt.plot(prevalence)
    plt.xlabel('Prevalence')
    plt.ylabel('Positive/Negative Predictive Value')
    plt.grid(axis='both', alpha=0.75)
    plt.legend(loc = 'upper right')
parser = argparse.ArgumentParser()
parser.add_argument('--population', '-pop', type = int)
parser.add_argument('--prevalence', '-prev', type = float)
parser.add_argument('--sensitivity', '-sen', type = float)
parser.add_argument('--specificity', '-spec', type = float)
parser.add_argument('--retestPositives', '-rp', type = int, default = 0)
parser.add_argument('--retestNegatives', '-rn', type = int, default = 0)
args = parser.parse_args()
population = args.population
prevalence = args.prevalence
sensitivity = args.sensitivity
specificity = args.specificity
retestPositives = args.retestPositives
retestNegatives = args.retestNegatives
main(population, prevalence, sensitivity, specificity, retestPositives, retestNegatives)
plt.show()