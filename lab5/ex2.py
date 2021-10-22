import pygame
from pygame.draw import *
from random import randint
pygame.init()

user1=input()
user="username: "+user1

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
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

pygame.display.update()
clock = pygame.time.Clock()
finished = False

def read_file():
    """Функция чтения файла. Возвращает три массива: в первом результаты находятся с именами игроков,
    во втором - только имена, в третьем - только результаты. Создает файл, если не было найдено нужного"""
    res=[]
    try:
        with open("res.txt", "r") as f:
            users=[]
            scores=[]
            for line in f:
                data=line.split(":   ")
                if len(data)==2:
                    res.append(data)
                    users.append(data[0])
                    scores.append(data[1])
    except:
        with open("res.txt", "w"):
            pass
        return [], [], []
    return res, users, scores

def write_file(user, score):
    """Функция записи в файл обновленных результатов. Для корректной работы функции важно, чтобы
    результаты в файле уже были отсортированы"""
    data, users, scores=read_file() 
    find=False
    with open("res.txt", "w") as f:
        # Если поставлен новый рекорд, добавляем новый результат в начало
        if len(scores)>=1 and score>int(scores[0]):
            scores=[str(score) +"\n"] + scores
            users=[user]+users
        else:
            # Пробегаем весь массив и ищем меньший результат
            for i, score_file in enumerate(scores):
                if int(score_file)<=score:
                    if not find:
                        # Следим, чтобы новый результат записывался один раз
                        scores_tmp=scores[:i] + [str(score)+"\n"] + scores[i:]
                        users_tmp=users[:i] + [user] + users[i:]
                        scores=scores_tmp
                        users=users_tmp
                        find=True
            # Если результата хуже не найдено, записываем в конец
            if not find:
                scores=scores+[str(score)+"\n"]
                users=users+[user]
        

        for i, user in enumerate(users):
            f.write(f"{user}:   {scores[i]}")
            

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

def pool_of_balls(number_of_balls):
    """Функция объединяет данные о нужном количестве (number_of_balls) мячей в двумерный массив"""
    pool=[]
    for i in range  (number_of_balls):
        pool2=new_ball()
        pool.append(pool2)
    return pool

def move(pool,number_of_balls,dt):
    """Фукция реализует движение шаров внутри поля выбранного размера, изменяя соответстсвующим образом координаты и, 
    если это необходимо, скорости шаров в их общем массиве (pool) размерности number_of_balls с временным шагом dt"""
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

def new_blinker():
    """Функция создает информацию о появляющемся и исчезающем объекте, возвращает массив, элементами которого являются цвет,
    время жизни, координаты его левого верхнего угла, ширина и высота соответственно"""
    pool2=[]
    pool2.append(COLORS[randint(0, 5)])
    pool2.append(randint(40,80))
    for j in range(2):
        pool2.append(randint(0,560))
    for j in range(2):
        pool2.append(randint(20,40))
    return pool2

def death_of_blinker(pool,dt):
    "Функция уменьшает оставшееся время жизни исчезающего объекта или заменяет его на новый, если время истекло"
    if pool[1]<=0:
        pool=new_blinker()
    else:
        pool[1]-=dt
    return pool

def draw_balls(pool, number_of_balls):
    """Функция отрисовывает общий массив (pool) шариков размерности number_of_balls"""
    for i in range(number_of_balls):
        circle(screen, pool[i][0], (pool[i][2], pool[i][3]), pool[i][1])

def draw_blinker(pool):
    """Функция отрисовывает исчезающий объект"""
    if pool[1]%40>20:
        rect(screen, pool[0], (pool[2], pool[3], pool[4], pool[5]))

# Счетчик очков
score=0
# Создаем много шариков и исчезающий объект
number=10
pool=pool_of_balls(number)
blinker=new_blinker()

while not finished:
    clock.tick(FPS)
    draw_balls(move(pool,number,1), number)
    blinker=death_of_blinker(blinker,1)
    draw_blinker(blinker)
    for event in pygame.event.get():
        # Если пользователь закрыл окно:
        if event.type==pygame.QUIT:
            # Записываем результат игры в файл
            write_file(user1,score)
            finished=True
        # Если пользователь нажал кнопку мыши:
        elif event.type==pygame.MOUSEBUTTONDOWN:
            print('Click!')
            # Считываем координаты клика
            event.x=event.pos[0]
            event.y=event.pos[1]
            counter=0
            # Проверем, попал ли пользователь хотя бы в один из объектов
            x=blinker[2]
            y=blinker[3]
            dx=blinker[4]
            dy=blinker[5]
            if (event.x<=x+dx)&(event.x>=x-dx)&(event.y<=y+dy)&(event.y>=y-dy):
                score+=2
                counter+=1
            for i in range(number):
                x=pool[i][2]
                y=pool[i][3]
                r=pool[i][1]
                event.r=((event.x-x)**2+(event.y-y)**2)**0.5
                if event.r<=r:
                    # Если пользователь попал, заменяем пойманный шарик на другой, случайный 
                    pool[i]=new_ball()
                    counter+=1  
            if counter==0:
                # Ни одного попадания не обнаружено - сообщаем об этом пользователю и уменьшаем количество очков на 1
                print('Miss!')
                score-=1
            else:
                # Обнаружено counter попаданий - сообщаем пользователю об успехе, даем по 2 балла за попадание
                print('Success!')
                score=score+counter*2
            # Обновляем картинку на экране, сообщаем текущее количество баллов
            pygame.display.update()
            screen.fill(BLACK)
            print(score)
    # Выводим результат на экран
    font=pygame.font.Font(None, 36)
    scorevalue="score = "+str(score)
    scoreboard=font.render(scorevalue, True, WHITE)
    screen.blit(scoreboard, (10, 50))
    username=font.render(user, True, WHITE)
    screen.blit(username, (10, 70))
    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()

