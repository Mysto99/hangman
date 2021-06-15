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

#counts the number of letters and creates a list with the same amount of dashes as letters.
answer = list(len(random_word)*'_')
lives = 7
game_won = False
#All the wrong guesses will be added to this list to keep track.
wrong_guess = []

#Continues to run the game as long as the user's life does not run out.
while game_won == False and lives > 0:
	#prints out the list containing the dashes and ask for the user input.
	print (answer)
	guess = input("Guess a letter or a word: ").lower()

	#If the user enter the correct word. game_won = True will end the while loop
	if guess == random_word:
		print ("You guessed correctly")
		game_won = True
	#Checks if the letter that the user input is in the random word.
	elif len(guess) == 1 and guess in random_word:
		for i in range(0, len(random_word)):
			letter = random_word[i]
			if guess == letter:
				answer[i] = guess
		#When the answer list contain no more dashes (replaced by letters), it will end the while loop.
		if '_' not in answer:
			game_won = True
	#If user took a wrong guess, it will be added to the wrong guess list and 1 life will be deducted.
	elif guess not in random_word:
		wrong_guess.append(guess)
		print ("Your wrong guesses: ", wrong_guess)
		lives -= 1
		print ("You have", lives, "lives left")

