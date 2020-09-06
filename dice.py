from random import *
min = 1
max = 6

again = "yes"

while again == "yes" or again == "y":
	print "..."
	print "Würfel1:"
	print random.randint(min, max)
	print "Würfel2:"
	print random.randint(min, max)
	
	again = raw_input("Repeat?")

	