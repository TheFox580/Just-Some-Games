import pygame
import random
import math

"""

Tic-Tac-Toe: A classic game where players take turns marking spaces in a 3x3 grid to get three in a row.

Snake Game: Control a snake as it moves around the screen, eating food to grow longer while avoiding collisions with itself and the walls.

Pong: A simple two-player game where each player controls a paddle to hit a ball back and forth, trying to score points against the opponent.

Hangman: Players guess letters to uncover a hidden word within a certain number of attempts.

Memory Puzzle: A game where players need to match pairs of cards by flipping them over two at a time.

Space Invaders: Control a spaceship to shoot down rows of descending aliens while avoiding their projectiles.

Minesweeper: Players clear a minefield without detonating any mines by using clues about the number of neighboring mines in each field.

Sudoku Solver: Create a program that generates and solves Sudoku puzzles.

2048: A sliding block puzzle game where players combine tiles with the same number to reach the 2048 tile.

Flappy Bird Clone: Navigate a bird through a series of pipes by tapping the screen to make it flap its wings.

Tower Defense Game: Defend a base from waves of enemies by strategically placing defensive towers along their path.

Crossword Puzzle Generator: Develop a program that generates crossword puzzles with clues.

Text-based Adventure Game: Create an interactive story where players make choices to progress through different scenarios.

Chess: Implement a two-player chess game with basic rules and functionalities.

Breakout: Control a paddle to bounce a ball and break bricks arranged at the top of the screen.

RPG Battle Simulator: Build a turn-based battle simulator where players control characters and fight against enemies.

Frogger: Guide a frog across a busy road and river, avoiding obstacles and vehicles.

Simon Says: A game that tests players' memory by requiring them to repeat a sequence of button presses.

Trivia Quiz: Create a quiz game with multiple-choice questions on various topics.

Racing Game: Develop a simple racing game where players compete against each other or AI opponents on a track.

"""

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
dt = 0

time_p1 = 0
time_p2 = 0
time_enemy = 0
time_apple = 0

score_p1 = 0
score_p2 = 0

border_top = pygame.Rect(-1, -1, 1280, 1)
border_left = pygame.Rect(-1, -1, 1, 720)
border_right = pygame.Rect(1281, -1, 1, 720)
border_bottom = pygame.Rect(-1, 721, 1280, 1)

list_border = [border_top, border_left, border_right, border_bottom]

player_1 = pygame.Rect(300, screen.get_height() / 2, 40, 40)
player_2 = pygame.Rect(1280 - 300, screen.get_height() / 2, 40, 40)
list_apples = []
list_enemies = []

pressed_pause = 0

