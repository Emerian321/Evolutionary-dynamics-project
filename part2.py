import numpy as np

import egttools as egt

from egttools.plotting.simplified import plot_replicator_dynamics_in_simplex


strategies = [egt.behaviors.NormalForm.TwoActions.Cooperator(), 
              egt.behaviors.NormalForm.TwoActions.Defector(), 
              egt.behaviors.NormalForm.TwoActions.TFT(), 
              egt.behaviors.NormalForm.TwoActions.GRIM(), 
              egt.behaviors.NormalForm.TwoActions.Detective()]

strategy_labels = [strategy.type().replace("NFGStrategies::", '') for strategy in strategies]

nb_rounds = 100

A = np.array([[0, 3],
            [-1, 2]])

game = egt.games.NormalFormGame(nb_rounds, A, strategies)
print(game.expected_payoffs())

