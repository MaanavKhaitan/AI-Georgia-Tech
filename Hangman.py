import numpy as np
import os
from numpy import loadtxt

# Import list of words 
#f = open('4000-most-common-english-words-csv.csv', 'r')
#word_list = loadtxt("4000-most-common-english-words-csv.csv", dtype='string', comments="\\r\\n", unpack=False)

word_list = ['orange', 'peel', 'lanyard', 'gentleman', 'wedding', 'console', 'lambda', 'dimension', 'alpha', 'stick', 'hockey', 'spread']

# Create empty list to be filled by user's guesses
user_guesses = []

# Determines inclusion of second player in game
second_player = False


def ask_user_letter(guesses_list):
# Asks user for and returns a letter guess
	user_letter = raw_input('Please enter a letter: ')

	# Check is user's guess is a single letter
	if len(user_letter) != 1 or type(user_letter) != str:
		print 'Guess must be one letter long.'
		user_letter = ask_user_letter(guesses_list)

	# Check if user's guess has already been guessed
	if user_letter in guesses_list:
		print 'You already typed the letter %s!' % (user_letter)
		user_letter = ask_user_letter(guesses_list)

	return user_letter.lower()


def print_initial_progress(word):
# Prints initial dashes based on length of word
	initial_progress = '_'

	# Returns ' _' for each character in word
	for i in range(0,len(word)-1):
		initial_progress += ' _'

	return initial_progress


def print_progress(letter, indices, progress):
# Prints progress of user at every turn
	final_progress = ''

	# If guess at first index, return guess + rest of progress
	if indices==[0]:
		final_progress += letter + progress[1:]
	# If guess appears more than once in word, replace all instances in final_progress with guess
	elif len(str(indices)) > 1:
		temporary_progress = progress
		for index in indices:
			temporary_progress = print_progress(letter,index,temporary_progress)
		final_progress = temporary_progress
	# Replace respective underscore in final_progress with guess
	else:
		later_index = ((indices+1)*2-2)
		final_progress += progress[0:((indices+1)*2-2)] + letter + progress[later_index+1:]
	final_progress = final_progress
	return final_progress 


def find_indices(word, letter):
# Returns all indices in word where letter appears
    return [i for i, ltr in enumerate(word) if ltr == letter]


def ask_second_player_for_word():
# Asks first player to provide a word for second player to guess
	second_player_word = raw_input('Player 1, please provide a word for player 2 to guess: ')
	return second_player_word.lower()


def play_hangman():
# Main function that makes user play the entire game of Hangman
	print 'Welcome to the wonderful game of Hangman!'
	wrong_guess_count = 0
	second_player = raw_input('How many players are playing today? (1/2)')

	# If second player is there, ask player 1 for word and move the gameplay downwards
	if second_player=='2':
		word = ask_second_player_for_word()
		for i in range(0,100):
			print " \n"
		print 'Now please hand the device to Player 2 and enjoy the game: '
	# If only one player, obtain random word
	else:
		word = np.random.choice(word_list).lower()

	user_guesses = []
	user_progress = print_initial_progress(word)
	complete_guess = ''

	# Loop over a  number that will be greater than user's possible guesses; at each iteration user provides new guess
	for i in range(0,100):

		# Print current status of hangman and guessed word
		print_hangman(wrong_guess_count)
		print user_progress

		user_guess = ask_user_letter(user_guesses)

		# If letter not guessed before, add it to list of guessed letters
		if user_guess not in user_guesses:
			user_guesses.append(user_guess)

		# If word has guess, update guessed word and add guess to string of correct user guesses		
		if user_guess in word:
			user_progress = print_progress(user_guess, find_indices(word,user_guess), user_progress)
			complete_guess += user_guess*len(find_indices(word,user_guess))
			print 'Yay! %s is in the word!'%(user_guess) # Inform user of correct guess

			# If correct guesses length = word length and correct guesses and word contain same unique characters
			if len(''.join(set(complete_guess))) == len(''.join(set(word))) and sorted(''.join(set(complete_guess))) == sorted(''.join(set(word))):
				print_hangman(wrong_guess_count)
				print user_progress
				print 'Congratulations! The word was %s!' % (word) # Inform user of win

				#Check if user wants to play again
				user_again_choice = raw_input('Would you like to play again? (y/n)')
				if user_again_choice=='y':
					print 'We\'re glad to hear that!'
					play_hangman() # Play full game again
				elif user_again_choice=='n':
					print 'Well we hope you enjoyed your game of Hangman today!' # Say goodbye to user
				break

		# Increment number of wrong guesses by 1, and inform user of guess failure
		else:
			wrong_guess_count += 1
			print '%s is not in the word.'%(user_guess)

		#If user guessed wrong six times
		if wrong_guess_count==6:
			print_hangman(wrong_guess_count)
			print user_progress
			print 'Sorry, game over! The word was %s.'%(word)

			# Ask user to play again
			user_again_choice = raw_input('Would you like to play and try your luck again? (y/n)')
			if user_again_choice=='y':
				print 'We\'re glad to hear that!'
				play_hangman()
			elif user_again_choice=='n':
				print 'Well we hope you enjoyed your game of Hangman today!'
			break


def print_hangman(wrong_count):
#Prints hangman for each wrong_count value
	if wrong_count==0:
		print " _________     \n"
		print "|         |    \n"
		print "|              \n"
		print "|        	  \n"
		print "|        	  \n"
		print "|              \n"
		print "|              \n"
	if wrong_count==1:
		print " _________     \n"
		print "|         |    \n"
		print "|         0    \n"
		print "|          	  \n"
		print "|        	  \n"
		print "|              \n"
		print "|              \n"
	if wrong_count==2:
		print " _________     \n"
		print "|         |    \n"
		print "|         0    \n"
		print "|         |    \n"
		print "|        	  \n"
		print "|              \n"
		print "|              \n"
	if wrong_count==3:
		print " _________     \n"
		print "|         |    \n"
		print "|         0    \n"
		print "|        /|    \n"
		print "|        	  \n"
		print "|              \n"
		print "|              \n"
	if wrong_count==4:
		print " _________     \n"
		print "|         |    \n"
		print "|         0    \n"
		print "|        /|\\  \n"
		print "|        	  \n"
		print "|              \n"
		print "|              \n"
	if wrong_count==5:
		print " _________     \n"
		print "|         |    \n"
		print "|         0    \n"
		print "|        /|\\  \n"
		print "|        / 	  \n"
		print "|              \n"
		print "|              \n"
	if wrong_count==6:
		print " _________     \n"
		print "|         |    \n"
		print "|         0    \n"
		print "|        /|\\  \n"
		print "|        / \\  \n"
		print "|              \n"
		print "|              \n"


# Begin playing game automatically once program run
play_hangman()
