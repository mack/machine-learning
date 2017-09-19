from dna import *

class Population(object):
    def __init__(self, target, mutation_rate, max_pop):
        self.target = target
        self.mutation_rate = mutation_rate
        self.max_pop = max_pop
        self.population = []
        self.buildPopulation()

    def buildPopulation(self):
        for i in range(self.max_pop):
            chromosome = DNA(len(self.target))
            self.population.append(chromosome)

    def calculate_fitness(self):
        self.score_total = 0
        for i in range(len(self.population)):
            self.score_total += self.population[i].rate(self.target)
        self.score_total /= len(self.population)
