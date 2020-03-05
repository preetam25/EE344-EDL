import numpy as np
import math
import random
import matplotlib.pyplot as plt
sigmax = 0.02
sigmay = 0.02
sigmaz = 0.02
xscale = 2
yscale = 3
zscale = 4
sigmam1 = 0.02
sigmam2 = 0.02
sigmam3 = 0.02
i = 1
observations = 100
x = np.empty(observations)
y = np.empty(observations)
z = np.empty(observations)
m1 = np.empty(observations)
m2 = np.empty(observations)
m3 = np.empty(observations)
ax =1.0
ay =1.0
az =1.0
mx =1.0
my =1.0
mz =1.0
am1 = 0.4
am2 = 0.4
am3 = 0.4
x[0] = 0.5
y[0] = 0.5
z[0] = 0.5
m1[0] = mx*math.exp(xscale*x[0]+yscale*y[0]+z[0]) + random.gauss(0,sigmam1)
m2[0] = my*math.exp(xscale*x[0]+y[0]+zscale*z[0]) + random.gauss(0,sigmam2)
m3[0] = mz*math.exp(x[0]+yscale*y[0]+zscale*z[0]) + random.gauss(0,sigmam3)

while i<observations:
  x[i] = ax*x[i-1] + random.gauss(0,sigmax)
  y[i] = ay*y[i-1] + random.gauss(0,sigmay)
  z[i] = az*z[i-1] + random.gauss(0,sigmaz)
  m1[i] = mx*math.exp(xscale*x[i]+yscale*y[i]+z[i]) + random.gauss(0,sigmam1)
  m2[i] = my*math.exp(xscale*x[i]+y[i]+zscale*z[i]) + random.gauss(0,sigmam2)
  m3[i] = mz*math.exp(x[i]+yscale*y[i]+zscale*z[i]) + random.gauss(0,sigmam3)
  i = i+1

plt.plot(x)
plt.show()
plt.plot(y)
plt.show()
plt.plot(z)
plt.show()
plt.plot(x,y)
plt.show()
plt.plot(y,z)
plt.show()
plt.plot(x,z)
plt.show()
