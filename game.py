# game.py
import pygame
import random

pygame.init()
pygame.display.set_caption("Yeet Yeet")
screen = pygame.display.set_mode((800, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    # Filling the screen colour with an RGB tuple (Blue)
    screen.fill((135,206,235))
    # Position of a circle on x y coords with radius r
    x = random.randint(10,790)
    y =random.randint(10,590)
    r = random.randint(2,10)
    # Draw the actual circle on surface "screen" with rgb tuple value
    # NOTE: Drawing to buffer
    pygame.draw.circle(screen,(0,0,150), (x,y), r)
    # Flip method takes everything in buffer and displays it to screen all at once
    pygame.display.flip()