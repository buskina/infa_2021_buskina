import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 2
screen = pygame.display.set_mode((600, 600))

# Задаем возможные цвета шариков
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

pygame.display.update()
clock = pygame.time.Clock()
finished = False

def new_ball(x,y,r):
    """Функция рисует шарик. Принимает на вход:
    x, y - координаты центра шарика
    r - радиус шарика"""
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

# Счетчик очков
score=0

while not finished:
    clock.tick(FPS)
    # Рисуем шарик
    global x,y,r
    x = randint(100,600)
    y = randint(100,600)
    r = randint(30,400)
    new_ball(x,y,r)

    for event in pygame.event.get():
        # Если пользователь закрыл окно:
        if event.type == pygame.QUIT:
            finished = True
        # Если пользователь нажал кнопку мыши:
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            # Считываем координаты клика
            event.x=event.pos[0]
            event.y=event.pos[1]
            # Проверяем, попал ли пользователь в шарик
            if (event.x>=x-r)&(event.x<=x+r)&(event.y>=y-r)&(event.y<=y+r):
                print('Success!')
                score+=2
            else:
                print('Miss!')
                score-=1
            pygame.display.update()
            screen.fill(BLACK)
    print('nextball')
    print(score)
    pygame.display.update()
    screen.fill(BLACK)

print(score)
pygame.quit()