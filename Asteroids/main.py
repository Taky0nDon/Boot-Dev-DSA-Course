import sys

import pygame

from asteroidfield import AsteroidField
from asteroid import Asteroid
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from shot import Shot

from logger import log_state, log_event

VERSION = pygame.version.ver
def main():
    print(f"Starting Asteroids with pygame version: {VERSION}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, drawable, updatable)

    asteroid_field = AsteroidField()
    player = Player(x=SCREEN_WIDTH/2,
                    y=SCREEN_HEIGHT/2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
        screen.fill((0,0,0))
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        iteration_time = game_clock.tick(60)
        dt = iteration_time / 1000


if __name__ == "__main__":
    main()
