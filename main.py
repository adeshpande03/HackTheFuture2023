import random
from spaceship import *
import pygame
import os

pygame.init()
WIDTH, HEIGHT = 600, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaceship Game")

SPEED = 3

BACKGROUND = pygame.image.load("space-bg.jpg")
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))

SPACESHIP = pygame.image.load("spaceship.png")
SPACESHIP = pygame.transform.scale(SPACESHIP, (40, 40)).convert_alpha()

HEART = pygame.transform.scale(pygame.image.load('heart.png'), (10,10))

ASTEROID = pygame.transform.scale(pygame.image.load("asteroid-v2.png"), (40, 40))
BOOST = pygame.transform.scale(pygame.image.load("boost.png"), (40, 40))
FALLING_OBJ = ["ASTEROID", "BOOST"]

FONT = pygame.font.Font('freesansbold.ttf', 12)

boost_percentage = 0

def draw_background(shooting_stars):
    WIN.blit(BACKGROUND, (0, 0))
    for star in shooting_stars:
        if star.y < HEIGHT:
            star.y += SPEED
            pygame.draw.rect(WIN, (255, 255, 255), star)
        else:
            shooting_stars.remove(star)


def handle_movement(keys_pressed, spaceship):
    if keys_pressed[pygame.K_LEFT] and spaceship.x - SPEED > 0:
        spaceship.x -= SPEED
    if keys_pressed[pygame.K_RIGHT] and spaceship.x + SPEED + spaceship.width < WIDTH:
        spaceship.x += SPEED
    if keys_pressed[pygame.K_DOWN] and spaceship.y + SPEED + spaceship.height < HEIGHT:
        spaceship.y += SPEED
    if keys_pressed[pygame.K_UP] and spaceship.y - SPEED > 0:
        spaceship.y -= SPEED

def draw_text(spaceship):
    lives_text = FONT.render('Lives:', True, (255,255,255))
    boost_text = FONT.render(f'Boost: {boost_percentage}%', True, (255, 255, 255))
    WIN.blit(lives_text, (500, 20))
    WIN.blit(boost_text, (500, 40))
    for life in range(1,spaceship.lives+1):
        WIN.blit(HEART, (lives_text.get_width() + 500 + HEART.get_width()*life, 20))

def handle_falling_obj(falling_obj, spaceship, sp):
    for obj in falling_obj:
        if obj.y + SPEED > HEIGHT:
            falling_obj.remove(obj)
        elif obj.colliderect(spaceship):
            sp.update_lives()
            falling_obj.remove(obj)
        else:
            obj.y += SPEED


def draw_game(spaceship, shooting_stars, falling_obj, sp):
    draw_background(shooting_stars)
    WIN.blit(SPACESHIP, (spaceship.x, spaceship.y))
    handle_falling_obj(falling_obj, spaceship, sp)
    for obj in falling_obj:
        WIN.blit(ASTEROID, (obj.x, obj.y))
    draw_text(sp)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    shooting_stars = []
    falling_obj = []
    spaceship_rect = pygame.Rect(
        WIDTH / 2, HEIGHT - 70, SPACESHIP.get_width(), SPACESHIP.get_height()
    )
    spaceship = Spaceship()
    for x in range(10, WIDTH, 25):
        if x % 2 == 0:
            y = 20
        else:
            y = 0
        star = pygame.Rect(x, y, 1, 18)
        shooting_stars.append(star)

    while run:
        clock.tick(60)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        if len(falling_obj) < 20:
            obj = pygame.Rect(
                random.randint(0, WIDTH),
                random.randint(-WIDTH, 0),
                ASTEROID.get_width(),
                ASTEROID.get_height(),
            )
            falling_obj.append(obj)
        handle_movement(keys_pressed, spaceship_rect)
        draw_game(spaceship_rect, shooting_stars, falling_obj, spaceship)
        if spaceship.lives == 0:
            run = False

    pygame.quit()


if __name__ == "__main__":
    main()
