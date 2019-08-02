import numpy as np
from scipy import stats

# Fixing random state for reproducibility
np.random.seed(9527)

chi_squared_df2 = np.random.chisquare(2, size=10000)
chi_squared_df5 = np.random.chisquare(5, size=10000)
stats.skew(chi_squared_df2)
stats.skew(chi_squared_df5)

import matplotlib.pyplot as plt

output = plt.hist([chi_squared_df2,chi_squared_df5], bins=50, histtype='step', 
                  label=['2 degrees of freedom','5 degrees of freedom'])
plt.legend(loc='upper right')

#Exercise with Break:
#Try Log-Normal Random Number with different mean and SD, with size 10000


#reference: https://scipy-cookbook.readthedocs.io/items/BrownianMotion.html

from numpy import sqrt
from scipy.stats import norm


def brownian(x0, nstep, dt, delta):

    x0 = np.asarray(x0)

    # For each element of x0, generate a sample of n numbers from a
    # normal distribution.
    r = np.random.normal(0, delta*sqrt(dt), x0.shape + (nstep,))
#    r = norm.rvs(size=x0.shape + (n,), scale=delta*sqrt(dt))

    # This computes the Brownian motion by forming the cumulative sum of
    # the random samples. 
    out = np.cumsum(r, axis=-1)

    # Add the initial condition.
    out += np.expand_dims(x0, axis=-1)

    return(out)

# The Wiener process parameter, Total time, Number of steps.
delta, T, nstep = (2, 10.0, 50)
# Time step size
dt = T/nstep
# Number of realizations to generate.
npath = 10
# Create an empty array to store the realizations.
x = np.empty((npath,nstep+1))
# Initial values of x.
x[:, 0] = 50
# Brownian Process for each path
x[:,1:] = brownian(x[:,0], nstep, dt, delta)

from matplotlib import pyplot as plt
t = np.linspace(0.0, nstep*dt, nstep+1)
for k in range(npath):
    plt.plot(t, x[k])
plt.xlabel('t', fontsize=16)
plt.ylabel('x', fontsize=16)
plt.grid(True)
plt.show()