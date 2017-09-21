from dna import *
import random

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
        # calculate score total
        for i in range(len(self.population)):
            self.score_total += self.population[i].rate(self.target)
        self.normalize() # normalize each score
        return self.score_total

    def normalize(self):
        # normalization
        for i in range(len(self.population)):
            self.population[i].score /= self.score_total

    def get_best(self):
        best = self.population[0]
        for i in range(1, len(self.population)):
            if (best.score < self.population[i].score):
                best = self.population[i]
        return best

    def create_offspring(self):
        for i in range(len(self.population)):
            parentA = self.select_random()
            parentB = self.select_random()
            child = self.perform_crossover(parentA, parentB)
            self.population[i] = child

    def perform_crossover(self, parentA, parentB):
        split_idx = random.randint(1, len(parentA.data) - 1)
        child = DNA(len(self.target))
        child.data[:split_idx] = parentA.data[:split_idx]
        child.data[split_idx:] = parentB.data[split_idx:]

    """ select_random()
    Returns a random element based on its
    cooresponding score (or probability)
    Args:
        N/A
    Returns:
        DNA: The randomly selected by weight, element
    """
    def select_random(self):
        r = random.random()
        upto = 0
        for i in range(len(self.population)):
            if upto + self.population[i].score >= r:
                return self.population[i]
            upto += self.population[i].score
