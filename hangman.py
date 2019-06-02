import random as rand
import os
import math

debug = False
win = 0
loss = 0


def main(win, loss):

	valid = False
	difficulty = 0
	guess = ''
	
	
	
	print('----------------------------')
	print('1. Beginner - 10 lives')
	print('2. Intermediate - 8 lives')
	print('3. Advanced - 6 lives')
	print('4. Expert - 4 lives')
	print('5. What - 2 lives')
	print('----------------------------')
	print('{} W | {} L | {} G | {} %'.format(win, loss, win+loss, math.floor((win/(win+loss or 1))*100)))
	print('----------------------------')

	while(True):
		try:
			difficulty = int(input('Enter a valid difficulty:'))
		except:
			print('Enter a valid input.')
		if(difficulty < 1 or difficulty > 5):
			continue
		else:
			break
		
	init_game(difficulty, win, loss)
	

	
def init_game(difficulty, win, loss):

	with open('words.txt', 'r+') as wordlist:
		attempted_guesses = ''
		
		currentguess = []
		words = wordlist.readlines()
		chosenword = words[math.floor(rand.random() * len(words))]
		
		
		for letter in range(len(chosenword) - 1):
			currentguess.append('?')
		
		game(difficulty_to_lives[difficulty], chosenword, currentguess, attempted_guesses, win, loss)
		
		
		

def game(lives, chosenword, currentguess, attempted_guesses, win, loss):
	
	os.system('cls')
	check_guess = ''.join(currentguess)
	if debug:
		print(chosenword)

	
	if(lives < 1):
		print('You lose!')
		_ = input('Press enter to continue...')
		os.system('cls')
		loss += 1
		main(win, loss)
	elif check_guess in chosenword:
		print('You win!')
		_ = input('Press enter to continue...')
		os.system('cls')
		win += 1
		main(win, loss)
	else:
	
		print('You have {} lives.'.format(str(lives)))
		print('\n')
		print(''.join(currentguess))
		print('\n')
		print('Attempted Guesses: {}'.format(str(attempted_guesses)))
		
		while(True):
			guess = input('Make a guess ')
			if guess in attempted_guesses:
				print(guess + ' was already attempted.')
				continue
			elif(len(guess) > 1):
				print('Cannot make multiple guesses at once.')
			else:
				attempted_guesses += guess
				break
				
		if guess not in chosenword:
			lives -= 1
			game(lives, chosenword, currentguess, attempted_guesses, win, loss)
		else:
			for i, letter in enumerate(chosenword):
				if(guess == letter):
					currentguess[i] = guess
			game(lives, chosenword, currentguess, attempted_guesses, win, loss)
				
		
		
		
		

difficulty_to_lives = {
	1:	10,
	2:	8,
	3:	6,
	4:	4,
	5:	2
}
os.system('cls')
main(win, loss)