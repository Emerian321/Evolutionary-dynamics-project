import numpy as np
import matplotlib.pyplot as plt

import egttools as egt

from egttools.plotting.simplified import plot_replicator_dynamics_in_simplex


strategies = [egt.behaviors.NormalForm.TwoActions.Cooperator(), 
              egt.behaviors.NormalForm.TwoActions.Defector(), 
              egt.behaviors.NormalForm.TwoActions.TFT()]

strategy_labels = [strategy.type().replace("NFGStrategies::", '') for strategy in strategies]

A = np.array([[0, 3],
            [-1, 2]])

nb_rounds = 10

game = egt.games.NormalFormGame(nb_rounds, A, strategies)
print(game.expected_payoffs())

fig, ax = plt.subplots(figsize=(10,8))

simplex, gradients, roots, roots_xy, stability = plot_replicator_dynamics_in_simplex(game.expected_payoffs(), ax=ax)

plot = (simplex.draw_triangle()
           .draw_gradients(density=1)
           .add_colorbar(label='gradient of selection')
           .add_vertex_labels(strategy_labels, epsilon_bottom=0.12)
           .draw_stationary_points(roots_xy, stability)
#            .draw_trajectory_from_roots(lambda u, t: egt.analytical.replicator_equation(u, game.expected_payoffs()), 
#                                        roots,
#                                        stability,
#                                        trajectory_length=30,
#                                        linewidth=0.1,
#                                        step=0.01,
#                                        color='k', draw_arrow=True, arrowdirection='right', arrowsize=30, zorder=4, arrowstyle='fancy')
           .draw_scatter_shadow(lambda u, t: egt.analytical.replicator_equation(u, game.expected_payoffs()), 100, color='gray', marker='.', s=0.1)
          )

ax.axis('off')
ax.set_aspect('equal')

plt.xlim((-.05,1.05))
plt.ylim((-.02, simplex.top_corner + 0.05))
plt.show()
