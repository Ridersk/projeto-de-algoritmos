import pygame
import os
import random
import time

red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
colors = [red, green, black]

running = True
posX = 10
posY = 20

pygame.display.set_caption("Test")
screen_width = 720
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()


class Board(object):
    def __init__(self):
        self.board = []
        self.block_width = 20
        self.block_height = 20
        self.width = int(screen_width/self.block_width)
        self.height = int(screen_height/self.block_height)

        self.make_board()

    def make_board(self):
        index = 0
        for i in range(self.height):
            for j in range(self.width):
                block = type('', (), {})()
                block.body = pygame.rect.Rect(
                    (j * self.block_width, i * self.block_height, self.block_width, self.block_height))
                block.color = colors[random.randint(0, len(colors) - 1)]
                block.index = index
                block.visited = False
                self.board.append(block)
                index += 1

    def refresh(self):
        if pygame.mouse.get_pressed()[0]:
            # if left button is clicked
            position = pygame.mouse.get_pos()
            self.selectBlock(position)
        self.draw()

    def draw(self):
        for block in self.board:
            pygame.draw.rect(screen, block.color, block.body)
        pygame.display.update()

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
            use bfs graph
        '''
        list_blocks = []
        old_color = block.color

        def enqueue(block):
            list_blocks.append(block)

        def dequeue():
            list_blocks.pop(0)

        def getEdges(current_block):
            edges = []
            if current_block.index - 1 >= 0 and self.board[current_block.index - 1].color == old_color:
                # block left
                edges.append(self.board[current_block.index - 1])
            if current_block.index + 1 < len(self.board) and self.board[current_block.index + 1].color == old_color:
                # block right
                edges.append(self.board[current_block.index + 1])
            if current_block.index - self.width >= 0 and self.board[current_block.index - self.width].color == old_color:
                # block top
                edges.append(self.board[current_block.index - self.width])
            if current_block.index + self.width < len(self.board) and self.board[current_block.index + self.width].color == old_color:
                # block bottom
                edges.append(self.board[current_block.index + self.width])
            return edges

        enqueue(block)
        while (len(list_blocks) > 0):
            current_block = list_blocks[0]
            current_block.visited = True
            dequeue()
            current_block.color = black
            self.draw()

            # edges of block, left, right, top and bottom
            edges = getEdges(current_block)

            for edge in edges:
                if not edge.visited:
                    enqueue(edge)
            # time.sleep(0.1)
            clock.tick(60)


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

        board.refresh()


if __name__ == '__main__':
    main()
