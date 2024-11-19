#importing necessary modules
from words import words
from image import img
import random

#variables
rand = random.randint(0, len(words) - 1)
word = words[rand]
length = len(word)
word_split = list(word)
count = 0
i = 0

#filling in the blanks for the word to be guessed
guess = ["_"] * length

#looping
while i != 7:
    print(' '.join(guess))
    inp = input("Enter a letter (only 1): ").lower()
    if len(inp) != 1 or not inp.isalpha():
        print("Invalid input! Try again")
        continue

    #checking whether the word is inside the list
    for b in word_split:
        if inp == b:
            del guess[count]
            guess.insert(count, inp)
        count += 1
    count = 0
    if inp in word_split:
        i = i
        print('Good guess!')
    else:
        i += 1
        print(f'Uh oh! The guess was incorrect! You have {7-i} guesses left')

    #drawing the hangman
    if i >= 7:
        print(img[i - 1])
        print(f"You failed us mate. The actual word was {word}")
        break
    else:
        print(img[i - 1])

    print("____________________________________________")

    #checking if you won or not
    if guess == word_split:
        print("You won, GG mate")
        break