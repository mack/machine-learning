from population import *

def main():
    # make use of dna and population
    pop = Population("My name is jarret", 0.01, 200)

    for j in range(1000):
        pop.calculate_fitness()
        pop.create_offspring()
        if (j % 100 == 0):
            print(pop.get_best().data)


if __name__ == '__main__':
    main()
