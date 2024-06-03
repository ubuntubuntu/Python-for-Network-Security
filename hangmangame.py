#!/bin/python3
import random
print("Welcome to Hangman Game")
chall_words = ["pentest","hacker","vulnerability"]
chosen_word = random.choice(chall_words)
print(chosen_word)
display_word = []
for letter in chosen_word:
        display_word += "_"
print(f"You have to fill this blank word {display_word}")
game_over = False

while not game_over:
        guess = input("Guess a letter ").lower()
        for position in range(len(display_word)):
                letter = chosen_word[position]
                if letter == guess:
                        display_word[position] = guess
        print(display_word)
        if "_" not in display_word:
                print("You Win")
                game_over = True
