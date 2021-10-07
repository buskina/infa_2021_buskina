import pygame
import numpy as np
from random import *
from pygame.draw import *

pygame.init()

FPS = 1
screen = pygame.display.set_mode((450, 650))

def clo(n):
    for i in range(n):
        "если будет скучно, можешь придумать способ размыть облака как в оригинальной картинке (17)"
        ellipse(clouds, (255,255,255,randint(10,120)), (randint(-100,350), randint(-100, 275), randint(100,500), randint(10,30)))
        ellipse(clouds, (37,37,37,randint(10,150)), (randint(-100,350), randint(-100, 275), randint(100,500), randint(10,30)))

def ellipse_series(surface, color, x_left, y_top, width, height, scale = 1):
    """
    Draws a sequence of ellipses with given colors and positions on the same surface
    
    :param surface: Surface to draw ellipes on
    :param x_left:  Array of the X coordinates of the leftmost points of the ellipses
    :param y_top:   Array of the Y coordinates of the highest points of the ellipses
    :param width:   Width array
    :param height:  Height array
    :param scale:   Scale factor of each ellipse

    """
    for c, x, y, w, h in zip(color, x_left, y_top, width, height):
        ellipse(surface, c, (x * scale, y * scale, w * scale, h * scale))

def spaceship(x, y, scale = 1):
    """
    Draws spaceship from the point (x, y)

    :param x: X coordinate of a top left corner of a drawing surface
    :param y: Y coordinate of a top left corner of a drawing surface
    :param scale: Scale of the drawing

    """

    # Main surface
    spaceship_surface = pygame.Surface((100 * scale, 100 * scale), pygame.SRCALPHA)

    # Colors
    WHITE      = (255, 255, 255)
    LIGHT      = (200, 200, 200, 150)
    LIGHT_GRAY = (200, 200, 200)
    DARK_GRAY  = (100, 100, 100)

    # Trianglular transparent ray of the spaceship
    vertices = [(10, 90), (50, 20), (90, 90)]
    polygon(spaceship_surface, LIGHT, [(x * scale, y * scale) for x, y in vertices])

    # Fuselage shape
    color  = [DARK_GRAY, LIGHT_GRAY]
    x_left = [10,        20]
    y_top  = [0,         0]
    width  = [90,        70]
    height = [30,        20]
    ellipse_series(spaceship_surface, color, x_left, y_top, width, height, scale)

    # Rivets on the fuselage
    color  = [WHITE] * 6
    x_left = [15, 28, 44, 87, 74, 58]
    y_top  = [13, 19, 22, 13, 19, 22]
    width  = [8] * 6
    height = [6] * 6
    ellipse_series(spaceship_surface, color, x_left, y_top, width, height, scale)
    
    # Adding surface to the drawing
    screen.blit(spaceship_surface, (x,y))

def alien(x, y, k = 1, flip = False):
    """
    Draws a scalable alien which can be mirrored along Y axis
    
    :param flip: True if alien should be mirrored, False else
    :param x: X coordinate of the top left corner of the drawing surface
    :param y: Y coordinate or the top left corner of the drawing surface
    :param k: Scale of the alien

    """ 
    
    # Main surface
    alien = pygame.Surface((100*k, 200*k), pygame.SRCALPHA)
    
    #Туловище и ноги, одинаковые фигуры рисуются последовательно
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
    #Второй рог
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
    #Глаза
    circle(alien, (0,0,0), (30*k,76*k), 7*k)
    circle(alien, (0,0,0), (50*k,77*k), 6*k)
    circle(alien, (255,255,255), (33*k,79*k), 2*k)
    circle(alien, (255,255,255), (52*k,79*k), 2*k)
    #Яблоко
    ellipse(alien, (255,0,0), (72*k,92*k,20*k,20*k))
    ellipse(alien, (50,170,0), (82*k,77*k,3*k,10*k))
    pygame.draw.arc(alien, (64,4,4), (77*k,87*k,10*k,10*k), -np.pi/8, 5*np.pi/8, 2)

    if flip: 
        alien = pygame.transform.flip(alien, True, False)
    screen.blit(alien, (x,y))

#Фон
rect(screen, (34, 43, 0), (0, 325, 450, 325))
rect(screen, (0, 34, 43), (0, 0, 450, 325))
circle(screen, (240,240,230), (300, 150), 60)
clouds = pygame.Surface((450, 650), pygame.SRCALPHA)
clo(20)
screen.blit(clouds, (0,0))

#Объекты
spaceship(200, 300, scale = 0.5)
spaceship(300, 280, scale = 1)
spaceship(0, 225, scale = 2)

alien(100, 280, k = 0.4, flip = True)
alien(50, 330, k = 0.4, flip = True)
alien(140,330, k = 0.4)
alien(100, 380, k = 0.8, flip = True)
alien(250, 320, k = 1.5)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    pygame.display.update()


pygame.quit()