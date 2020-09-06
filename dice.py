from random import *
min = 1
max = 6

again = "yes"

while again == "yes" or again == "y":
	print ("...")
	print ("Dice1:")
	print (random.randint(min, max))
	print ("Dice2:")
	print (random.randint(min, max))
	
	again = input("Repeat?")

	
