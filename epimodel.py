import argparse
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate
from celluloid import Camera

def main(modelType, tMax, resolution, I0, N_0, Lambda, mu, beta, gamma, epsilon, omega, nu, animatePlot):
    L = lambda x : x * Lambda 
    M = lambda x : x * mu
    B = lambda x : x * beta
    E = lambda x : x * epsilon 
    G = lambda x : x * gamma
    O = lambda x : x * omega
    N = lambda x : x * nu
    def SIR(t, c):
        Nt = c[0] + c[1] + c[2]
        SI = c[0] * c[1]
        return [L(Nt) - B(SI)/Nt - M(c[0]), B(SI)/Nt - G(c[1]) - M(c[1]), G(c[1]) - M(c[2]), B(SI)/Nt, G(c[1])]
    def SIRS(t, c):
        Nt = c[0] + c[1] + c[2]
        SI = c[0] * c[1]
        return [L(Nt) - B(SI) / Nt - M(c[0]) + N(c[2]), B(SI) / Nt - G(c[1]) - M(c[1]), G(c[1]) - N(c[2]) - M(c[2]), B(SI) / Nt, G(c[1])]
    def SIRD(t, c):
        Nt = c[0] + c[1] + c[2]
        SI = c[0] * c[1]
        return [L(Nt) - B(SI)/Nt - M(c[0]), B(SI)/Nt - G(c[1]) - M(c[1]), G(c[1]) - M(c[2]), O(c[1]), B(SI)/Nt, G(c[1]), O(c[1])]
    def SIRDS(t, c):
        Nt = c[0] + c[1] + c[2]
        SI = c[0] * c[1]
        return [L(Nt) - B(SI) / Nt - M(c[0]) + N(c[2]), B(SI) / Nt - G(c[1]) - M(c[1]) - O(c[1]), G(c[1]) - M(c[2]) - N(c[2]), O(c[1]), B(SI) / Nt, G(c[1]), O(c[1])]
    def SEIR(t, c):
        Nt = c[0] + c[1] + c[2] + c[3]
        SI = c[0] * c[2]
        return [L(Nt) - B(SI)/Nt - M(c[0]), B(SI)/Nt - E(c[1]) - M(c[1]), E(c[1]) - G(c[2]) - M(c[2]), G(c[2]) - M(c[3]), B(SI)/Nt, E(c[1]), G(c[2])]
    def SEIRS(t, c):
        Nt = c[0] + c[1] + c[2] + c[3]
        SI = c[0] * c[2]
        return [L(Nt) + N(c[3]) - B(SI)/Nt - M(c[0]), B(SI)/Nt - E(c[1]) - M(c[1]), E(c[1]) - G(c[2]) - M(c[2]), G(c[2]) - N(c[3]) - M(c[3]), B(SI)/Nt, E(c[1]), G(c[2])]
    def SEIRD(t, c):
        Nt = c[0] + c[1] + c[2] + c[3]
        SI = c[0] * c[2]
        return [L(Nt) - B(SI)/Nt - M(c[0]), B(SI)/Nt - E(c[1]) - M(c[1]), E(c[1]) - G(c[2]) - O(c[2]) - M(c[2]), G(c[2]) - M(c[3]), O(c[2]), B(SI)/Nt, E(c[1]), G(c[2]), O(c[2])]
    def SEIRDS(t, c):
        Nt = c[0] + c[1] + c[2] + c[3]
        SI = c[0] * c[2]
        return [L(Nt) + N(c[3]) - B(SI)/Nt - M(c[0]), B(SI)/Nt - E(c[1]) - M(c[1]), E(c[1]) - G(c[2]) - O(c[2]) - M(c[2]), G(c[2]) - N(c[3]) - M(c[3]), O(c[2]), B(SI)/Nt, E(c[1]), G(c[2]), O(c[2])]
    def getInitialValuesAndPlotInfo(modelType, N_0, I0):
        labels = ['Susceptible'] + ['Exposed' if x == 'E' else 'Infectious' if x == 'I' else 'Recovered' if x == 'R' else 'Deceased' if x == 'D' else '' for x in modelType[1:]]
        labels = [x for x in labels if x != '']
        deltaLabels = ['Newly ' + x for x in labels[1:]]
        deltaColors = ['tab:orange' if x == 'E' else 'tab:purple' if x == 'I' else 'tab:green' if x == 'R' else 'tab:red' if x == 'D' else '' for x in modelType[1:]]
        deltaColors = [x for x in deltaColors if x != '']
        colors = ['tab:blue'] + deltaColors
        initialValues = [N_0 - I0] + [0 if x == 'E' else I0 if x == 'I' else 0 if x == 'R' else 0 if x == 'D' else '' for x in modelType[1:]]
        initialValues = initialValues + [0 for x in deltaLabels]
        initialValues = [x for x in initialValues if x != '']
        modelTitle = f'{modelType} Model\n$N_0 = {N_0}$, $\Lambda = {Lambda}$, $\mu = {mu}$\n$R_0 = {round(beta / gamma, 2)}$' 
        addendum = [f', $\epsilon = {epsilon}$' if x == 'E' else f', $\omega = {omega}$' if x == 'D' else f', $\\nu = {nu}$' if x == 'S' else '' for x in modelType[1:]]
        addendum = [x for x in addendum if x != '']
        for x in addendum:
            modelTitle = modelTitle + x
        return [labels, deltaLabels], [colors, deltaColors], initialValues, modelTitle
    def getCompartments(model, delta):
        compartments = [[n[x] for n in model.y.T] for x in range(len(model.y.T[0]))]
        deltaCompartments = [[0] + [x[n] - x[n - 1] for n in range(1, len(x))] for x in compartments[-delta:]]
        return [compartments[0:len(compartments) - delta], deltaCompartments]
    def makePlot(model, compartments, labels, colors, modelTitle):
        fig, axs = plt.subplots(2, sharex = True)
        axs[0].set_title(modelTitle)
        for x in range(len(compartments[0])):
            axs[0].plot(model.t, compartments[0][x], color = f'{colors[0][x]}', label = f'{labels[0][x]}')
        for x in range(len(compartments[1])):
            axs[1].plot(model.t, compartments[1][x], color = f'{colors[1][x]}', label = f'{labels[1][x]}')
        for n in axs:
            n.margins(x=0)
            n.grid(axis = 'both', alpha = 0.75)
            n.set(xlabel = 'Time')
            n.set(ylabel = 'Individuals')
            n.legend(loc = 'upper right')
    def makeAnimation(model, compartments, labels, colors):
        fig, axs = plt.subplots(2)
        camera = Camera(fig)
        for x in range(len(model.t)):
            for n in range(len(compartments[0])):
                axs[0].plot(model.t[:x], compartments[0][n][:x], color = f'{colors[0][n]}')
            for n in range(len(compartments[1])):
                axs[1].plot(model.t[:x], compartments[1][n][:x], color = f'{colors[1][n]}')
            for n in axs:
                n.grid(axis = 'both', alpha = 0.75)
                n.set(xlabel = 'Time')
                n.set(ylabel = 'Individuals')
            if x % 1 == 0:
                camera.snap()
        animation = camera.animate()
        animation.save(f'{modelType}model.gif', writer = 'imagemagick')
    modelDict = {'SIR':SIR, 'SIRS':SIRS, 'SIRD':SIRD, 'SIRDS':SIRDS, 'SEIR':SEIR, 'SEIRS':SEIRS, 'SEIRD':SEIRD, 'SEIRDS':SEIRDS}
    labels, colors, initialValues, modelTitle = getInitialValuesAndPlotInfo(modelType, N_0, I0)
    model = scipy.integrate.solve_ivp(modelDict[modelType], (0, tMax), initialValues, t_eval = np.linspace(0, tMax, resolution))
    compartments = getCompartments(model, len(labels[1]))
    makePlot(model, compartments, labels, colors, modelTitle)
    plt.show()
    if animatePlot:
        makeAnimation(model, compartments, labels, colors)

