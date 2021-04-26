###############################################################################
# This file is designed to be run on the OSU FLIP servers. 
# To run the program, enter in the command below into the FLIP servers.
#	python3 hw1.py
###############################################################################
# request input
print("Please enter a year: ")

# take input from
input_year = input()

# cast into an integer
year = int(input_year)

# determine leap year
if year % 4 == 0:
	if year % 100 == 0:
		if year % 400 == 0:
			print(str(year) + " is a leap year")
		else:
			print(str(year) + " is not a leap year")
	else:
		print(str(year) + " is a leap year")	
else:
	print(str(year) + " is not a leap year")
