import pygame
import numpy as np
from pygame.draw import *

def cir(c,x,y):
    circle(screen, (0, 0, 0), (x, y), 11)
    circle(screen, c, (x, y), 10)

def sun(d,x,y):
    a=[]
    for i in range (0,8,1):
        a.append((x+10*np.sin(i*np.pi/4),y+10*np.cos(i*np.pi/4)))
        a.append((x+15*np.sin(np.pi/8+i*np.pi/4), y+15*np.cos(np.pi/8+i*np.pi/4)))
    polygon(screen, d, a)

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (0, 255, 255), (0, 0, 360, 120))
rect(screen, (0, 155, 0), (0, 120, 360, 140))
rect(screen, (0, 0, 0), (39, 99, 82, 62))
rect(screen, (184, 90, 18), (40, 100, 80, 60))
rect(screen, (255, 125, 26), (64, 114, 32, 32))
rect(screen, (30, 148, 130), (65, 115, 30, 30))
polygon(screen, (0, 0, 0), [(38,101), (80,59),
                               (122,101), (38,101)])
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

cir(w, 180, 40)
cir(w, 190, 40)
cir(w, 200, 40)
cir(w, 210, 40)
cir(w, 187, 30)
cir(w, 203, 30)

sun((255,255,0),300,30)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()