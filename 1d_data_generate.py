import numpy as np
import math
import random
import matplotlib.pyplot as plt
sigmax = 0.02
sigmam = 0.02
i = 1
observations = 500
x = np.empty(observations)
m = np.empty(observations)
ax =1.0
am = 0.4
x[0] = 0.5
m[0] = ay*math.exp(x[0]) + random.gauss(0,sigmam)
while i<observations:
  x[i] = ax*x[i-1] + random.gauss(0,sigmax)
  m[i] = ay*math.exp(x[i]) + random.gauss(0,sigmam)
  i = i+1

plt.plot(m)
plt.show()
plt.plot(x)
plt.show()
