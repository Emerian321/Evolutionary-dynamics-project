from random import randint
import numpy as np

def moran_step(current_state, beta, mu, Z, A):
    # select 2 random individuals in the population
    first_pick = selected(current_state, Z)
    current_state -= first_pick
    second_pick = selected(current_state, Z-1)
    current_state -= second_pick
    
    # Calculate the fitness difference between the two selections
    fitness_diff = fitness(Z-2, A, current_state, first_pick, second_pick)
    
    # Put back invader to the population
    current_state += second_pick
    
    # If there is a random mutation for the resident
    if np.random.rand() < mu:
        current_state += randint(0, 1)
    
    # else if resident decides to be invaded
    elif np.random.rand() < fermi(beta, fitness_diff):
        current_state -= (first_pick - second_pick)

    # return updated state
    return int(current_state)

def fermi(beta, fitness_diff):
    '''
    The probability that the first type imitates the second
    '''
    return 1.0/(1.0 + np.exp(-beta*fitness_diff))
    

def fitness(Z, A, k, resident, invader):
    '''
    The fitness function determines the average payoff of k
    invaders and N-k residents
    in the population of N players.
    '''
    
    # Invader's fitness
    resultA=((k*A[invader][1])+
    ((Z-k)*A[invader][0]))/float(Z)
    
    # resident's fitness
    resultB=((k*A[resident][1])+
    ((Z-k)*A[resident][0]))/float(Z)
    
    # fitness difference
    return resultB - resultA


def selected(current_state, Z):
    selected = randint(0, Z)
    if selected <= current_state:
        return 1 # TFT
    else:
        return 0 # Defector
    
    
def estimate_stationary_distribution(nb_runs, transitory, nb_generations, beta, mu, Z, A):
    res = [0 for i in range(Z+1)]
    for __ in range(nb_runs):
        state = randint(0, Z) # starting amount of TFT in population
        for _ in range(transitory):
            state = moran_step(state, beta, mu, Z, A)
        for _ in range(nb_generations-transitory):
            state = moran_step(state, beta, mu, Z, A)
            res[state] += 1
    
    for state in range(len(res)):
        res[state] = res[state] / (nb_runs * (nb_generations - transitory))
    
    return res