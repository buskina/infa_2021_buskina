import pygame
import numpy as np
from random import *
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((450, 650))

def clo(n):
    for i in range(n):
        ellipse(clouds, (255,255,255,randint(10,120)), (randint(-100,350), randint(-100, 275), randint(100,500), randint(10,30)))
        ellipse(clouds, (37,37,37,randint(10,150)), (randint(-100,350), randint(-100, 275), randint(100,500), randint(10,30)))

def spaceship(k,x,y):
    spsh = pygame.Surface((100*k, 100*k), pygame.SRCALPHA)
    polygon(spsh, (200, 200, 200, 150), [(10*k,90*k), (50*k,20*k),
                               (90*k,90*k), (10*k,90*k)])
    ellipse(spsh, (100,100,100), (10*k,0,90*k,30*k))
    ellipse(spsh, (200,200,200), (20*k,0,70*k,20*k))
    ellipse(spsh, (255,255,255), (15*k,13*k,8*k,6*k))
    ellipse(spsh, (255,255,255), (28*k,19*k,8*k,6*k))
    ellipse(spsh, (255,255,255), (44*k,22*k,8*k,6*k))
    ellipse(spsh, (255,255,255), (87*k,13*k,8*k,6*k))
    ellipse(spsh, (255,255,255), (74*k,19*k,8*k,6*k))
    ellipse(spsh, (255,255,255), (58*k,22*k,8*k,6*k))
    screen.blit(spsh, (x,y))

def alien(k,x,y):
    alien = pygame.Surface((100*k, 200*k), pygame.SRCALPHA)
    #Туловище и ноги
    ellipse(alien, (255,255,200), (24*k,95*k,25*k,65*k))
    ellipse(alien, (255,255,200), (15*k,136*k,16*k,25*k))
    ellipse(alien, (255,255,200), (40*k,145*k,16*k,25*k))
    ellipse(alien, (255,255,200), (12*k,155*k,10*k,25*k))
    ellipse(alien, (255,255,200), (42*k,165*k,10*k,25*k))
    circle(alien, (255,255,200), (8*k,180*k), 8*k)
    circle(alien, (255,255,200), (55*k,190*k), 8*k)
    #Руки
    circle(alien, (255,255,200), (20*k,103*k), 8*k)
    circle(alien, (255,255,200), (50*k,105*k), 8*k)
    ellipse(alien, (255,255,200), (7*k,110*k,12*k,10*k))
    ellipse(alien, (255,255,200), (50*k,110*k,12*k,10*k))
    ellipse(alien, (255,255,200), (7*k,120*k,7*k,9*k))
    ellipse(alien, (255,255,200), (62*k,110*k,20*k,8*k))
    #Рожки
    ellipse(alien, (255,255,200), (0,37*k,15*k,10*k))
    ellipse(alien, (255,255,200), (5*k,47*k,10*k,7*k))
    ellipse(alien, (255,255,200), (10*k,53*k,8*k,9*k))
    ellipse(alien, (255,255,200), (15*k,60*k,5*k,9*k))

    ellipse(alien, (255,255,200), (81*k,45*k,12*k,15*k))
    ellipse(alien, (255,255,200), (73*k,45*k,7*k,6*k))
    ellipse(alien, (255,255,200), (63*k,48*k,8*k,8*k))
    ellipse(alien, (255,255,200), (52*k,60*k,6*k,8*k))
    ellipse(alien, (255,255,200), (55*k,58*k,8*k,4*k))
    #Голова
    circle(alien, (255,255,200), (20*k,75*k), 8*k)
    circle(alien, (255,255,200), (55*k,75*k), 8*k)
    ellipse(alien, (255,255,200), (15*k,65*k,50*k,15*k))
    ellipse(alien, (255,255,200), (20*k,75*k,40*k,15*k))
    ellipse(alien, (255,255,200), (25*k,80*k,30*k,15*k))
    circle(alien, (255,255,200), (40*k,90*k), 10*k)
    circle(alien, (0,0,0), (30*k,76*k), 7*k)
    circle(alien, (0,0,0), (50*k,77*k), 6*k)
    circle(alien, (255,255,255), (33*k,79*k), 2*k)
    circle(alien, (255,255,255), (52*k,79*k), 2*k)

    ellipse(alien, (255,0,0), (72*k,92*k,20*k,20*k))
    ellipse(alien, (50,170,0), (82*k,77*k,3*k,10*k))
    pygame.draw.arc(alien, (64,4,4), (77*k,87*k,10*k,10*k), -np.pi/8, 5*np.pi/8, 2)
    screen.blit(alien, (x,y))

