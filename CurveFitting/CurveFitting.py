import random
def readFromFile():
        f = open("input.txt", "r")

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
                        CurveFitting(points, degreeOfEquation, numberOfPoints, 10)
        	
		
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



def CurveFitting(points, degree, numberOfPoints, populationSize):
        population = []
        # Generate random chromosoms and put them into the population.
        for _ in range(0, populationSize, 1):
                population.append([random.uniform(-10,10) for _ in xrange(degree+1)])
	
	# Selection	
	populationFitness = []
	for i in range(0, populationSize, 1):
		populationFitness.append(MSE(points, population[i], degree))	
	
	min = populationFitness[0]						
	for i in range(0, len(populationFitness), 1) :
		if populationFitness[i] < min:
			min = populationFitness[i] 
	

			
readFromFile()




		

#print(MSE([[2, 8], [3, 27], [4, 64]], [0, 0, 0, 1], 3))












	

