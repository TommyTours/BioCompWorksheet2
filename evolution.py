import random


class Individual:
    gene = []
    fitness = 0


def init_population(number_of_genes, population_size):
    population = []

    for x in range(0, population_size):
        tempGene = []
        for y in range(0, number_of_genes):
            tempGene.append(random.randint(0, 1))
        newInd = Individual()
        newInd.gene = tempGene.copy()
        population.append(newInd)

        return population
