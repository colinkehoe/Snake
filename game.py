import pygame
import time
import random

window_x = 720
window_y = 480

#define window size and initialize pygame
pygame.init()
game_window = pygame.display.set_mode((720, 480))
pygame.display.set_caption('Snake')

#define colors
blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

#FPS controller
fps = pygame.time.Clock()

#snake globals
snake_speed = 15
snake_position = [100, 50]
snake_body = [ [100, 50],
                [90, 50],
                [80, 50],
                [70, 50],
            ]
direction = 'RIGHT'
change_to = direction

#food globals
fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True

#score globals
score = 0
def show_score(choice, color, font, size):
    #define font
    score_font = pygame.font.SysFont(font, size)

    #create the display surface
    score_surface = score_font.render('Score : ' + str(score), True, color)

    #create a rectangle for the text surface
    score_rect = score_surface.get_rect()

    #display the score
    game_window.blit(score_surface, score_rect)

#define game over screen
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score: ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()

    #set position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)

    #blit will draw the text to the screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    #quit after 2 seconds
    time.sleep(2)
    pygame.quit()
    quit()

while True:

    #handle key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    #If two keys are pressed at the same time
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    
    #move the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    #Snake body growing mechanism
    #if fruit and snake collide then score will increment by 1
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 1
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                          random.randrange(1, (window_y//10)) * 10]

    fruit_spawn = True
    game_window.fill(black)

    for pos in snake_body:
        #draw snake
        pygame.draw.rect(game_window, blue, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(game_window, white, (fruit_position[0], fruit_position[1], 10, 10))

    #game over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()

    #display score
    show_score(1, white, 'times new roman', 20)

    #refresh game screen
    pygame.display.update()

    fps.tick(snake_speed)