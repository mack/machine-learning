from population import *

def main():
    # make use of dna and population
    pop = Population("ithinkgabbyisbeautiful", 0.01, 200)
    j = 0
    while(True):
        pop.calculate_fitness();
        pop.create_offspring()
        if(pop.get_best().data == list(pop.target)):
            break;
        if (j % 25):
            print(pop.get_best().data)
        j += 1

    print("It took " + str(j) + "generations to get the string")




if __name__ == '__main__':
    main()
