import math
from random import randint as rnd
from random import choice

import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = 0x000000
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.vy -= 1
        self.x += self.vx
        self.y -= self.vy
        if self.y + self.r >= HEIGHT:
            self.vx = 0.8*self.vx
            self.vy = -0.9*self.vy
            self.y = HEIGHT - self.r
        if self.x + self.r >= WIDTH:
            self.vx = -self.vx
            self.x = WIDTH - self.r

    def draw(self):
        """Отрисовывает мяч"""
        border = self.r+1
        pygame.draw.circle(
            self.screen,
            BLACK,
            (self.x, self.y),
            border
        )
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if ((self.x-obj.x)**2+(self.y-obj.y)**2)**0.5 > self.r + obj.r:
            return False
        else:
            return True


class Gun:
    def __init__(self, screen):
        """ Конструктор класса gun
        """
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet, targets
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = YELLOW
        else:
            self.color = BLACK

    def draw(self):
        """Отрисовывает пушку"""
        pygame.draw.line(
            self.screen,
            BLACK,
            (10, 450), (10+self.f2_power * math.cos(self.an), 450+self.f2_power * math.sin(self.an)),
            7
        )
        pygame.draw.line(
            self.screen,
            self.color,
            (10, 450), (10+self.f2_power * math.cos(self.an), 450+self.f2_power * math.sin(self.an)),
            5
        )
    
    def power_up(self):
        """Определяет силу выстрела"""
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = YELLOW
        else:
            self.color = GREY


class Target:
    def __init__(self, screen, x = 600, y = 300, r = 10, vx = 0, vy = 0):
        """ Конструктор класса target

        Args:
        x - начальное положение мишени по горизонтали
        y - начальное положение мишени по вертикали
        r - радиус мишени
        vx - скорость мишени по горизонтали
        vy - скорость мишени по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = r
        self.vx = vx
        self.vy = vy
        self.color = choice(GAME_COLORS)
        self.points = 0
        self.live = 1

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(10, 50)
        vx = self.vx = rnd(-10, 10)
        vy = self.vy = rnd(-10, 10)
        color = self.color = RED

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        """Отрисовывает мишень"""
        border = self.r+1
        pygame.draw.circle(
            self.screen,
            BLACK,
            (self.x, self.y),
            border
        )
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )
    def move(self):
        """Переместить мишени по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y -= self.vy
        if self.y + self.r >= HEIGHT:
            self.vy = -self.vy
            self.y = HEIGHT - self.r
        if self.x + self.r >= WIDTH:
            self.vx = -self.vx
            self.x = WIDTH - self.r
        if self.y - self.r <= 0:
            self.vy = -self.vy
            self.y = self.r
        if self.x - self.r <= 0:
            self.vx = -self.vx
            self.x = self.r


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
targets = []

clock = pygame.time.Clock()
gun = Gun(screen)
targets.append(Target(screen))
targets.append(Target(screen))
for i in targets:
    i.new_target()
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    for i in targets:
        i.move()
        i.draw()

    for b in balls:
        b.live -= 1
        if b.live > 0 or (abs(b.vy)>0.0001 and abs(b.vx)>0.0001):
            b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
        for i in targets:
            if b.hittest(i):
                i.hit()
                i.new_target()
    gun.power_up()

pygame.quit()
