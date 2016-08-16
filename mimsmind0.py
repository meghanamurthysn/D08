#!/usr/bin/env python3
##############################################################################################################################
# Imports
import random
import sys

# Body

# Generate a random integer of the specified length or default = 1
def get_randint(length):
	n = random.randint(10**(length - 1), (10**length) - 1)
	return n

def mimsmind0(rand_int, length):
	count = 0
	try:
		guess = int(input("Guess a {} - digit number: ".format(length)))
	except ValueError:
		print("Please enter only integers")
	while(True):
		# Correct guess
		if guess == rand_int:
			count += 1
			print("Congratulations. You guessed the correct number in {} tries.".format(count))
			break
		# Lower value
		elif guess < rand_int:
			try:
				guess = int(input("Try again. Guess a higher number: "))
			except ValueError:
				print("Please enter only integers for length")
			count += 1
		# Higher value
		elif guess > rand_int:
			try:
				guess = int(input("Try again. Guess a lower number: "))
			except ValueError:
				print("Please enter only integers for length")
			count += 1
		# Incorrect length of digits
		elif len(guess) != length:
			print("The input must be {} - digits long".format(length))
			count += 1
##############################################################################################################################
def main():
	try:
		length = int(sys.argv[1])
	except ValueError:
		print("Length must be an integer")
	except IndexError:
		length = 1
	rand_int = get_randint(length)
	mimsmind0(rand_int, length)

if __name__ == '__main__':
	main()