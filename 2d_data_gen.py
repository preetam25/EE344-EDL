import numpy as np
import math
import random
import matplotlib.pyplot as plt
sigmax = 0.02
xscale = 2
yscale = 3
sigmay = 0.02
sigmam1 = 0.02
sigmam2 = 0.02
i = 1
observations = 100
x = np.empty(observations)
y = np.empty(observations)
m1 = np.empty(observations)
m2 = np.empty(observations)
ax =1.0
ay =1.0
am1 = 0.4
am2 = 0.4
x[0] = 0.5
y[0] = 0.5
m1[0] = ay*math.exp(xscale*x[0]+y[0]) + random.gauss(0,sigmam1)
m2[0] = ay*math.exp(x[0]+yscale*y[0]) + random.gauss(0,sigmam2)

while i<observations:
  x[i] = ax*x[i-1] + random.gauss(0,sigmax)
  y[i] = ay*y[i-1] + random.gauss(0,sigmay)
  m1[i] = ay*math.exp(xscale*x[i]+y[i]) + random.gauss(0,sigmam1)
  m2[i] = ay*math.exp(x[i]+yscale*y[i]) + random.gauss(0,sigmam2)

  i = i+1

plt.plot(x)
plt.show()
plt.plot(x)
plt.show()
plt.plot(x,y)
plt.show()
