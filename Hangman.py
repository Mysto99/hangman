import random

#Opens the file containing all the words and adds them to a list
word_list = []
with open('words.txt','r') as file:
	for line in file:
		for word in line.split():
			word_list.append(word)

#Randomly chooses a word from the list.
random_word = random.choice(word_list)
#print (random_word)

answer = list(len(random_word)*'_')
lives = 7
game_won = False
wrong_guess = []

while game_won == False and lives > 0:
	print (answer)
	guess = input("Guess a letter or a word: ").lower()

	if guess == random_word:
		print ("You guessed correctly")
		game_won = True
	elif len(guess) == 1 and guess in random_word:
		for i in range(0, len(random_word)):
			letter = random_word[i]
			if guess == letter:
				answer[i] = guess
		if '_' not in answer:
			game_won = True
	elif guess not in random_word:
		wrong_guess.append(guess)
		print ("Your wrong guesses: ", wrong_guess)
		lives -= 1
		print ("You have", lives, "lives left")

