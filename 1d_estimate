import numpy as np
import math
import random
import matplotlib.pyplot as plt
from scipy import stats
particles = 100
likelihood = np.empty(particles)
estimated = np.empty(observations)
particle_estimate = np.random.uniform(-0.5,1,(particles))
i = 0
while i <observations:
  particle_estimate = particle_estimate + np.random.normal(0,5*sigmax,(particles))
  j = 0
  while j < np.shape(particle_estimate)[0]:
    likelihood[j] = math.exp(-5*((m[i]-ay*math.exp(particle_estimate[j]))**2))
    j = j+1
  likelihood = likelihood/np.sum(likelihood)
  custm = stats.rv_discrete(name='custm', values=(particle_estimate*10000000, likelihood))
  particle_estimate = custm.rvs(size=particles)/10000000
  #print("actual",x[i])
  #print("estimated",np.mean(particle_estimate))
  estimated[i] = np.mean(particle_estimate)
  #print("error",(x[i]-np.mean(particle_estimate))/x[i])
  i= i+1
plt.plot(x)
plt.plot(estimated)
plt.show()
