from time import time as t
from random import randint
from itertools import combinations

NUMBER_OF_ITERATIONS_IN_SIMULATION = 500000

def prod(ite):
	# returns the product of an iter, like the product of a list.
	ans = 1
	for elem in ite:
		ans *= elem
	return ans

def getE_simulation(n,amount=NUMBER_OF_ITERATIONS_IN_SIMULATION):
	lis = []
	for a in range(1,amount):
		curr = 0 #0=River Left   N+1=River Right
		count = 0
		while (curr<n):
			count += 1
			curr = randint(curr+1,n)
		lis.append(count)
	return(sum(lis)/a)

def getE_direct(n):
	ans = 0
	for a in range(1,n+1):
		ans += a * massProb(a,n)
	return ans

def massProb(x,n):
	exceptions = combinations(range(1,n),n-x)
	ans = 0
	rangeSet = set(range(1,n+1))
	for exc in exceptions:
		ans += 1/prod(rangeSet - set(exc))
	return ans

def compareUpTo(n):
	"""Shows results of expectancy, once by simulating it and other by the direct calculation, from 2 up to and including"""
	for i in range(2,n+1):
		print_direct(i)
		print_Simul(i)
		print()

def print_direct(i):
	start = t()
	print("     Real_Expectancy({}) = {}\t\tCalculation Time: {}s".format(i,round(getE_direct(i),5),round(t()-start,3)),flush=True)

def print_Simul(i):
	start = t()
	print("Simulated_Expectancy({}) = {}\t\tCalculation Time: {}s".format(i,round(getE_simulation(i),5),round(t()-start,3)),flush=True)

def startMenu():
	print("1: Basic showcase (Simulation and Direct up to 15 with {} iterations).".format(NUMBER_OF_ITERATIONS_IN_SIMULATION))
	print("2: Custom showcase (Simulation and Direct Calculation)")
	print("3: Direct Calc Rundown (from 1 to n)")
	print("4: Simulation Rundown (from 1 to n)")
	print("5: Direct")
	inp = int(input("Input: "))

	if (inp==1):
		compareUpTo(15)

	elif (inp==2):
		inp = int(input("Expectancy(n)\t\twith n= "))
		print_direct(inp)
		print_Simul(inp)
		print("\n")

	elif (inp==3):
		n = int(input("n: "))
		for i in range(2,n+1):
			print_direct(i)

	elif (inp==4):
		n = int(input("n: "))
		for i in range(2,n+1):
			print_Simul(i)

	elif (inp==5):
		inp = int(input("Expectancy(n)\t\twith n= "))
		print_direct(inp)

	else:
		startMenu()

startMenu()