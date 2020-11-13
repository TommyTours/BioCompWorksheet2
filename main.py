import evolution
import matplotlib.pyplot as plt
import numpy as np

#def get_best_and_mean(population):


def new_generation(population):

    offspring = []

    population = evolution.crossover(population)

    evolution.individual_fitness(population)

    population_fitness = evolution.population_fitness(population)

    # print("Fitness after crossover: " + str(population_fitness))

    population = evolution.mutation(population, 0.02)

    evolution.individual_fitness(population)

    population_fitness = evolution.population_fitness(population)

    # print("Fitness after mutation: " + str(population_fitness))

    offspring = evolution.tournament_selection(population)

    population_fitness = evolution.population_fitness(offspring)

    print("Fitness after selection of new generation: " + str(population_fitness[0]))

    return offspring


population = evolution.init_population(50, 50)

evolution.individual_fitness(population)

population_fitness = evolution.population_fitness(population)

print("Initial population fitness: " + str(population_fitness[0]))

population = evolution.tournament_selection(population)

population_fitness = evolution.population_fitness(population)

print("Fitness after selection: " + str(population_fitness[0]))

best_and_mean = [[], []]

for x in range(0, 200):
    population = new_generation(population)
    fitness = evolution.population_fitness(population)
    best_and_mean[0].append(fitness[1])
    best_and_mean[1].append(fitness[2])

plt.plot(best_and_mean[0])
plt.plot(best_and_mean[1])
plt.ylabel('Fitness')
plt.xlabel('Generation')
plt.legend(['Best', 'Mean'])
plt.show()

print("hah")