def tralien(k,x,y):
    alien = pygame.Surface((100*k, 200*k), pygame.SRCALPHA)
    #Туловище и ноги
    ellipse(alien, (255,255,200), (24*k,95*k,25*k,65*k))
    ellipse(alien, (255,255,200), (15*k,136*k,16*k,25*k))
    ellipse(alien, (255,255,200), (40*k,145*k,16*k,25*k))
    ellipse(alien, (255,255,200), (12*k,155*k,10*k,25*k))
    ellipse(alien, (255,255,200), (42*k,165*k,10*k,25*k))
    circle(alien, (255,255,200), (8*k,180*k), 8*k)
    circle(alien, (255,255,200), (55*k,190*k), 8*k)
    #Руки
    circle(alien, (255,255,200), (20*k,103*k), 8*k)
    circle(alien, (255,255,200), (50*k,105*k), 8*k)
    ellipse(alien, (255,255,200), (7*k,110*k,12*k,10*k))
    ellipse(alien, (255,255,200), (50*k,110*k,12*k,10*k))
    ellipse(alien, (255,255,200), (7*k,120*k,7*k,9*k))
    ellipse(alien, (255,255,200), (62*k,110*k,20*k,8*k))
    #Рожки
    ellipse(alien, (255,255,200), (0,37*k,15*k,10*k))
    ellipse(alien, (255,255,200), (5*k,47*k,10*k,7*k))
    ellipse(alien, (255,255,200), (10*k,53*k,8*k,9*k))
    ellipse(alien, (255,255,200), (15*k,60*k,5*k,9*k))

    ellipse(alien, (255,255,200), (81*k,45*k,12*k,15*k))
    ellipse(alien, (255,255,200), (73*k,45*k,7*k,6*k))
    ellipse(alien, (255,255,200), (63*k,48*k,8*k,8*k))
    ellipse(alien, (255,255,200), (52*k,60*k,6*k,8*k))
    ellipse(alien, (255,255,200), (55*k,58*k,8*k,4*k))
    #Голова
    circle(alien, (255,255,200), (20*k,75*k), 8*k)
    circle(alien, (255,255,200), (55*k,75*k), 8*k)
    ellipse(alien, (255,255,200), (15*k,65*k,50*k,15*k))
    ellipse(alien, (255,255,200), (20*k,75*k,40*k,15*k))
    ellipse(alien, (255,255,200), (25*k,80*k,30*k,15*k))
    circle(alien, (255,255,200), (40*k,90*k), 10*k)
    circle(alien, (0,0,0), (30*k,76*k), 7*k)
    circle(alien, (0,0,0), (50*k,77*k), 6*k)
    circle(alien, (255,255,255), (33*k,79*k), 2*k)
    circle(alien, (255,255,255), (52*k,79*k), 2*k)

    ellipse(alien, (255,0,0), (72*k,92*k,20*k,20*k))
    ellipse(alien, (50,170,0), (82*k,77*k,3*k,10*k))
    pygame.draw.arc(alien, (64,4,4), (77*k,87*k,10*k,10*k), -np.pi/8, 5*np.pi/8, 2)
    flip = pygame.transform.flip(alien, True, False,)
    screen.blit(flip, (x,y))

rect(screen, (34, 43, 0), (0, 325, 450, 325))
rect(screen, (0, 34, 43), (0, 0, 450, 325))
circle(screen, (240,240,230), (300, 150), 60)
clouds = pygame.Surface((450, 650), pygame.SRCALPHA)
clo(20)
screen.blit(clouds, (0,0))
spaceship(1,300,280)
tralien(0.4,100,280)
spaceship(2,0,225)
tralien(0.4,50,330)
alien(0.4,140,330)
spaceship(0.5,200,300)
alien(1.5,250,320)
tralien(0.8,100,380)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()