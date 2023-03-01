import random

import pygame.sprite

from pygame_project.data.game_data.constants_data import *


def initialization(number):
    global clock, screen, hero, slimes, counter_healthes, Sprites, Healthes, Slimes, health_img
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_icon(load_image(ICON))
    pygame.display.set_caption(CAPTION)

    Sprites = pygame.sprite.Group()
    Healthes = pygame.sprite.Group()
    Slimes = pygame.sprite.Group()
    clock = pygame.time.Clock()

    BACK = [load_image(r'Hero_moves\back.png'),
            load_image(r'Hero_moves\back_1.png'),
            load_image(r'Hero_moves\back_2.png'),
            load_image(r'Hero_moves\back_3.png'),
            load_image(r'Hero_moves\back_4.png'),
            load_image(r'Hero_moves\back_5.png'),
            load_image(r'Hero_moves\back_6.png')
            ]
    FORWARD = [load_image(r'Hero_moves\forward.png'),
               load_image(r'Hero_moves\forward_1.png'),
               load_image(r'Hero_moves\forward_2.png'),
               load_image(r'Hero_moves\forward_3.png'),
               load_image(r'Hero_moves\forward_4.png'),
               load_image(r'Hero_moves\forward_5.png'),
               load_image(r'Hero_moves\forward_6.png')
               ]
    LEFT = [load_image(r'Hero_moves\left.png'),
            load_image(r'Hero_moves\left_1.png'),
            load_image(r'Hero_moves\left_2.png')
            ]
    RIGHT = [load_image(r'Hero_moves\right.png'),
             load_image(r'Hero_moves\right_1.png'),
             load_image(r'Hero_moves\right_2.png')
             ]
    ALL_MOVES = [BACK, FORWARD, LEFT, RIGHT]

    hero = Hero(ALL_MOVES)
    Hero_x, Hero_y = HEIGHT / 2, WIDTH / 4
    hero.sprite.rect.center = (Hero_x, Hero_y)

    Blue_slime_img = pygame.transform.smoothscale(load_image('Blue_slime.png'), (40, 30))
    Green_slime_img = pygame.transform.smoothscale(load_image('Green_slime.png'), (40, 30))
    Orange_slime_img = pygame.transform.smoothscale(load_image('Orange_slime.png'), (40, 30))
    Pink_slime_img = pygame.transform.smoothscale(load_image('Pink_slime.png'), (40, 30))

    slimes_images = [Blue_slime_img, Green_slime_img, Orange_slime_img, Pink_slime_img]
    slimes = []
    rangee = [15, 20, 25, 30]

    for i in range(rangee[number]):
        slimes.append(Slime(slimes_images[random.randrange(1, 4)]))
        slimes[i].sprite1.rect.x = random.randrange(10, WIDTH - 10)
        slimes[i].sprite1.rect.top = random.randrange(10, HEIGHT - 10)

    counter_healthes = []
    health_img = pygame.transform.scale(load_image('health.png'), (36, 36))
    width = WIDTH
    distance = []
    for i in range(7):
        width -= 37
        distance.append(width)
        counter_healthes.append(Health(health_img))
        counter_healthes[i].sprite.rect.x = distance[i]
        counter_healthes[i].sprite.rect.y = 10


