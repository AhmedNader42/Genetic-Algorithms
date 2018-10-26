import random

# Input
def readInputFromFile() :
    f = open("myInput.txt", "r")
    of = open("myOutput.txt", "w+")

    if f.mode == "r":
        # Read all the lines from the file
        lines = f.readlines()

        # Filter out the \n, and replace with ''
        lines = map(lambda x:x.strip(), lines)

        # Get the number of test cases at first index
        testCases = int(lines[0])
        print "Number of test cases : " , testCases
        
        # Ignore the space at index 1 and start reveiving input at index 2
        index = 2

        for testCase in range(0, testCases, 1):
            print "Test Case : " , testCase+1

            # Number of items
            noOfItems = int(lines[index])
            print "Number of items " , noOfItems
            index += 1

            # Knapsack size
            knapsackSize = int(lines[index])
            print "Knapsack size " , knapsackSize
            index += 1

            items = []
            # Items
            for _ in range(0, noOfItems, 1):
                line = lines[index]
                items.append([line.split(" ")[0], line.split(" ")[1]])
                index += 1 
            # Put the call to Knapsack function here
            selectedItems = knapsack(knapsackSize, noOfItems, 10, 10, items)
            value = 0
            for each in selectedItems:
                value += each[1]
            print value, selectedItems
            of.write("Case ")
            of.write(str(testCase+1))
            of.write(": ")
            of.write(str(value))
            of.writelines("\n")
            of.write(str(len(selectedItems)))
            of.write("\n")
            for each in selectedItems:
                of.write(str(each[0]))
                of.write(" ")
                of.write(str(each[1]))
                of.write("\n")
            # Skip 2 spaces and start to read the next test case
            index += 2

    f.close()
    of.close()




def knapsack(maxWeight, numberOfItems, populationSize, maxGen, originalItems):
    # Array of chromosoms [[1,0,1], [0,0,1]]
    population = []
    items = originalItems
    
    # Generate random chromosoms and put them into the population.
    for _ in range(0, populationSize, 1):
        population.append([random.randint(0,1) for _ in xrange(numberOfItems)])

    bestChromosome = []
    bestChromosomeValue = 0
    for _ in range(0, maxGen, 1):

        populationFitness = []
        # Evaluate fitness of the population
        for chromosomeIndex in range(0, len(population), 1):

            # Current chromosome being evaluated
            chromosome = population[chromosomeIndex]
            chromosomeFitness = 0
            chromosomeWeight = 0

            for itemIndex in range(0, numberOfItems, 1):
                item = items[itemIndex]
                weight = int(item[0])
                value = int(item[1])
                itemState = int(chromosome[itemIndex]) # 1 selected, 0 not selected

                if chromosomeWeight + weight > maxWeight:
                    population[chromosomeIndex][itemIndex] = 0
                    itemState = 0
                
                chromosomeFitness += itemState * value
                chromosomeWeight += itemState * weight


                # print item, weight, value, itemState, chromosomeFitness

            populationFitness.append(chromosomeFitness)
        # print populationFitness

        totalFitness = sum(populationFitness)
        # print totalFitness
        for fitnessIndex in range(0, len(population), 1):
            populationFitness[fitnessIndex] = int(float(populationFitness[fitnessIndex]) / float(totalFitness) * 100)
            
        #print populationFitness


        # Selection
        populationRoullet = []
        for index in range(0, len(population), 1):
            probability = populationFitness[index]
            for _ in range(0, probability, 1):
                populationRoullet.append(population[index])

        

        # print population

        # Cross Over
        pXOver = 0.5
        pXOver2 = random.random()

        firstParentIndex = random.randint(0, len(populationRoullet)-1)
        p1 = populationRoullet[firstParentIndex]
        secondParentIndex = random.randint(0, len(populationRoullet)-1)
        p2 = populationRoullet[secondParentIndex]
        offspring1 = []
        offspring2 = []
        
        
        if pXOver2 >= pXOver :
            # Perform XOver
            xOverPoint = random.randint(0, len(p1)-1)
            # print "XOverpoint : ", xOverPoint
            offspring1.extend(p1[:xOverPoint])
            offspring1.extend(p2[xOverPoint:])

            offspring2.extend(p2[:xOverPoint])
            offspring2.extend(p1[xOverPoint:])
            # print "Parents : " , p1, p2
            # print "Offspring: " , offspring1, offspring2
            
            replacements = 0
            for each in range(0, len(population), 1):
                if replacements > 1:
                    break
                if population[each] == p1:
                    population[each] = offspring1
                    replacements += 1
                elif population[each] == p2:
                    population[each] = offspring2
                    replacements += 1
        else:
            offspring1 = p1
            offspring2 = p2
            # print "No XOver"




        # Mutation
        pMutation = 0.1
        for currentChromosomeIndex in range(0, len(population), 1):
            currentChromosome = population[currentChromosomeIndex]
            
            for currentGeneIndex in range(0,len(currentChromosome), 1):
                r = random.random()
                # print r
                if r < pMutation : 
                    # print "MUTATION : " , r
                    currentValue = currentChromosome[currentGeneIndex]
                    if currentValue == 1:
                        currentChromosome[currentGeneIndex] = 0
                    else :
                        currentChromosome[currentGeneIndex] = 1
    
        populationFitness = []
        for chromosomeIndex in range(0, len(population), 1):
            chromosome = population[chromosomeIndex]
            chromosomeFitness = 0
            chromosomeWeight = 0

            for itemIndex in range(0, numberOfItems, 1):
                item = items[itemIndex]
                weight = int(item[0])
                value = int(item[1])
                itemState = int(chromosome[itemIndex]) # 1 selected, 0 not selected

                if chromosomeWeight + weight > maxWeight:
                    population[chromosomeIndex][itemIndex] = 0
                    itemState = 0
                
                chromosomeFitness += itemState * value
                chromosomeWeight += itemState * weight
            populationFitness.append(chromosomeFitness)
            
        print populationFitness    
        for i in range(0, len(populationFitness),1):
            if populationFitness[i] > bestChromosomeValue:
                bestChromosomeValue = populationFitness[i]
                bestChromosome = population[i]
    
        # Replacemnet
        population = []

        # Generate random chromosoms and put them into the population.
        for _ in range(0, populationSize, 1):
            population.append([random.randint(0,1) for _ in xrange(numberOfItems)])

    
    
    outputList = []

    for geneIndex in range(0, len(bestChromosome), 1):
        item = items[geneIndex]
        weight = int(item[0])
        value = int(item[1])
        state = bestChromosome[geneIndex]
        if state == 1:
            outputList.append([weight, value])
    return outputList
    
    
# knapsack(35,5, 10, 10, [['10', '27'], ['9', '27'], ['8', '12'], ['8', '28'], ['3', '23']])





readInputFromFile()

