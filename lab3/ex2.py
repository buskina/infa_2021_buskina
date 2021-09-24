import pygame
from pygame.draw import *

def cir(c,x,y):
    circle(screen, (0, 0, 0), (x, y), 11)
    circle(screen, c, (x, y), 10)

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (0, 255, 255), (0, 0, 360, 120))
rect(screen, (0, 155, 0), (0, 120, 360, 140))
rect(screen, (0, 0, 0), (39, 99, 82, 62))
rect(screen, (184, 90, 18), (40, 100, 80, 60))
rect(screen, (255, 125, 26), (64, 114, 32, 32))
rect(screen, (30, 148, 130), (65, 115, 30, 30))
polygon(screen, (0, 0, 0), [(39,99), (81,59),
                               (122,102), (39,99)])
polygon(screen, (255, 0, 0), [(40,100), (80,60),
                               (120,100), (40,100)])
rect(screen, (0, 0, 0), (265, 70, 10, 60))
g=(0, 50, 0)
w=(255, 255, 255)
cir(g, 270, 55)
cir(g, 260, 60)
cir(g, 280, 60)
cir(g, 270, 65)
cir(g, 260, 70)
cir(g, 280, 70)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()