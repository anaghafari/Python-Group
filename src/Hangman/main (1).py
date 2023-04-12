import pygame
import random

import levels
import words

# setup
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Welcome to Hangman Aqua Game")

# FIXME
while levels.level <= 2:
    word_count = 0
    while word_count < 1:
        # choose a random word
        target = random.choice(words.level_words())
        target_lst = [target[i] for i in range(len(target))]
        copy_lst = target_lst.copy()

        while len(target_lst) > 0:
            guess = input("Guess a letter: ")
            if guess not in target_lst:
                print("That's wrong!")
            else:
                # find indices
                indices = []
                for pos, char in enumerate(copy_lst):
                    if char == guess:
                        indices.append(pos)

                while guess in target_lst:
                    target_lst.remove(guess)
                print("Good job! That's a letter!")

        print("You guessed the word correctly!")
        word_count += 1
    
    print("Entering the next level...")
    levels.update_level()

print("Game end.")