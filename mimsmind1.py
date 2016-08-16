#!/usr/bin/env python3
# mimsmind1.py
##############################################################################################################################
# Imports
import random
import sys

# Body

# Generate a random integer with digits equal to length
def get_randint(length):
	n = random.randint(10**(length - 1), (10**length) - 1)
	return n

# Convert str to list
def make_list(str):
	lst = [item for item in str]
	return lst

# Function to count number of bulls
def get_bulls(guess_lst, rand_lst, length):
	bull_count = 0
	bull_idx = []
	for idx in range(length):
		if guess_lst[idx] == rand_lst[idx]:
			bull_idx.append(idx)
			bull_count += 1
	return bull_count, bull_idx

# Remove the bulls
def remove_bull(num_lst, idx):
	for i in idx:
		num_lst[i] = ''
	return num_lst

def distinct(lst):
	dist_lst = []
	for i in range(len(lst)):
		if lst[i] not in dist_lst:
			dist_lst += lst[i]
	return dist_lst

def get_cows(guess_no_bull, rand_no_bull, length):
	distinct_guess_no_bull = distinct(guess_no_bull)
	for item in distinct_guess_no_bull:
		guess_cows = guess_no_bull.count(item)
		rand_cows = rand_no_bull.count(item)
		cow_count = min(guess_cows, rand_cows)
	return cow_count

def mimsmind1(rand_int, length):
	total_guess = (length**2) + (length - 1)
	user_guess = 0
	welcome_msg = "Let's play the mimsmind1 game. You have {} guesses.".format(total_guess)
	prompt = 'Guess a {} digit number: '.format(length)
	print (welcome_msg + "\n" + prompt, end=' ')
	try:
		guess = input(": ")
		guess_int = int(guess)
	except ValueError:
		print("Please enter only integers")
	while total_guess:
		# Correct guess
		if guess == rand_int:
			user_guess += 1
			total_guess -= user_guess
			print("Congratulations. You guessed the correct number in {} tries.".format(user_guess))
			break
		# Incorrect length of digits
		elif len(guess) != length:
			print("The input must be {} - digits long".format(length))
			user_guess += 1
			total_guess -= user_guess
		# Bulls and Cows
		else:
			guess_lst = make_list(guess)
			rand_lst = make_list(str(rand_int))
			bulls = get_bulls(guess_lst, rand_lst, length)
			num_bulls = bulls[0]
			bull_index = bulls[1]
			guess_no_bull = remove_bull(guess_lst, bull_index)
			rand_no_bull = remove_bull(rand_lst, bull_index)
			num_cows = get_cows(guess_no_bull, rand_no_bull, length)
			user_guess += 1
			total_guess -= user_guess
			print("{} bull(s), {} cow(s). Try again: ".format(num_bulls, num_cows))
	else:
		print("Sorry, you ran out of guesses.")
########################################################################################################################
def main():
	try:
		length = int(sys.argv[1])
	except ValueError:
		print("Length must be an integer")
	except IndexError:
		length = 3
	rand_int = get_randint(length)
	mimsmind1(rand_int, length)

if __name__ == '__main__':
	main()