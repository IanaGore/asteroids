import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    score = Score()

    dt = 0
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r and game_over:
                # Restart game
                return main()

        if not game_over:
            updatable.update(dt)

            for asteroid in asteroids:
                if asteroid.collides_with(player):
                    game_over = True
                    score.update_high_score()

                for shot in shots:
                    if asteroid.collides_with(shot):
                        shot.kill()
                        points = asteroid.split()
                        score.add_points(points)

        screen.fill("black")

        if not game_over:
            for obj in drawable:
                obj.draw(screen)
            score.draw(screen)
        else:
            score.draw_game_over(screen)
            restart_font = pygame.font.Font(None, 36)
            restart_text = restart_font.render("Press R to Restart", True, "white")
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 120))
            screen.blit(restart_text, restart_rect)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
