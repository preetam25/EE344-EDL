import numpy as np
import math
import random
import matplotlib.pyplot as plt
from scipy import stats
particles = 100
likelihood = np.empty(particles)
estimatedx = np.empty(observations)
estimatedy = np.empty(observations)
particle_estimate = np.random.uniform(-0.5,1,(particles,2))
i = 0
while i <observations:
  particle_estimate = particle_estimate + np.random.normal(0,5*sigmax,(particles,2))
  j = 0
  while j < np.shape(particle_estimate)[0]:
    likelihood[j] = math.exp(-5*((m1[i]-ay*math.exp(xscale*particle_estimate[j,0]+particle_estimate[j,1]))**2))*math.exp(-5*((m2[i]-ay*math.exp(particle_estimate[j,0]+yscale*particle_estimate[j,1]))**2))
    j = j+1
  likelihood = likelihood/np.sum(likelihood)
  custmx = stats.rv_discrete(name='custmx', values=(particle_estimate[:,0]*10000000, likelihood))
  particle_estimate[:,0] = custmx.rvs(size=particles)/10000000
  custmy = stats.rv_discrete(name='custmy', values=(particle_estimate[:,1]*10000000, likelihood))
  particle_estimate[:,1] = custmy.rvs(size=particles)/10000000
  #print("actual",x[i])
  #print("estimated",np.mean(particle_estimate))
  estimatedx[i] = np.mean(particle_estimate[:,0])
  estimatedy[i] = np.mean(particle_estimate[:,1])
  #print("error",(x[i]-np.mean(particle_estimate))/x[i])
  i= i+1
plt.plot(x)
plt.plot(estimatedx)
plt.show()
plt.plot(y)
plt.plot(estimatedy)
plt.show()
plt.plot(x,y)
plt.plot(estimatedx,estimatedy)
plt.show()
