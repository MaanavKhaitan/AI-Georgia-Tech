import numpy as np

word_list = ['orange', 'lambda', 'gentleman', 'lanyard', 'jelly', 'xylophone', 'waffle']
user_guesses = []
second_player = False

def ask_user_letter(guesses_list):
#Asks user for and returns a letter guess
	user_letter = raw_input('Please enter a letter: ')
	if len(user_letter) != 1 or type(user_letter) != str:
		print 'Guess must be one letter long.'
		user_letter = ask_user_letter(guesses_list)
	if user_letter in guesses_list:
		print 'You already typed the letter %s!' % (user_letter)
		user_letter = ask_user_letter(guesses_list)
	return user_letter.lower()

def print_initial_progress(word):
#Prints initial dashes based on length of word
	initial_progress = '_'
	for i in range(0,len(word)-1):
		initial_progress += ' _'
	return initial_progress

def print_progress(letter, indices, progress):
#Prints progress of user at every turn
	final_progress = ''
	if indices==[0]:
		final_progress += letter + progress[1:]
	elif len(str(indices)) > 1:
		temporary_progress = progress
		for index in indices:
			temporary_progress = print_progress(letter,index,temporary_progress)
		final_progress = temporary_progress
	else:
		later_index = ((indices+1)*2-2)
		final_progress += progress[0:((indices+1)*2-2)] + letter + progress[later_index+1:]
	final_progress = final_progress
	return final_progress 

def find_indices(word, letter):
#Returns all indices in word where letter appears
    return [i for i, ltr in enumerate(word) if ltr == letter]

def ask_second_player_for_word():
	second_player_word = raw_input('Player 1, please provide a word for player 2 to guess: ')
	return second_player_word.lower()

def play_hangman():
#Main function that makes user play the entire game of Hangman
	print 'Welcome to the wonderful game of Hangman!'
	wrong_guess_count = 0
	second_player = raw_input('How many players are playing today? (1/2)')
	if second_player=='2':
		word = ask_second_player_for_word()
		for i in range(0,40):
			print " \n"
		print 'Now please hand the device to Player 2 and enjoy the game: '
	else:
		word = np.random.choice(word_list).lower()
	user_guesses = []
	user_progress = print_initial_progress(word)
	complete_guess = ''
	for i in range(0,50):
		print_hangman(wrong_guess_count)
		print user_progress
		user_guess = ask_user_letter(user_guesses)
		if user_guess not in user_guesses:
			user_guesses.append(user_guess)		
		if user_guess in word:
			user_progress = print_progress(user_guess, find_indices(word,user_guess), user_progress)
			complete_guess += user_guess*len(find_indices(word,user_guess))
			if len(''.join(set(complete_guess))) == len(''.join(set(word))) and sorted(''.join(set(complete_guess))) == sorted(''.join(set(word))):
				print_hangman(wrong_guess_count)
				print user_progress
				print 'Congratulations! The word was %s!' % (word)
				user_again_choice = raw_input('Would you like to play again? (y/n)')
				if user_again_choice=='y':
					print 'We\'re glad to hear that!'
					play_hangman()
				elif user_again_choice=='n':
					print 'Well we hope you enjoyed your game of Hangman today!'
				break
		else:
			wrong_guess_count += 1
			print '%s is not in the word.'%(user_guess)
		if wrong_guess_count==6:
			print_hangman(wrong_guess_count)
			print user_progress
			print 'Sorry, game over! The word was %s.'%(word)
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



play_hangman()
