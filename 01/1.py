import numpy as np

def fuelCalc(mass):
    return np.floor(mass/3) - 2

data = np.array(np.loadtxt("./01/input.txt"))
total = np.sum(fuelCalc(data))
print(total)