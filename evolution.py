import random
import copy


class Individual:  # Class to represent Individuals within the population
    gene = []  # List of binary values
    fitness = 0


def init_population(number_of_genes, population_size):  # Creates initial population
    population = []

    for x in range(0, population_size):  # for specified population size
        tempGene = []
        for y in range(0, number_of_genes):  # for each gene in individual, randomly set zero or one
            tempGene.append(random.randint(0, 1))
        newInd = Individual()
        newInd.gene = tempGene.copy()
        population.append(newInd)  # add new individual to population

    return population


def tournament_selection(population):  # choose fitter individual to pass on their genes to the next generation
    offspring = []
    population_size = len(population)

    for i in range(0, population_size):  # for specified population size
        parent1 = random.randint(0, population_size - 1)
        off1 = population[parent1]
        parent2 = random.randint(0, population_size - 1)
        off2 = population[parent2]  # choose 2 random individuals from the population
        if off1.fitness > off2.fitness:
            offspring.append(copy.deepcopy(off1))
        else:
            offspring.append(copy.deepcopy(off2))  # add the fitter of the two to the new population

    return offspring


def individual_fitness(population):   # calculates and sets the fitness value of an individual
    population_size = len(population)

    for x in range(0, population_size):  # for each individual in the population, set fitness to the number of ones
        population[x].fitness = sum(int(gene) for gene in population[x].gene)


def population_fitness(population):  # Calculate total fitness of population
    total_fitness = 0
    best = 0
    population_size = len(population)

    for x in range(0, population_size):  # for each individual in population, add it's fitness to total fitness
        if population[x].fitness > best:
            best = population[x].fitness
        total_fitness += population[x].fitness

    total_best_mean = [total_fitness, best, total_fitness/population_size]

    return total_best_mean


def swap_tails(first, second, crosspoint):  # swaps the tails of first and individual from specified crosspoint onwards

    temp_individual = copy.deepcopy(first)  # temporary copy of individual 1 to facilitate this process
    for y in range(crosspoint, len(first.gene)):
        first.gene[y] = second.gene[y]
        second.gene[y] = temp_individual.gene[y]  # uses value from temp and first has already been changed


def crossover(population):  # performs crossover on each pair of individuals
    population_size = len(population)

    number_of_genes = len(population[0].gene)
    for x in range(0, population_size, 2):
        crosspoint = random.randint(0, number_of_genes - 1)  # picks a random crosspoint in the gene
        swap_tails(population[x], population[+1], crosspoint)
        population[x].fitness = 0
        population[x+1].fitness = 0  # resets fitness value as crossover has modified it.

    return population


def mutation(population, mutation_rate):
    offspring = []
    population_size = len(population)

    number_of_genes = len(population[0].gene)
    for x in range(0, population_size):
        new_individual = Individual()
        new_individual.gene = []
        for y in range(0, number_of_genes):
            gene = population[x].gene[y]
            mutation_probability = random.randint(0, 100)
            if mutation_probability < (100 * mutation_rate):
                if gene == 1:
                    gene = 0
                else:
                    gene = 1
            new_individual.gene.append(gene)

        offspring.append(new_individual)

    return offspring
