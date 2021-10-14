import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 40
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

def pool_of_balls(number_of_balls):
    """Функция создает несколько мячей"""
    pool=[]
    for i in range  (number_of_balls):
        pool2=new_ball()
        pool.append(pool2)
    return pool

def new_ball():
    """Функция создает мяч и возвращает массив из его цвета, размера, пары координат
    (x, y), скорости (v_x, v_y)"""
    pool2=[]
    pool2.append(COLORS[randint(0, 5)])
    pool2.append(randint(30,50))
    for j in range(2):
        pool2.append(randint(100,500))
    for j in range(2):
        pool2.append(randint(-10,10))
    return pool2

def move(pool,number_of_balls,dt):
    for i in range  (number_of_balls):
        pool[i][2]+=pool[i][4]*dt
        pool[i][3]+=pool[i][5]*dt
        if  pool[i][2]+pool[i][1]>600:
             pool[i][2]=600-pool[i][1]
             pool[i][4]=-pool[i][4]
        if  pool[i][2]-pool[i][1]<0:
             pool[i][2]=pool[i][1]
             pool[i][4]=-pool[i][4]
        if  pool[i][3]+pool[i][1]>600:
             pool[i][3]=600-pool[i][1]
             pool[i][5]=-pool[i][5]
        if  pool[i][3]-pool[i][1]<0:
             pool[i][3]=pool[i][1]
             pool[i][5]=-pool[i][5]
    return pool

def draw(pool, number_of_balls):
    for i in range(number_of_balls):
        circle(screen, pool[i][0], (pool[i][2], pool[i][3]), pool[i][1])

# Счетчик очков
score=0
# Создаем много шариков
number=10
pool=pool_of_balls(number)

while not finished:
    clock.tick(FPS)
    draw(move(pool,number,1), number)
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
            counter=0
            for i in range(number):
                x=pool[i][2]
                y=pool[i][3]
                r=pool[i][1]
                if (event.x>=x-r)&(event.x<=x+r)&(event.y>=y-r)&(event.y<=y+r):
                    pool[i]=new_ball()
                    counter+=1  
            if counter==0:
                print('Miss!')
                score-=1
            else:
                print('Success!')
                score=score+counter*2
            pygame.display.update()
            screen.fill(BLACK)
            print(score)
    pygame.display.update()
    screen.fill(BLACK)

print(score)
pygame.quit()