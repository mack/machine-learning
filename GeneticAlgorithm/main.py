from population import *

def main():
    # make use of dna and population
    pop = Population("Mack", 0.01, 200)
    pop.calculate_fitness()

if __name__ == '__main__':
    main()