parser = argparse.ArgumentParser()
parser.add_argument('--tMax', '-t', type = float)
parser.add_argument('--resolution', '-r', default = 1500, type = int)
parser.add_argument('--initialInfected', '-i', type = int)
parser.add_argument('--population', '-N', type = int)
parser.add_argument('--birthRate', '-lambda', type = float, default = 0.0115)
parser.add_argument('--mortalityRate', '-mu', type = float, default = 0.0110)
parser.add_argument('--meanContacts', '-beta', type = float)
parser.add_argument('--recoveryPeriod', '-gamma', type = float)
parser.add_argument('--latentPeriod', '-epsilon', type = float, default = 0)
parser.add_argument('--fatalityRate', '-omega', type = float, default = 0)
parser.add_argument('--immunityPeriod', '-nu', type = float, default = None)
parser.add_argument('--animatePlot', '-a', default = True)
args = parser.parse_args()
tMax = args.tMax
resolution = args.resolution
I0 = args.initialInfected
N_0 = args.population
Lambda = args.birthRate
mu = args.mortalityRate
beta = args.meanContacts
gamma = 1 / (args.recoveryPeriod)
epsilon = args.latentPeriod
modelType = 'S'
if epsilon != 0:
    epsilon = 1 / epsilon
    modelType = modelType + 'E'
modelType = modelType + 'IR'
omega = args.fatalityRate
if omega != 0:
    modelType = modelType + 'D'
nu = args.immunityPeriod
if nu != None:
    nu = 1 / nu
    modelType = modelType + 'S'
animatePlot = args.animatePlot
if animatePlot == 'False':
    animatePlot = False
main(modelType, tMax, resolution, I0, N_0, Lambda, mu, beta, gamma, epsilon, omega, nu, animatePlot)
plt.show()
