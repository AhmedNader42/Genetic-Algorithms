import random

def readFromFile():
        f = open("input.txt", "r")
        of = open("myOutput.txt", "w+")

        if f.mode == "r":
                lines = f.readlines()
                lines = map(lambda x:x.strip(), lines)	
                testCases = int(lines[0])
                # print "Number of test Cases : " , testCases
                # print(lines)
                points = []
                index = 1
                for testCase in range(0, testCases, 1):
                        l = lines[index].split(" ")
                        numberOfPoints = int(l[0])	
                        # print "Number Of : " , numberOfPoints
                        degreeOfEquation = int(l[1])
                        # print "Degree of Equation : ", degreeOfEquation
                        index += 1
			for i in range(0, numberOfPoints, 1):
                                line = lines[index]
                                # print(line)
                                index += 1
                                points.append([float(line.split(" ")[0]), float(line.split(" ")[1])])
                        (value, chromosome) = CurveFitting(points, degreeOfEquation, numberOfPoints, 1000, 100)
                        print value, chromosome
                        of.write("Case ")
                        of.write(str(testCase+1))
                        of.write("\n")
                        for each in chromosome:
                                of.write(str(each))
                                of.write(" ")
                                of.write("\n")
                        of.write("Error : ")
                        of.write(str(value))
                        of.write("\n")

        f.close()
        of.close()
        	
		
def MSE(points, chromosome, degree):
	errorSum = 0
	for point in points:
		yCalc = 0 
		x = point[0]
		yActual = point[1]
		for d in range(0, degree+1, 1):
			yCalc += chromosome[d] * x**d
		errorSum += (yCalc - yActual)**2
	return 1/float(len(points)) * errorSum	



def CurveFitting(points, degree, numberOfPoints, populationSize, numberOfGenerations):

        minimumValue = 10000000000000000000000000000000000000000000.0
        bestChromosome = []
        for currentGeneration in range(0, numberOfGenerations, 1):
                population = []
                # Generate random chromosoms and put them into the population.
                for _ in range(0, populationSize, 1):
                        population.append([random.uniform(-10,10) for _ in xrange(degree+1)])
                
                # Selection	
                populationFitness = []
                for i in range(0, populationSize, 1):
                        populationFitness.append(MSE(points, population[i], degree))	

                # print min(populationFitness)

                # Cross Over
                pXOver = 0.5
                pXOver2 = random.random()

                firstParentIndex = random.randint(0, len(population)-1)
                p1 = population[firstParentIndex]
                secondParentIndex = random.randint(0, len(population)-1)
                p2 = population[secondParentIndex]
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
                        #     print "Parents : " , p1, p2
                        #     print "Offspring: " , offspring1, offspring2
                
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
                        #     print "No XOver"


                
                # Mutation
                for currentChromosomeIndex in range(0, len(population), 1):
                        currentChromosome = population[currentChromosomeIndex]
                        b = 0.5

                        for currentGeneIndex in range(0,len(currentChromosome), 1):
                                delta = 0
                                rPrime = random.random()
                                r = random.random()

                                if rPrime <= 0.5 : 
                                        delta = -10.0 * (1 - r ** (1-currentGeneration/numberOfGenerations)**b)
                                        if (currentChromosome[currentGeneIndex] + delta) <= 10.0 and (currentChromosome[currentGeneIndex] + delta) >= -10.0:
                                                currentChromosome[currentGeneIndex] += delta  
       
                                else :
                                        delta = 10.0 * (1 - r ** (1-currentGeneration/numberOfGenerations)**b)
                                        

                                        if (currentChromosome[currentGeneIndex] - delta) >= -10.0 and (currentChromosome[currentGeneIndex] - delta) <= 10.0:
                                                currentChromosome[currentGeneIndex] -= delta


                for i in range(0, populationSize, 1):
                        minimum = MSE(points, population[i], degree)
                        if minimum < minimumValue:
                                minimumValue = minimum
                                bestChromosome = population[i]        

        return minimumValue, bestChromosome  
                
                




			
readFromFile()



		

#print(MSE([[2, 8], [3, 27], [4, 64]], [0, 0, 0, 1], 3))












	

