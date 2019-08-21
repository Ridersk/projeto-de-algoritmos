import pygame
import os
import random

red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
colors = [red, green, black]

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
        size_board = 20

        for i in range(size_board):
            for j in range(size_board):
                block = type('', (), {})()
                block.body = pygame.rect.Rect((j * 20 + 5, i * 20 + 5, 20, 20))
                block.color = colors[random.randint(0, len(colors) - 1)]
                self.board.append(block)

    def draw(self):
        if pygame.mouse.get_pressed()[0]:
            # if left button is clicked
            position = pygame.mouse.get_pos()
            print(position)
            self.selectBlock(position)
        for block in self.board:
            pygame.draw.rect(screen, block.color, block.body)

    def selectBlock(self, position):
        psx = position[0]
        psy = position[1]
        for block in self.board:
            if (psx > block.body.left and psx < block.body.right and psy > block.body.top and psy < block.body.bottom):
                self.paint(block)
                break

    def paint(self, block):
        '''
            Paint similar color blocks like a flood fill graph
        '''
        block.color = black


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
