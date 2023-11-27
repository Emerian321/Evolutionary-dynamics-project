import pairwise_imitation_process as pip
import numpy as np
import egttools as egt
from math import exp

import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

payoff_matrix = np.array([
    [0, 3],
    [-1, 2]
])

strategies = [egt.behaviors.NormalForm.TwoActions.Defector(), egt.behaviors.NormalForm.TwoActions.TFT()] # DO NOT CHANGE LIST ORDERING

R = 100

beta = 10

mu = exp(-3)

Z = 50

transitory = 10**3

nb_generations = 10**6

nb_runs = 10

game = egt.games.NormalFormGame(R, payoff_matrix, strategies)

A = game.expected_payoffs()

sd = pip.estimate_stationary_distribution(nb_runs, transitory, nb_generations, beta, mu, Z, A)
print(sum(sd))
fix, ax = plt.subplots(figsize=(8, 5))

ax.plot(np.arange(0, Z+1), sd)
ax.set_ylabel('stationary distribution', fontsize=15, fontweight='bold')
ax.set_xlabel('Quantity of Copycats', fontsize=15, fontweight='bold')
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.tick_params(axis='x', which='both', labelsize=15, width=3)
ax.tick_params(axis='y', which='both', direction='in', labelsize=15, width=3)

for tick in ax.xaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for tick in ax.yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')

plt.show()