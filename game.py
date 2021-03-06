# Python_learning/game.py
import pygame

class SpaceRocks:
    def __init__(self):
        # Initialize pygame and set the title
        pygame.init()
        pygame.display.set_caption("Space Rocks")

        self.screen = pygame.display.set_mode((800,600))

    def main_loop(self):
        while True:
            self._handle_input()
            self._game_logic()
            self._draw()
    
    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

    def _game_logic(self):
        pass

    def _draw(self):
        self.screen.fill((0,0,255))
        pygame.display.flip()