import random
import numpy as np
from deap import base, creator, tools, algorithms

# Setup
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("attr", random.random)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr, n=5)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Evaluation: minimize sum
toolbox.register("evaluate", lambda ind: (sum(ind),))
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    pop = toolbox.population(n=100)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values[0])
    stats.register("min", np.min)

    algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=20, stats=stats, halloffame=hof, verbose=False)
    print("Best:", hof[0], "Fitness:", hof[0].fitness.values[0])

if __name__ == "__main__":
    main()



import random 
import numpy as np
from deap import base, creator, tools, algorithms

creator.create("FitnessMin", base.Fitness,weights = (-1.0,))
creator.create("Individual", list, fitness = creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register()
# import random
# import numpy as np
# from deap import base, creator, tools, algorithms

# # Step 1: Define the Fitness and Individual Classes
# creator.create("FitnessMin", base.Fitness, weights=(-1.0,))  # Minimize fitness
# creator.create("Individual", list, fitness=creator.FitnessMin)

# # Step 2: Initialize the Toolbox
# toolbox = base.Toolbox()
# toolbox.register("attr_float", random.random)  # Float in [0.0, 1.0)
# toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=5)
# toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# # Step 3: Define the Evaluation Function
# def evalOneMax(individual):
#     return sum(individual),  # Must return a tuple

# # Step 4: Register the Evaluation Function with the Toolbox
# toolbox.register("evaluate", evalOneMax)

# # Step 5: Define the Operators
# toolbox.register("mate", tools.cxTwoPoint)                      # Crossover
# toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)        # Mutation
# toolbox.register("select", tools.selTournament, tournsize=3)    # Selection

# # Step 6: Define the Main Loop of the Evolutionary Algorithm
# def main():
#     pop = toolbox.population(n=300)  # Population of 300 individuals
#     hof = tools.HallOfFame(1)        # Keep track of the best individual

#     stats = tools.Statistics(lambda ind: ind.fitness.values)
#     stats.register("avg", np.mean)
#     stats.register("std", np.std)
#     stats.register("min", np.min)
#     stats.register("max", np.max)

#     # Evolutionary algorithm execution
#     pop, log = algorithms.eaSimple(pop, toolbox,
#                                    cxpb=0.5,      # Crossover probability
#                                    mutpb=0.2,     # Mutation probability
#                                    ngen=40,       # Number of generations
#                                    stats=stats,
#                                    halloffame=hof,
#                                    verbose=True)

#     return pop, log, hof

# # Step 7: Run the Algorithm
# if __name__ == "__main__":
#     pop, log, hof = main()
#     print("Best individual is: %s\nwith fitness: %s" % (hof[0], hof[0].fitness.values))
