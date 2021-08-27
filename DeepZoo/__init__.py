
from pygame import *
import numpy as np
from skimage import io as io
import os
import matplotlib.pyplot as plt
from skimage.util import view_as_blocks
import pygame as pg
global screen,clock

def plot(x):
    fig, ax = plt.subplots()
    im = ax.imshow(x, cmap = 'gray')
    ax.axis('off')
    fig.set_size_inches(18, 10)
    plt.show()

def flipimg(x):
    x = np.fliplr(x)
    x = np.rot90(x,k=1,axes=(0,1))
    return x

def get_google_slide(url):
    url_head = "https://docs.google.com/presentation/d/"
    url_body = url.split('/')[5]
    page_id = url.split('.')[-1]
    return url_head + url_body + "/export/png?id=" + url_body + "&pageid=" + page_id

def blit_array(b,xy):
    screen.blit(pg.surfarray.make_surface(b*1.0),(xy[0],xy[1]))
    
fps = 60
clock = pg.time.Clock()

import pygame
import numpy as np
from pygame import surfarray

def setup(h,w):
    return pygame.display.set_mode((w, h))
    
    
def draw(display, img)
    surfarray.blit_array(display, img)

