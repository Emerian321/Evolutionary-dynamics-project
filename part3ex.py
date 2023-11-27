import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import seaborn as sns

import egttools as egt

A = np.array([
    [0, 3],
    [-1, 2]
])


strategies = [egt.behaviors.NormalForm.TwoActions.TFT(), egt.behaviors.NormalForm.TwoActions.Defector()]

nb_rounds = 100

game = egt.games.NormalFormGame(nb_rounds, A, strategies)

print(game.expected_payoffs())


Z = 50
beta = 1
mu = 1e-3
transitory = 1000
nb_generations = 1000000
nb_runs = 10

evolver = egt.numerical.PairwiseComparisonNumerical(Z, game, 100000)

sd = evolver.estimate_stationary_distribution_sparse(nb_runs, nb_generations, transitory, beta, mu)
print(sd.toarray()[0])
sns.set_context("notebook", rc={"lines.linewidth": 3, "axes.linewidth": 3})

fix, ax = plt.subplots(figsize=(8, 5))

ax.plot(np.arange(0, Z+1)/Z, sd.toarray()[0])
ax.set_ylabel('stationary distribution', fontsize=15, fontweight='bold')
ax.set_xlabel('frequency of Copycat (k/Z)', fontsize=15, fontweight='bold')
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.tick_params(axis='x', which='both', labelsize=15, width=3)
ax.tick_params(axis='y', which='both', direction='in', labelsize=15, width=3)

for tick in ax.xaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for tick in ax.yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')

sns.despine()

plt.show()