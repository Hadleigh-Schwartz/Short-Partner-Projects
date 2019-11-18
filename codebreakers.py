""" Authors: Katie Dykstra and Hadleigh Schwartz
This file contains code for a game named Code Breakers. 
This game provides the user with a 5x5 board of words and then gives the user a 
hint that connects multiple words, followed by the number of words the hint
connects (ex: Halloween - 3). The user inputs their guesses and then a new board
is generated with smiley faces in the place of correctly guessed words.
"""

from __future__ import print_function

#global variable
words = ["Beijing", "Corn", "India", "Bottle", "Himalayas","Air", "Fire"
            , "Calf", "Lemon", "Suit", "Spells", "Club", "Bird", "Boil",
            "Olive", "Car", "Log ", "Net", "Wall", "Ghosts", "Mount",
            "Fry", "Bat", "Toast", "Vietnam"]

def instructions():
    print("You will be given a 5x5 board of words and then I will give you a\n"\
    		"hint that connects multiple words, followed by the number of words\n"\
    		"the hint connects (ex: Halloween - 3). To exit the game at any time type QUIT\n")
    userInput = raw_input("Please type c to continue or q to quit: ")
    if userInput == "c":
    	set_board()
    elif userInput == "q":
    	print("You have chosen to exit the game.")
    	exit()
    elif userInput != "q" and userInput != "c":
    	print("You have typed the wrong letter, the game will now quit.")
    	exit()

#dashed line
def line():
    print ("\n________________________________________________________________")

#sets board
def set_board():
    i = 0
    counter = 0
    while i < 5:
        j = 0
        while j < 5:
            print( words[counter] + " | ", end = " | ")
            counter += 1
            j += 1
        line()
        i += 1

#provides hint
def givehint(answerkey):
	x = " "
	for i in range(len(answerkey)):
		#gives hint
		for j in range(len(answerkey)):
			if j == len(answerkey[i]) - 1:
				print("Your hint: " + answerkey[i][0] + " - " + str(j))
				for f in range(len(answerkey[i]) - 1):
					x = raw_input("Answer " + str(f + 1) + "(as spelled on board) ")
					if x in answerkey[i]:
						for h in range(len(words)):
							if words[h] == x:
						   		words[h] += ":)"
					elif x == "QUIT":
						exit()
					elif j == 0 or x != answerkey[i][j]:
						x = raw_input("You've guessed incorrectly, please try again ")
		for k in range(len(answerkey[i])):
			correct = len(answerkey[i]) - 1
			counter = 0
			if counter == correct:
				print("Your hint: " + answerkey[i][0] + " - " + str(j))
				for f in range(len(answerkey[i]) - 1):
					x = raw_input("Answer " + str(f + 1) + "(as spelled on board) ")
					if x == "QUIT":
						exit()	
					elif f == 0 or x != answerkey[i][f]:
						x = raw_input("You've guessed incorrectly, please try again ")
			elif counter != correct:
				if x in answerkey[i]:
					for d in range(len(words)):
							if words[d] == x:
						   		words[d] += ":)"
					counter += 1
					continue
				elif k == 0 or x != answerkey[i][k]:
					x = raw_input("You've guessed incorrectly, please try again ")
					for e in range(len(words)):
						if words[e] == x:
						   	words[e] += ":)"
					if x == "QUIT":
						exit()
					else:
						continue
		print("\n\n")
		set_board()
		if i == len(answerkey) - 1:
			print("You have completed the game!!Congrats:)")

instructions()
answerkey1 = [["Mexico","Corn","Wall"],["Poker","Club","Suit"],["French","Fry", "Toast", "Vietnam"],
				["Halloween","Spells","Ghosts","Bat"],["Badminton","Beijing","Bird","Net"],
				["Forest","Fire","Olive","Lemon","Log"],["Altitude","Mount","Boil"],
				["Hindu","Himalayas","Calf", "India"],["Pollution","Air","Bottle","Car"]]
givehint(answerkey1)
