import pygame
import numpy as np
from random import *
from pygame.draw import *

pygame.init()

FPS = 10
screen = pygame.display.set_mode((450, 650))

def clouds(surface, n):
    """
    Draws n pairs of dark and light transparent clouds

    :param surface: Surface to draw clouds on
    :param n: Number of pairs of clouds to draw

    """
    for i in range(n):
        # TODO: blur clouds
        LIGHT = (255, 255, 255, randint(10, 120))
        DARK  = ( 37,  37,  37, randint(10, 150))
        ellipse(surface, LIGHT, (randint(-100,350), randint(-100, 275), randint(100,500), randint(10,30)))
        ellipse(surface,  DARK, (randint(-100,350), randint(-100, 275), randint(100,500), randint(10,30)))


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


def alien(x, y, scale = 1, flip = False):
    """
    Draws a scalable alien which can be mirrored along Y axis
    
    :param flip: True if alien should be mirrored, False else
    :param x: X coordinate of the top left corner of the drawing surface
    :param y: Y coordinate or the top left corner of the drawing surface
    :param k: Scale of the alien

    """ 
    
    # Main surface
    alien = pygame.Surface((100 * scale, 200 * scale), pygame.SRCALPHA)
    
    # Colors
    SKIN  = (255, 255, 200)
    WHITE = (255, 255, 255)
    BLACK = (  0,   0,   0)
    RED   = (255,   0,   0)
    GREEN = ( 50, 170,   0)
    BROWN = ( 64,   4,   4)

    # Body and legs
    color  = [SKIN] * 7
    x_left = [24,  15,  40,  12,  42,   0,  47]
    y_top  = [95, 136, 145, 155, 165, 172, 182]
    width  = [25,  16,  16,  10,  10,  16,  16]
    height = [65,  25,  25,  25,  25,  16,  16]
    ellipse_series(alien, color, x_left, y_top, width, height, scale)
    
    # Hands
    color  = [SKIN] * 6
    x_left = [  7,  50,   7,  62, 12, 42]
    y_top  = [110, 110, 120, 110, 95, 97]
    width  = [ 12,  12,   7,  20, 16, 16]
    height = [ 10,  10,   9,   8, 16, 16]
    ellipse_series(alien, color, x_left, y_top, width, height, scale)
    
    # Horns; first 4 ellipses are the left horn, last 5 are another one
    color  = [SKIN] * 9
    x_left = [0,  5,  10, 15, 81, 73, 63, 52, 55]
    y_top  = [37, 47, 53, 60, 45, 45, 48, 60, 58]
    width  = [15, 10,  8,  5, 12,  7,  8,  6,  8]
    height = [10,  7,  9,  9, 15,  6,  8,  8,  4]
    ellipse_series(alien, color, x_left, y_top, width, height, scale)
      
    # Head
    color = [SKIN] * 6
    x_left = [12, 47, 15, 20, 25, 30]
    y_top  = [67, 67, 65, 75, 80, 90]
    width  = [16, 16, 50, 40, 30, 20]
    height = [16, 16, 15, 15, 15, 20]
    ellipse_series(alien, color, x_left, y_top, width, height, scale)

    # Eyes
    color    = [BLACK, BLACK, WHITE, WHITE]
    x_center = [30, 50, 33, 52]
    y_center = [76, 77, 79, 79]
    radius   = [7,   6,  2,  2]
    for c, _x, _y, r in zip(color, x_center, y_center, radius):
        # names _x and _y are chosen so not to confuse with params
        circle(alien, c, (_x * scale, _y * scale), r * scale)

    # Apple
    color  = [RED, GREEN]
    x_left = [72, 82]
    y_top  = [92, 77]
    width  = [20,  3]
    height = [20, 10]
    ellipse_series(alien, color, x_left, y_top, width, height, scale)
    
    pygame.draw.arc(alien, BROWN,
        (77 * scale, 87 * scale, 10 * scale, 10 * scale),
        -np.pi / 8, 5 * np.pi / 8, 2)

    # Mirroring the alien if needed
    if flip: 
        alien = pygame.transform.flip(alien, True, False)
    
    # Adding surface to the drawing
    screen.blit(alien, (x,y))


def background():
    """
    Draws background with clouds

    """
    # Background
    SKY    = ( 0, 34, 43)
    GROUND = (34, 43,  0)
    rect(screen, GROUND, (0, 325, 450, 325))
    rect(screen,    SKY, (0,   0, 450, 325))
    circle(screen, (240, 240, 230), (300, 150), 60)
    
    # Clouds
    clouds_surface = pygame.Surface((450, 650), pygame.SRCALPHA)
    clouds(clouds_surface, 20)
    screen.blit(clouds_surface, (0, 0))


def picture():
    """
    Draws spaceships, aliens and the background with clouds

    """
    background()
    
    spaceship(200, 300, scale = 0.5)
    spaceship(300, 280, scale = 1)
    spaceship(  0, 225, scale = 2)

    alien(100, 280, scale = 0.4, flip = True)
    alien( 50, 330, scale = 0.4, flip = True)
    alien(140, 330, scale = 0.4)
    alien(100, 380, scale = 0.8, flip = True)
    alien(250, 320, scale = 1.5)


picture()

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