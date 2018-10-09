import pygame
from maze import Maze
from eventloop import EventLoop


class Game:
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 740))
        pygame.display.set_caption("PacMan Portal")

        self.maze = Maze(self.screen, mazefile='maze_layout.txt', brickfile='maze_block', portalfile='portal',
                         shieldfile='shield', pointfile='powerpoint')

    def __str__(self):
        return 'Game(PacMan Portal), maze=' + str(self.maze) + ')'

    def play(self):
        eloop = EventLoop(finished=False)
        while not eloop.finished:
            eloop.check_events()
            self.update_screen()

    def update_screen(self):
        self.screen.fill(Game.BLACK)
        self.maze.blitme()
        pygame.display.flip()


game = Game()
game.play()
