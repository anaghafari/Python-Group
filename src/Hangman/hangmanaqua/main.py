import levels
import pygame
import random
import words

def update_game_screen(hidden_letters, screen, water_level):
    """ Updates water level. """
    screen.fill("white")
    hangman_img = pygame.image.load("hangman0.png")
    water_img = pygame.image.load("water.png")
    shark_img = pygame.image.load("shark.png")

    screen.blit(hangman_img, (0, 0))

    if water_level == 0:
        screen.blit(water_img, (0, 250))
    if water_level == 1:
        screen.blit(water_img, (0, 180))
    if water_level == 2:
        screen.blit(water_img, (0, 110))
    if water_level == 3:
        screen.blit(water_img, (0, 40))
    if water_level == 4:
        screen.blit(water_img, (0, -30))
    if water_level == 5:
        screen.blit(water_img, (0, -100))

    screen.blit(shark_img, (500, 50))

    blanks = font.render("".join(hidden_letters), True, "black")
    screen.blit(blanks, (screen.get_width() / 2, 250))

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

pygame.display.set_caption("Welcome to Hangman Aqua Game")
font = pygame.font.SysFont("Arial", 36)

running = True

while True:

    current_water_level = 0
    word_count = 0

    # choose a random word
    target = random.choice(words.level_words())
    hidden_letters = []
    for _ in range(len(target)):
        hidden_letters.append("-")

    while word_count < 1:
        update_game_screen(hidden_letters, screen, current_water_level)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                guess = chr(event.key)

                # pygame.draw.rect(Display,WHITE,(220,200,280,100)) #hide word
                #     pygame.draw.rect(Display,WHITE,(260,50,200,100))

                if guess in target:
                    indices = []
                    for pos, char in enumerate(target):
                        if char == guess:
                            hidden_letters[pos] = target[pos]
                else:
                    current_water_level += 1
                
                update_game_screen(hidden_letters, screen, current_water_level)
        
        if "".join(hidden_letters) == target:
            update_game_screen(hidden_letters, screen, current_water_level)
            next_screen = font.render("You guessed the word correctly!", True, "black")
            screen.blit(next_screen, (screen.get_width() / 2, screen.get_height() / 2))
            word_count += 1
        
        if current_water_level == 5:
            screen.fill("white")
            next_screen = font.render("GAME OVER!", True, "black")
            screen.blit(next_screen, (screen.get_width() / 2 - 100, screen.get_height() / 2 - 50))
            running = False

        pygame.display.update()
        clock.tick(30)

        if not running:
            pygame.quit()
    
    update_game_screen(hidden_letters, screen, current_water_level)
    next_screen = font.render("Entering the next level...", True, "black")
    screen.blit(next_screen, (screen.get_width() / 2, screen.get_height() / 2))
    levels.update_level()

    print(levels.level)

    if levels.level > 2:
        screen.fill("white")
        next_screen = font.render("GAME END!", True, "black")
        screen.blit(next_screen, (screen.get_width() / 2 - 100, screen.get_height() / 2 - 50))
        running = False
    
    pygame.display.update()
    clock.tick(30)

    if not running:
        pygame.quit()