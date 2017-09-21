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
        for i in range(len(self.population)):
            if (self.population[i].rate(self.target) > 2):
                print(self.population[i].rate(self.target))
                print(self.population[i].data)
                print("what")
            self.score_total += self.population[i].rate(self.target)
        self.normalize()
        print(self.score_total)
        return self.score_total

    def normalize(self):
        for i in range(len(self.population)):
            self.population[i].score /= self.score_total

    def create_offspring(self):
        return self.select_random()

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
