import numpy as np
import matplotlib.pyplot as plt
from math import *

' sin(i)*2'
def plot(string):
    x = np.array(np.arange(-10,10,0.01))
    y = []
    for i in x:
        y.append(eval(string))
    y = np.array(y)
    p = plt.plot(x,y)
    plt.show()

plot('cos(i)*2')
