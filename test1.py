import scurve.scurve as scurve
import numpy as np

side = 4
power2 = int(2 ** np.floor(np.sqrt(side * 2)))
map = scurve.fromSize('hilbert', 2, power2 * power2)
print(map.dimensions())

