import evolution

def new_generation(population):



    population = evolution.crossover(population)

    evolution.individual_fitness(population)

    population_fitness = evolution.population_fitness(population)

    # print("Fitness after crossover: " + str(population_fitness))

    population = evolution.mutation(population, 0.02)

    evolution.individual_fitness(population)

    population_fitness = evolution.population_fitness(population)

    # print("Fitness after mutation: " + str(population_fitness))

    population = evolution.tournament_selection(population)

    population_fitness = evolution.population_fitness(population)

    print("Fitness after selection of new generation: " + str(population_fitness))

    return population


population = evolution.init_population(10, 50)

evolution.individual_fitness(population)

population_fitness = evolution.population_fitness(population)

print("Initial population fitness: " + str(population_fitness))

population = evolution.tournament_selection(population)

population_fitness = evolution.population_fitness(population)

print("Fitness after selection: " + str(population_fitness))

for x in range(0, 5):
    population = new_generation(population)

