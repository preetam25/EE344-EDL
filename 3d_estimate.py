import numpy as np
import math
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import stats
particles = 500
likelihood = np.empty(particles)
estimatedx = np.empty(observations)
estimatedy = np.empty(observations)
estimatedz = np.empty(observations)
particle_estimate = np.random.uniform(-0.5,1,(particles,3))
i = 0
while i <observations:
  particle_estimate = particle_estimate + np.random.normal(0,5*sigmax,(particles,3))
  j = 0
  while j < np.shape(particle_estimate)[0]:
    likelihood[j] = math.exp(-2*((m1[i]-mx*math.exp(xscale*particle_estimate[j,0]+yscale*particle_estimate[j,1]+particle_estimate[j,2]))**2))*math.exp(-2*((m2[i]-my*math.exp(xscale*particle_estimate[j,0]+particle_estimate[j,1]+zscale*particle_estimate[j,2]))**2))*math.exp(-2*((m3[i]-mz*math.exp(particle_estimate[j,0]+yscale*particle_estimate[j,1]+zscale*particle_estimate[j,2]))**2))
    j = j+1
  likelihood = likelihood/np.sum(likelihood)
  custmx = stats.rv_discrete(name='custmx', values=(particle_estimate[:,0]*10000000, likelihood))
  particle_estimate[:,0] = custmx.rvs(size=particles)/10000000
  custmy = stats.rv_discrete(name='custmy', values=(particle_estimate[:,1]*10000000, likelihood))
  particle_estimate[:,1] = custmy.rvs(size=particles)/10000000
  custmz = stats.rv_discrete(name='custmz', values=(particle_estimate[:,2]*10000000, likelihood))
  particle_estimate[:,2] = custmz.rvs(size=particles)/10000000
  #print("actual",x[i])
  #print("estimated",np.mean(particle_estimate))
  estimatedx[i] = np.mean(particle_estimate[:,0])
  estimatedy[i] = np.mean(particle_estimate[:,1])
  estimatedz[i] = np.mean(particle_estimate[:,2])

  #print("error",(x[i]-np.mean(particle_estimate))/x[i])
  i= i+1
plt.plot(x)
plt.plot(estimatedx)
plt.show()
plt.plot(y)
plt.plot(estimatedy)
plt.show()
plt.plot(z)
plt.plot(estimatedz)
plt.show()
plt.plot(x,y)
plt.plot(estimatedx,estimatedy)
plt.show()
plt.plot(x,z)
plt.plot(estimatedx,estimatedz)
plt.show()
plt.plot(y,z)
plt.plot(estimatedy,estimatedz)
plt.show()
fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot3D(x, y, z, 'blue')
ax.plot3D(estimatedx, estimatedy, estimatedz, 'red')
plt.show()
