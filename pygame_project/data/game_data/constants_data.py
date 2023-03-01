import pygame
import os
import sys

import tkinter as tk

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
pygame.mixer.pre_init()
pygame.init()

CAPTION = 'Evolver'
FPS = 60
DIRECTORY = 'data\images'
ICON = 'icon.png'
SIZE = WIDTH, HEIGHT = screen_width, screen_height
SCREEN_RECT = (0, 0, WIDTH, HEIGHT)
BLACK = pygame.Color("black")
RED = pygame.Color("red")
WHITE = pygame.Color("white")
BLUE = pygame.Color("blue")
YELLOW = pygame.Color("yellow")
GREEN = pygame.Color("green")
GOLD = pygame.Color("#ffd700")

the_damage_ouch_sound = pygame.mixer.Sound("data\sounds\damage.ogg")
the_death_sound = pygame.mixer.Sound('data\sounds\death.ogg')


def load_image(name, colorkey=None):
    fullname = os.path.join(DIRECTORY, name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image





def draw_text(x, y, string, font, col, window):
    text = font.render(string, True, col)
    textbox = text.get_rect()
    textbox.center = (x, y)
    window.blit(text, textbox)


