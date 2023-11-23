import numpy as np
import matplotlib.pyplot as plt
import egttools as egt
from plot import make_plot


def sim_game(nb_rounds, A, strategies):
    return egt.games.NormalFormGame(nb_rounds, A, strategies)


def show_plot(game):
    make_plot(game)