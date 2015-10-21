from random import choice
from tkinter import Tk
import subprocess

# The goal of this module is to print 3 random restaurants from a text file.

# Create empty list
restList = []

# Open restList.txt
restFile = open('restList.txt')

# Loop through restList.txt and add to restList
for line in restFile:
	restList.append(line)
	# Each entry has '\n' appended to it still. 

#Close restList.txt
restFile.close()

stringList = ''
printList = []

y = input('# of restaurants to display?')
x = 0 

while x < int(y):
	# Select random element from restList
	rest = choice(restList)
	if rest not in printList:
		x += 1
		# Adjustment for resturant at end of file
		if '\n' not in rest:
			rest += '\n'
		printList.append(rest)
		stringList += rest

# Print restuarants
print(stringList)


# To Do:
	#GUI
	#Reroll
		#don't include last places.