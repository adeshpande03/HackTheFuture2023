import random
from spaceship import *
import pygame
import random
import math
pygame.init()
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaceship Game")

SPEED = 3
OBJECTSPEED = 2
ASTEROID_MASS = 30
BACKGROUND = pygame.image.load("space-bg-v4.jpg")
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))

SPACESHIP = pygame.image.load("spaceship.png")
SPACESHIP = pygame.transform.scale(SPACESHIP, (40, 40)).convert_alpha()

HEART = pygame.transform.scale(pygame.image.load("heart.png"), (10, 10))

GARBAGE = pygame.transform.scale(pygame.image.load("trash-v2.png"), (75, 75))
ASTEROID = pygame.transform.scale(pygame.image.load("asteroid-v2.png"), (60, 60))
BOOST = pygame.transform.scale(pygame.image.load("boost-v3.png"), (40, 40))


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


def asteroid_gravity(falling_asteroids, spaceship):
    asteroid_mass = 50
    xAccel, yAccel = 0, 0
    for asteroid in falling_asteroids:
        G = .08
        degree = math.atan2(asteroid.y - spaceship.y, asteroid.x - spaceship.x)
        radiusSquared = ((asteroid.x - spaceship.x)**2 + (asteroid.y - spaceship.y)**2)
        xAccel += G*ASTEROID_MASS/(radiusSquared) * math.cos(degree)
        yAccel += G*ASTEROID_MASS/(radiusSquared) * math.sin(degree)
    spaceship.x += xAccel
    spaceship.y += yAccel  
    
    
def draw_text(spaceship):
    lives_text = FONT.render('Lives:', True, (255,255,255))
    boost_text = FONT.render(f'Boost: {spaceship.boost}%', True, (255, 255, 255))
    score_text = FONT.render(f'Score: {int(spaceship.score)}', True, (255, 255, 255))
    mass_text = FONT.render(f'Mass: {(spaceship.mass)} kg', True, (255, 255, 255))
    asteroid_mass_text = FONT.render(f'Asteroid Mass: {ASTEROID_MASS} kg', True, (255, 255, 255))
    xPos = 470
    WIN.blit(lives_text, (xPos, 40))
    WIN.blit(boost_text, (xPos, 60))
    WIN.blit(score_text, (xPos,20))
    WIN.blit(mass_text, (xPos, 80))
    WIN.blit(asteroid_mass_text, (xPos, 100))
    for life in range(1,spaceship.lives+1):
        WIN.blit(HEART, (lives_text.get_width() + xPos + HEART.get_width()*life, 40))

def handle_falling_asteroids(falling_obj, spaceship, sp):
    for obj in falling_obj:
        if obj.y + OBJECTSPEED > HEIGHT:
            falling_obj.remove(obj)
        elif obj.colliderect(spaceship):
            if sp.mass <= ASTEROID_MASS:
                sp.update_lives()
            falling_obj.remove(obj)
        else:
            obj.y += OBJECTSPEED
def handle_falling_boost_and_garbage(sp, spaceship, falling_boost = [], falling_garbage = []):
    for obj in falling_boost:
        if obj.y + OBJECTSPEED > HEIGHT:
            falling_boost.remove(obj)
        elif obj.colliderect(spaceship):
            sp.gain_boost()
            falling_boost.remove(obj)
        else:
            obj.y += OBJECTSPEED
    for obj in falling_garbage:
        if obj.y + OBJECTSPEED > HEIGHT:
            falling_garbage.remove(obj)
        elif obj.colliderect(spaceship):
            sp.gain_mass()
            falling_garbage.remove(obj)
        else:
            obj.y += OBJECTSPEED

def draw_game(
    spaceship, falling_asteroids, spObj, falling_boost=[], falling_garbage=[]
):
    draw_background()
    WIN.blit(SPACESHIP, (spaceship.x, spaceship.y))
    handle_falling_asteroids(falling_asteroids, spaceship, spObj)
    handle_falling_boost_and_garbage(spObj, spaceship, falling_boost, falling_garbage)
    for obj in falling_asteroids:
        WIN.blit(ASTEROID, (obj.x, obj.y))
    for obj in falling_boost:
        WIN.blit(BOOST, (obj.x, obj.y))
    for obj in falling_garbage:
        WIN.blit(GARBAGE, (obj.x, obj.y))
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
    SPACE_EVENT = pygame.USEREVENT + 1
    while run:
        global SPEED 
        global OBJECTSPEED
        global ASTEROID_MASS
        spaceship.update_score(0.1)
        clock.tick(60)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
            if e.type == SPACE_EVENT:
                SPEED /= 2
                pygame.time.set_timer(SPACE_EVENT, 0)
                
        keys_pressed = pygame.key.get_pressed()
        
        if keys_pressed[pygame.K_SPACE] and spaceship.boost == 100:
            spaceship.boost = 0
            SPEED *= 2
            pygame.time.set_timer(SPACE_EVENT, 1500)
            
            
            
        # if boost_used:
        #     boost_use_timer += clock.tick()
        #     if boost_use_timer:
        #         SPEED /= 15
        #     boost_used = False

        speed_timer += clock.tick()
        if speed_timer > 350:
            SPEED += 1
            OBJECTSPEED += 1
            ASTEROID_MASS += 15
            speed_timer = 0
            
        
        asteroid_interval = random.randint(1, 2)
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
            
        boost_interval = random.randint(40, 100)/10
        boost_tick = clock.tick()
        boost_elapsed += boost_tick
        if boost_elapsed > boost_interval:
            obj = pygame.Rect(
                random.randint(0, WIDTH),
                random.randint(-WIDTH, 0),
                BOOST.get_width(),
                BOOST.get_height(),
            )
            falling_boost.append(obj)
            boost_elapsed = 0
            
        garbage_interval = random.randint(40, 80)/10
        garbage_tick = clock.tick()
        garbage_elapsed += garbage_tick
        if garbage_elapsed > garbage_interval:
            obj = pygame.Rect(
                random.randint(0, WIDTH),
                random.randint(-WIDTH, 0),
                GARBAGE.get_width(),
                GARBAGE.get_height(),
            )
            falling_garbage.append(obj)
            garbage_elapsed = 0  

        asteroid_gravity(falling_asteroids, spaceship_rect)
        handle_movement(keys_pressed, spaceship_rect)
        draw_game(spaceship_rect, falling_asteroids, spaceship, falling_boost, falling_garbage)
        if spaceship.lives == 0:
            run = False
        print(spaceship.speed)
    pygame.quit()


if __name__ == "__main__":
    main()
