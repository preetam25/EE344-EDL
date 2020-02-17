import numpy as np
import math
import random
import matplotlib.pyplot as plt
sigmax = math.sqrt(0.2)
sigmay = math.sqrt(0.2)
i = 1
observations = 100
x = np.empty(observations)
y = np.empty(observations)
ax = 0.6
ay = 0.2
x[0] = 2
y [0] = ay*math.exp(x[0]) + random.gauss(0,sigmay)
while i<100:
  x[i] = ax*x[i-1] + random.gauss(0,sigmax)
  y[i] = ay*math.exp(x[i]) + random.gauss(0,sigmay)
  i = i+1
print(x)
print(y)

