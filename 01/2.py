import numpy as np

vals = np.array(np.loadtxt('./01/input.txt'))

def fuelCalc(vals):
    fuel = [value // 3 - 2 for value in vals]
    for f in fuel:
        t = f // 3 - 2
        if t > 0:
            fuel.append(t)
    return sum(fuel)

print(fuelCalc(vals))