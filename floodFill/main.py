import pygame
import os

green = (0, 255, 0)
black = (0, 0, 0)
running = True
posX = 10
posY = 20

pygame.display.set_caption("Test")
screen_width = 720
screen_heigh = 480
screen = pygame.display.set_mode((screen_width, screen_heigh))
clock = pygame.time.Clock()


class Board(object):
    def __init__(self):
        self.board = []
        self.make_board()

    def make_board(self):
        for i in range(10):
            for j in range(10):
                self.board.append(pygame.rect.Rect(
                    (j * 20 + 5, i * 20 + 5, 20, 20)))

    def draw(self):
        for block in self.board:
            pygame.draw.rect(screen, black, block)


def main():
    global running
    running = True
    pygame.init()

    board = Board()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill((255, 255, 255))

        board.draw()
        pygame.display.update()

        clock.tick(40)


if __name__ == '__main__':
    main()
