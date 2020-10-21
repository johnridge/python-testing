import math
import numpy as np
import matplotlib.pyplot as plt

c = 3*10**14
h = 6.626*10**(-22)
k = 1.38*10**(-11)
x = np.linspace(0.0001, 3, 500)
B = (10**(-6))*2*h*c**2/(x**5*(np.exp(h*c/(x*k*5000))-1))
plt.plot(x,B)
plt.show()
