from population import *

def main():
    # make use of dna and population
    pop = Population("jarrettheg", 0.01, 200)

    for j in range(1000):
        if (j % 25):
            print(pop.get_best().data)
        if(pop.calculate_fitness() == len(pop.target)):
            j = 2000
        pop.create_offspring()
    print(pop.get_best().data)



if __name__ == '__main__':
    main()
