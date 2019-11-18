""" Authors: Hadleigh Schwartz and Katie Dykstra. This program creates a genetic
algorithm that presents the user with a valid equation that solves to 23 and
keeps producing generations based on fitnesses until a valid equation that
solves to 23 is produced.
"""

from __future__ import print_function
import random


def random_pop():
	"""Cretaes initial population of 20"""
	init_pop = []

	for i in range(20):
		genome = ""

		for j in range(0,9):
			rand = "{0:04b}".format(random.randint(0,13))[::-1]
			genome += rand

		init_pop.append(genome)

	return init_pop


def genome_to_operators(genome):
	"""Converts from binary to raw function"""
	indivgenome = ""
	y = 0

	for i in range(0,len(genome),4):
			y = int(int((genome[i:i + 4]),2))
			if y == 10:
				indivgenome += "+"

			elif y == 11:
				indivgenome += "-"

			elif y == 12:
				indivgenome += "*"

			elif y == 13:
				indivgenome += "/"

			elif y < 10:
				indivgenome += str(y)

	return indivgenome


def convert_to_valid(genome):
	"""Converts the raw functions to a valid expression"""
	try:
		
		valid_expression = ""
		counter = 0
		char_type = None
		prev_type = "operator"

		for x,character in enumerate(genome):
			if (genome[x] == "+" or genome[x] == "-" or genome[x] == "*"  
				or genome[x] == "/"):
				char_type = "operator"

			else:
				char_type = "operand"

			if prev_type != char_type:
				valid_expression += genome[x]

			prev_type = char_type

		"""Make sure last character is not an operator"""
		if (valid_expression[len(valid_expression) - 1] == "+" or valid_expression[len(valid_expression) - 1] == "-"
			or valid_expression[len(valid_expression) - 1] == "*" or 
			valid_expression[len(valid_expression) - 1] == "/"):
			valid_expression = valid_expression[0:-1]		

		return valid_expression

	except:
		return "fail"
	

def solve_valid(validexpression):
	"""Solves valid expression"""
	answer = 0

	if len(validexpression) == 0:
		return answer

	else:
		answer = float(validexpression[0:1])
		validexpression = validexpression[1:len(validexpression)]

	while len(validexpression) != 0:
		operator_operand_pair = validexpression[0:2]

		if operator_operand_pair == '/0':
			return 0

		validexpression = validexpression[2:len(validexpression)]
		answer = eval(str(answer) + operator_operand_pair)

	return answer


def test_fitness(numbers):
	"""Determines the fitness of each member of the population"""
	fitnesses = []

	for num in numbers:
		fitnesses.append(round(1.0/abs(23.0 - num),4))

	return fitnesses


def breeding_recombination(indices_two_mates, pop):
	"""Swaps bits of two mates and replaces them in the current population"""
	mate1 = list(pop[indices_two_mates[0]])
	mate2 = list(pop[indices_two_mates[1]])
	rate = .4
	randNumb = random.random()
	temp = ""

	for i in range(len(mate1)):

		if i % 2 == 0:
			temp = mate1[i]
			mate1[i] = mate2[i]
			mate2[i] = temp

	if randNumb < rate:
		location = random.randint(0, 8)
		
		for i in range(4):
			mate1[location*4 + i] = str(random.randint(0,1))
		
	mate2 = ''.join([str(item) for item in mate2])
	mate1 = ''.join([str(item) for item in mate1])

	bred = [mate2, mate1]

	return(bred)


def selection(fitnesses, pop):
	""" Selects two mates at a time based on passed in fitness values."""
	population = []
	values = fitnesses
	indices = list(range(len(fitnesses)))

	for k in range(10):
		mates = [0, 0]

		if len(values) == 2:
			mates[0] = indices[0]
			mates[1] = indices[1]
			
		elif len(values) == 0:
			break

		else:
			f = sum(values)
			p = f / 2.0
			start = random.random() * p
			index = 0
			fitness = values[index]
			
			for i in range(2):

				pointer = start + i * p
				if fitness >= pointer:
					
					if i == 1 and index != 0:
						mates[i] = indices[index - 1]
						del values[index - 1]
						del indices[index - 1]

					else:
						mates[i] = indices[index]
						del values[index]
						del indices[index]

				else:
					index += 1

					while index < len(values):
						fitness += values[index]

						if fitness >= pointer:
				
							if i == 1 and index != 0:
								mates[i] = indices[index - 1]
								del values[index - 1]
								del indices[index - 1]

							else:
								mates[i] = indices[index]
								del values[index]
								del indices[index]
							break
						index += 1
				
		bred = breeding_recombination(mates, pop)
		mate1 = bred[0]
		population.append(mate1)
		mate2 = bred[1]
		population.append(mate2)

	return population


def main():
	"""Executes the above functions"""
	init_pop = random_pop()
	currentpop = init_pop
	generation = 0
	check = 0

	while check == 0:
		pop_numbers = []

		for genome in currentpop:
			tooperators = genome_to_operators(genome)
			print ("Raw function " + tooperators)
			valid = convert_to_valid(tooperators)
			
			if valid == "fail":
				new_genome = ""

				for j in range(0,9):
					rand = "{0:04b}".format(random.randint(0,13))[::-1]
					new_genome += rand

				genome = new_genome
				tooperators = genome_to_operators(genome)
				print ("Raw function " + tooperators)
				valid = convert_to_valid(tooperators)

			print("Corrected: " + valid)
			solved = solve_valid(valid)
			print("Solved: " + str(solved))
			pop_numbers.append(solved)

			if solved == 23:
				print("DONE on Generation " + str(generation))
				check = 1
				return

			print("Generation " + str(generation))

		fitnesses = test_fitness(pop_numbers)
		newpop = selection(fitnesses, currentpop)
		currentpop = newpop
		generation += 1


main()



