# game.py

import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, WHITE
from player import Player
from obstacle import Obstacle

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Simple Game")
        self.clock = pygame.time.Clock()
        self.running = True

        # Create sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()

        # Create player and obstacles
        self.player = Player()
        self.all_sprites.add(self.player)

        obstacle = Obstacle(200, 150, 200, 50)
        self.all_sprites.add(obstacle)
        self.obstacles.add(obstacle)

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.all_sprites.update()

        # Check for collision
        if pygame.sprite.spritecollide(self.player, self.obstacles, False):
            self.running = False

    def draw(self):
        self.screen.fill(WHITE)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def quit(self):
        pygame.quit()

def main():
    print('hi!')

# main()
if __name__ == "__main__":
    main()
