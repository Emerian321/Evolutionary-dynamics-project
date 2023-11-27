from random import randint

def moran_step(current_state, beta, mu, Z, A):
    first_pick = selected(current_state, Z)
    current_state -= first_pick
    second_pick = selected(current_state, Z-1)
    current_state -= second_pick


def fitness(Z, A, k, invader, resident):
    '''
    The fitness function determines the average payoff of k
    invaders and N-k residents
    in the population of N players.
    '''
    resultA=(((k-1)*A[invader][invader])+
    ((Z-k)*A[invader, resident]))/float(Z-1)
    resultB=((k*A[resident][invader])+
    ((Z-k-1)*A[resident, resident]))/float(Z-1)
    return [resultA, resultB]

def selected(current_state, Z):
    selected = randint(0, Z)
    if selected <= current_state:
        current_state -= 1
        return 1 # TFT
    else:
        return 0 # Defector
    
def estimate_stationary_distribution(nb_runs, transitory, nb_generations, beta, mu, Z, A):
    res = 0
    for _ in range(nb_runs):
        state = randint(0, Z) # amount of TFT in population
        for i in range(transitory):
            state = moran_step(state, beta, mu, Z, A)
        for i in range(nb_generations-transitory):
            state = moran_step(state, beta, mu, Z, A)
            
    