def game():
    global number
    pygame.mixer.music.load('data\sounds\game_background_sound.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.05)
    background = pygame.transform.scale(load_image('game_playgrond.png'), (WIDTH, HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            hero.update(event)

        if len(Healthes.sprites()) == 0:

            line = 'YOU DIED!'
            font = pygame.font.Font(None, 100)
            number = 0
            screen.fill(BLACK)
            draw_text(WIDTH // 2, HEIGHT // 2 - 100, line, font, RED, screen)
            pygame.display.flip()
            pygame.time.wait(2500)
            pygame.mixer.stop()

            return
        elif len(slimes) == 0:
            line1 = 'YOU WIN!'
            line2 = "next wave"
            font = pygame.font.Font(None, 100)
            screen.fill(BLACK)
            draw_text(WIDTH // 2, HEIGHT // 2 - 100, line1, font, YELLOW, screen)
            draw_text(WIDTH // 2, HEIGHT // 2 - 30, line2, font, YELLOW, screen)
            if number == 3:
                draw_text(WIDTH // 2, HEIGHT // 2 + 40, "ТЫ натуральный КРАСАУЧИК !", font, BLUE, screen)
            pygame.display.flip()
            pygame.time.wait(2500)
            pygame.mixer.stop()
            return

        else:
            for i in slimes:
                i.update(hero.sprite.rect.center)
            screen.blit(background, (0, 0))
            Sprites.draw(screen)
            Slimes.draw(screen)
            Healthes.draw(screen)
            pygame.display.flip()
            clock.tick(FPS)


def start_screen():
    pygame.mixer.music.load(r'data\sounds\background_sound.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.05)
    intro_text = ["",
                  "Правила игры",
                  "W, A, S, D - чтобы двигаться,",
                  "ПРОБЕЛ - чтобы бить,",
                  "ESCAPE - чтобы выйти",
                  "Удачи, Evolver!!!"]

    fon = pygame.transform.scale(load_image('fon.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 40)
    text_coord = HEIGHT // 2 - 100
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = WIDTH // 2
        text_coord += intro_rect.height
        draw_text(intro_rect.x + 1, intro_rect.y - 1, line, font, BLACK, screen)
        draw_text(intro_rect.x + 2, intro_rect.y - 2, line, font, BLACK, screen)
        draw_text(intro_rect.x - 1, intro_rect.y + 1, line, font, BLACK, screen)
        draw_text(intro_rect.x - 1, intro_rect.y + 1, line, font, BLACK, screen)
        draw_text(intro_rect.x, intro_rect.y, line, font, WHITE, screen)

    logo_image = load_image('logo.png')
    logo = pygame.transform.scale(logo_image, (logo_image.get_width() // 2.5, logo_image.get_height() // 2.5))
    draw_text(HEIGHT // 2, HEIGHT - 60, "Для начала игры нажмите ENTER", font, GOLD, screen)
    screen.blit(logo, (WIDTH // 2 - 190, HEIGHT // 2 - 200))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.stop()
                    return
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

        pygame.display.flip()
        clock.tick(FPS)


class Hero(pygame.sprite.Sprite):
    def __init__(self, images):
        super().__init__()
        self.back = images[0]
        self.forward = images[1]
        self.left = images[2]
        self.right = images[3]
        self.move = 0

        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = images[1][0]
        self.sprite.rect = self.sprite.image.get_rect()

        self.sword_sprite = pygame.sprite.Sprite()
        self.sword_sprite.image = load_image(ICON)
        self.sword_sprite.rect = self.sword_sprite.image.get_rect()

        self.mask = pygame.mask.from_surface(self.sprite.image)
        Sprites.add(self.sprite, self.sword_sprite)

        self.flag = False
        self.counter = 0
        self.counter1 = 0
        self.count = 5

    def update(self, event):
        keys = pygame.key.get_pressed()
        if self.flag:
            if keys[pygame.K_w]:
                if self.counter1 == 6:
                    self.counter1 = 0
                self.counter1 += 1
                self.sprite.image = self.back[self.counter1]
                self.sprite.rect.y -= 5
                self.move = 'w'
            elif keys[pygame.K_s]:
                if self.counter1 == 6:
                    self.counter1 = 0
                self.counter1 += 1
                self.sprite.image = self.forward[self.counter1]
                self.sprite.rect.y += 5
                self.move = 's'
            if keys[pygame.K_a]:
                if self.counter == 2:
                    self.counter = 0
                self.counter += 1
                if self.counter == 1:
                    self.sprite.image = self.left[1]
                if self.counter == 2:
                    self.sprite.image = self.left[2]
                self.sprite.rect.x -= 10
                self.move = 'a'
            elif keys[pygame.K_d]:
                if self.counter == 2:
                    self.counter = 0
                self.counter += 1
                if self.counter == 1:
                    self.sprite.image = self.right[1]
                if self.counter == 2:
                    self.sprite.image = self.right[2]
                self.sprite.rect.x += 10
                self.move = 'd'

        keyses = sum(keys)
        if keys[pygame.K_SPACE] and self.count == 5 and keyses > 1:
            self.count = 0
            angle = 0

            while angle < 45:
                rotated_image = pygame.transform.rotate(self.sword_sprite.image, angle)
                angle += 5
                if self.move == 'w':
                    rect_y = self.sprite.rect.y - angle
                    screen.blit(rotated_image, (self.sprite.rect.x, rect_y))
                if self.move == 's':
                    rect_y = self.sprite.rect.y + angle
                    screen.blit(rotated_image, (self.sprite.rect.x, rect_y))
                if self.move == 'a':
                    rect_x = self.sprite.rect.x - angle
                    screen.blit(rotated_image, (rect_x, self.sprite.rect.y))
                if self.move == 'd':
                    rect_x = self.sprite.rect.x + angle
                    screen.blit(rotated_image, (rect_x, self.sprite.rect.y))
                pygame.display.flip()
            result = pygame.sprite.spritecollide(hero.sword_sprite, Slimes, dokill=False,
                                                 collided=pygame.sprite.collide_rect_ratio(1.7))
            for i in result:
                i.kill()
                for j in slimes:
                    if j.sprite1.rect == i.rect:
                        slimes.remove(j)
        if self.count != 5:
            self.count += 1

        if event.type == pygame.KEYDOWN:
            self.flag = True
        elif event.type == pygame.KEYUP:
            self.counter = 0
            self.flag = False
        self.sword_sprite.rect.center = self.sprite.rect.center


class Slime(pygame.sprite.Sprite):
    def __init__(self, image):
        super(Slime, self).__init__()
        self.sprite1 = pygame.sprite.Sprite()
        self.sprite1.image = image
        self.sprite1.rect = self.sprite1.image.get_rect()
        self.speed = 1
        self.mask = pygame.mask.from_surface(self.sprite1.image)
        Slimes.add(self.sprite1)
        self.count = 30

    def update(self, hero_rect):
        if pygame.sprite.collide_rect(self.sprite1, hero.sprite):
            if len(Healthes.sprites()) > 0 and self.count == 30:
                Healthes.sprites()[-1].kill()
                the_damage_ouch_sound.play()
                self.count = 0

            self.count += 1
        else:
            hero_x, hero_y = hero_rect
            if hero_x > self.sprite1.rect.x:
                self.sprite1.rect.x += self.speed
            else:
                self.sprite1.rect.x -= self.speed

            if hero_y > self.sprite1.rect.y:
                self.sprite1.rect.y += self.speed
            else:
                self.sprite1.rect.y -= self.speed


class Health(pygame.sprite.Sprite):
    def __init__(self, image):
        super(Health, self).__init__()
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = image
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.center = (WIDTH - 10, 10)
        Healthes.add(self.sprite)

def main_algorithm():
    global number
    number = -1
    while True:
        number += 1
        if number == 4:
            number = 0
        initialization(number)
        start_screen()
        game()
