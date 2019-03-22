# Based on https://github.com/probml/pmtk3/blob/master/demos/bimodalDemo.m
# Bimodal Spike Demo

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import os

# Define two normal distrubutions and their corresponding weights.
mu = [0, 2]
sigma = [1, 0.05]
n = [norm(loc=mu[i], scale=sigma[i]) for i in range(2)]
w = [0.5, 0.5]

# Define a set of x points for graphing.
xs = np.linspace(-2, 2*mu[1], 600)

# Combine the two distributions by their weights, evaluated at the x points.
p = sum(w[i] * n[i].pdf(xs) for i in range(2))

# Calculate the mean of the final distribution.
mean_p = np.mean(xs * p)

# Plot the final distribution and its mean.
linewidth = 3
plt.plot(xs, p, 'black', linewidth=linewidth)
plt.vlines(mean_p, ymin=0, ymax=max(p), color='red', linewidth=linewidth)
plt.savefig(os.path.join('../figures', 'bimodalSpike'))
plt.show()
