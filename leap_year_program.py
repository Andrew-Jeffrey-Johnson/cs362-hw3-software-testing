###############################################################################
# This file is designed to be run on the OSU FLIP servers. 
# To run the program, enter in the command below into the FLIP servers.
#	python3 hw1.py
###############################################################################

# returns true if the given year is a leap year
def is_leap_year (year):
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				return True;
			else:
				return False
		else:
			return True
	else:
		return False

# create a variable to hold the integer year
year = 0

# loop until valid input is given
valid = False
while not valid:
	# request input
	print("Please enter a year: ")
	
	# take input from
	input_year = input()

	# take input from
	try:
		# cast into an integer
		year = int(input_year)
		valid = True
	except ValueError:
		# print error report
		print('ERROR: Input is not a valid year. Please only enter valid years.')

# produce output
if is_leap_year (year):
	print(str(year) + " is a leap year")
else:
	print(str(year) + " is not a leap year")
	
	
