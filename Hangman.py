import numpy as np

word_list = ['maanav', 'meele', 'lambda']

def ask_user_letter():
#Asks user for and returns a letter guess
	user_letter = raw_input('Please enter a letter: ')
	if len(user_letter) != 1:
		print 'Guess must be one letter long.'
		ask_user_letter()
	return user_letter

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
	return final_progress 

def find_indices(word, letter):
#Returns all indices in word where letter appears
    return [i for i, ltr in enumerate(word) if ltr == letter]


def play_hangman():
#Main function that makes user play the entire game of Hangman
	print 'Welcome to the wonderful game of Hangman!'
	wrong_guess_count = 0
	word = np.random.choice(word_list)
	user_progress = print_initial_progress(word)
	complete_guess = ''
	for i in range(0,50):
		print_hangman(wrong_guess_count)
		print user_progress
		user_guess = ask_user_letter()
		if user_guess in word:
			user_progress = print_progress(user_guess, find_indices(word,user_guess), user_progress)
			complete_guess += user_guess*len(find_indices(word,user_guess))
			if len(complete_guess) == len(word) and sorted(complete_guess) == sorted(word):
				print 'Congratulations! The word was %s!' % (word)
				break
		else:
			wrong_guess_count += 1
			print '%s is not in the word.'%(user_guess)
		if wrong_guess_count==6:
			print_hangman(wrong_guess_count)
			print 'Sorry, game over! The word was %s.'%(word)
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

