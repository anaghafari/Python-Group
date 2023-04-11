# Python-Group

Anahita Ghafari-Tester and Project manager


Daniel Qian-Multimedia Creator/Implementer 


Elsa Bringard-Designer


Kaitlyn Cao-Developer/Coder




### Hangman
Graphic based OOP Hangman

### This is our version of hangman, unlike other versions of hangman instead of adding limbs until you lose, the water rises until you lose. There are also different difficulties available, and there is a shark.

mock up provided by Anahita and Elsa
![Running Hangman](https://github.com/anaghafari/Python-Group/blob/main/Images/shark.png?raw=true)
![Running Hangman](https://github.com/anaghafari/Python-Group/blob/main/Images/shark2.png?raw=true)
![Running Hangman](https://github.com/anaghafari/Python-Group/blob/main/Images/shark3.png?raw=true)
updated mark down provided by Elsa Bringard
![Markdown](https://github.com/anaghafari/Python-Group/blob/main/Images/Class%20diagram%20hangman%20aqua.png?raw=true)
provided by Elsa Bringard, and Anahita
![Running main.py] (import pygame
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
provided by
![Running levels.py] ()
provided by
![Running words.py] ()




