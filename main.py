import random
from spaceship import *
import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaceship Game")

SPEED = 3
OBJECTSPEED = 2

BACKGROUND = pygame.image.load("space-bg.jpg")
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))

SPACESHIP = pygame.image.load("spaceship.png")
SPACESHIP = pygame.transform.scale(SPACESHIP, (40, 40)).convert_alpha()

HEART = pygame.transform.scale(pygame.image.load("heart.png"), (10, 10))

ASTEROID = pygame.transform.scale(pygame.image.load("asteroid-v2.png"), (60, 60))
BOOST = pygame.transform.scale(pygame.image.load("boost.png"), (40, 40))
FALLING_OBJ = ["ASTEROID", "BOOST"]

FONT = pygame.font.Font("freesansbold.ttf", 12)

boost_percentage = 0

def draw_background():
    WIN.blit(BACKGROUND, (0, 0))


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
    score_text = FONT.render(f'Score: {int(spaceship.score)}', True, (255, 255, 255))
    WIN.blit(lives_text, (500, 40))
    WIN.blit(boost_text, (500, 60))
    WIN.blit(score_text, (500,20))

    for life in range(1,spaceship.lives+1):
        WIN.blit(HEART, (lives_text.get_width() + 500 + HEART.get_width()*life, 40))

def handle_falling_obj(falling_obj, spaceship, sp):
    for obj in falling_obj:
        if obj.y + OBJECTSPEED > HEIGHT:
            falling_obj.remove(obj)
        elif obj.colliderect(spaceship):
            sp.update_lives()
            falling_obj.remove(obj)
        else:
            obj.y += OBJECTSPEED


def draw_game(
    spaceship, falling_asteroids, spObj, falling_boost=[], falling_garbage=[]
):
    draw_background()
    WIN.blit(SPACESHIP, (spaceship.x, spaceship.y))
    handle_falling_obj(falling_asteroids, spaceship, spObj)
    for obj in falling_asteroids:
        WIN.blit(ASTEROID, (obj.x, obj.y))
    draw_text(spObj)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    falling_asteroids = []
    falling_boost = []
    falling_garbage = []
    spaceship_rect = pygame.Rect(
        WIDTH / 2, HEIGHT - 70, SPACESHIP.get_width(), SPACESHIP.get_height()
    )
    spaceship = Spaceship()
    asteroid_elapsed = 0
    boost_elapsed = 0
    garbage_elapsed = 0
    speed_timer = 0
    while run:
        spaceship.update_score(0.001)
        clock.tick(60)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        
        

        speed_timer += clock.tick()
        if speed_timer > 300:
            global SPEED
            global OBJECTSPEED
            SPEED += 1
            OBJECTSPEED += 1
            print(SPEED, OBJECTSPEED)
            speed_timer = 0
        asteroid_interval = random.randint(90, 160)/10
        asteroid_tick = clock.tick()
        asteroid_elapsed += asteroid_tick
        if asteroid_elapsed > asteroid_interval:
            obj = pygame.Rect(
                random.randint(0, WIDTH),
                random.randint(-WIDTH, 0),
                ASTEROID.get_width(),
                ASTEROID.get_height(),
            )
            falling_asteroids.append(obj)
            asteroid_elapsed = 0  
            
            

        handle_movement(keys_pressed, spaceship_rect)
        draw_game(spaceship_rect, falling_asteroids, spaceship)
        if spaceship.lives == 0:
            run = False

    pygame.quit()


if __name__ == "__main__":
    main()