is_running = True
is_playing = True
p1_alive = True
p2_alive = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    
    screen.fill("black")

    font = pygame.font.SysFont("Helvetica Rounded", 36)
    txtscore_p1 = font.render(f"Player 1 score : {score_p1}", True, "white")
    txtscore_p2 = font.render(f"Player 2 score : {score_p2}", True, "white")
    txtapples = font.render(f"Apples on the screen : {len(list_apples)}", True, "white")
    txtsize = font.render(f"Player 1 size : {round(player_1.width/2)}", True, "white")
    txtsize2 = font.render(f"Player 2 size : {round(player_2.width/2)}", True, "white")
    txttime_p1 = font.render(f"Player 1 timer alive : {math.floor(time_p1/60)}", True, "white")
    txttime_p2 = font.render(f"Player 2 time alive : {math.floor(time_p2/60)}", True, "white")
    screen.blit(txtscore_p1,(10, 10))
    screen.blit(txtscore_p2,(1050, 10))
    screen.blit(txtapples,(500, 10))
    screen.blit(txtsize,(10, 35))
    screen.blit(txtsize2,(1050, 35))
    screen.blit(txttime_p1,(10, 60))
    screen.blit(txttime_p2,(1000, 60))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        if pressed_pause <= 0:
            is_playing = not is_playing
            pressed_pause = 0.25*60

    if pressed_pause > 0:
        pressed_pause -= 1

    if is_playing:
        
        if not p1_alive and not p2_alive:
            is_running = False

        if p1_alive :
            time_p1 += 1
            pygame.draw.rect(screen, "white", player_1, player_1.width)
        if p2_alive :
            time_p2 += 1
            pygame.draw.rect(screen, "blue", player_2, player_2.width)

        for apple in list_apples:
            if player_1.width + 5 >= apple.width or player_2.width + 5 >= apple.width:
                pygame.draw.rect(screen, "red", apple, apple.width)
            else:
                pygame.draw.rect(screen, "gray", apple, apple.width)
        for enemy in list_enemies:
            pygame.draw.rect(screen, "green", enemy, enemy.width)

        if p1_alive:
            if keys[pygame.K_z]:
                player_1.top -= 1 + (1-round(player_1.width/40))
            if keys[pygame.K_s]:
                if player_1.width < 20:
                    player_1.top += 10
                elif player_1.width > 60:
                    player_1.top += 3
                else:
                    player_1.top += 5
            if keys[pygame.K_q]:
                if player_1.width < 20:
                    player_1.left -= 10
                elif player_1.width > 60:
                    player_1.left -= 3
                else:
                    player_1.left -= 5
            if keys[pygame.K_d]:
                if player_1.width < 20:
                    player_1.left += 10
                elif player_1.width > 60:
                    player_1.left += 3
                else:
                    player_1.left += 5

        if p2_alive:
            if keys[pygame.K_UP]:
                if player_2.width < 20:
                    player_2.top -= 10
                elif player_2.width > 60:
                    player_2.top -= 3
                else:
                    player_2.top -= 5
            if keys[pygame.K_DOWN]:
                if player_2.width < 20:
                    player_2.top += 10
                elif player_2.width > 60:
                    player_2.top += 3
                else:
                    player_2.top += 5
            if keys[pygame.K_LEFT]:
                if player_2.width < 20:
                    player_2.left -= 10
                elif player_2.width > 60:
                    player_2.left -= 3
                else:
                    player_2.left -= 5
            if keys[pygame.K_RIGHT]:
                if player_2.width < 20:
                    player_2.left += 10
                elif player_2.width > 60:
                    player_2.left += 3
                else:
                    player_2.left += 5

        time_enemy += 1
        time_apple += 1

        if time_apple > 200:
            
            if p1_alive :
                player_1.width -= 2
                player_1.height -= 2
                player_1.left += 1
                player_1.top += 1

            if p2_alive: 
                player_2.width -= 2
                player_2.height -= 2
                player_2.left += 1
                player_2.top += 1

            if player_1.width < 10:
                p1_alive = False

            if player_2.width < 10:
                p2_alive = False

            for apple in list_apples:
                apple.width += 2
                apple.height += 2
                apple.left -= 1
                apple.top -= 1
            
            for _ in range(2):
                apple = pygame.Rect(random.randint(100, screen.get_width() - 100), random.randint(100, screen.get_height() - 100), 10, 10)

                pygame.draw.rect(screen, "red", apple, apple.width)

                list_apples.append(apple)

            time_apple = 0

        if time_enemy > 1000:

            for enemy in list_enemies:
                enemy.width += 2
                enemy.left -= 1
                enemy.height += 2
                enemy.top -= 1

            if len(list_enemies) < 5:
                
                enemy = pygame.Rect(random.randint(100, screen.get_width() - 100), random.randint(100, screen.get_height() - 100), 10, 10)

                pygame.draw.rect(screen, "green", enemy, enemy.width)

                list_enemies.append(enemy)

            time_enemy = 0

        for enemy in list_enemies:
            if pygame.Rect.colliderect(player_1, enemy):
                p1_alive = False
            if pygame.Rect.colliderect(player_2, enemy):
                p2_alive = False

        for apple in list_apples:
            if pygame.Rect.colliderect(player_1, apple):
                if player_1.width + 5 >= apple.width:
                    apple.width = 0
                    apple.height = 0
                    list_apples.remove(apple)
                    score_p1 += 1
                    player_1.width += 2
                    player_1.height += 2
                    player_1.left -= 1
                    player_1.top -= 1
            if pygame.Rect.colliderect(player_2, apple):
                if player_2.width + 5 >= apple.width:
                    apple.width = 0
                    apple.height = 0
                    list_apples.remove(apple)
                    score_p2 += 1
                    player_2.width += 2
                    player_2.height += 2
                    player_2.left -= 1
                    player_2.top -= 1
            for enemy in list_enemies:
                if pygame.Rect.colliderect(apple, enemy):
                    apple.width = 0
                    apple.height = 0
                    list_apples.remove(apple)
                    score_p1 -= 1
                    score_p2 -= 1
        
        if pygame.Rect.colliderect(player_1, player_2):
            is_running = False
        
        for border in list_border:
            if p1_alive:
                if pygame.Rect.colliderect(player_1, border):
                    p1_alive = False
            if p2_alive:
                if pygame.Rect.colliderect(player_2, border):
                    p2_alive = False
        
        if player_1.width == 80 or player_2.width == 80:
            is_running = False
    
    else:
        screen.blit(pygame.font.SysFont("Helvetica Rounded", 120).render("Paused", True, "white"),(500, 325))

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()