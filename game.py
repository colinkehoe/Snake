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

#score globals
score = 0
high_score = 0
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
    while True:
        my_font = pygame.font.SysFont('calibri', 32)

        text = ["Your score: " + str(score), 
                "High score: "+ str(high_score), 
                "Press 'enter' to play again", 
                "Press 'esc' to quit"
                ]
        label = []
        
        for line in text:
            label.append(my_font.render(line, True, white))

        for line in range(len(label)):
            game_window.blit(label[line], (window_x//2 - label[line].get_width()//2, window_y//2 - label[line].get_height()//2 + line*50))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True
                if event.key == pygame.K_ESCAPE:
                    return False

def game(): 
    global score
    snake_position = [100, 50]
    snake_body = [ [100, 50],
                [90, 50],
                [80, 50],
                [70, 50],
    ]
    snake_speed = 15
    direction = 'RIGHT'
    change_to = direction
    fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
    fruit_spawn = True
    score = 0

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
        break_out_flag = False
        if snake_position[0] < 0 or snake_position[0] > window_x-10:
            break_out_flag = True
        if snake_position[1] < 0 or snake_position[1] > window_y-10:
            break_out_flag = True
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                print("hit")
                break_out_flag = True
        if break_out_flag == True:
            break

        #display score
        show_score(1, white, 'calibri', 20)

        #refresh game screen
        pygame.display.update()

        fps.tick(snake_speed)

def main():
    global high_score, score
    while True:
        game()
        if score > high_score:
            high_score = score
        cont = game_over()
        if not cont:
            break
    pygame.quit()
    quit()

if __name__ == '__main__':
    main()