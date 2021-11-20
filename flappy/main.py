import time
import pygame


class Flappybird:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/bird.png")
        self.x = 170
        self.y = 300

    def draw_bird(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

class Game:
    def __init__(self):
        self.surface = pygame.display.set_mode((400, 600))
        self.bg = pygame.image.load("resources/bg.jpg")
        self.flappy_bird = Flappybird(self.surface)
        self.flappy_bird.draw_bird()


    def draw_bg(self):
        self.surface.blit(self.bg, (-49, 0))

    def bird_jump(self):
        for i in range(1, 30, 3):
            time.sleep(0.02)
            self.flappy_bird.y -= i
            self.draw_bg()
            self.flappy_bird.draw_bird()
        for i in range(1, 30, 3):
            time.sleep(0.026)
            self.flappy_bird.y += i
            self.draw_bg()
            self.flappy_bird.draw_bird()

        pygame.display.flip()


    def run(self):

        running = True
        self.draw_bg()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

                    if event.key == pygame.K_SPACE:
                        self.bird_jump()

            self.flappy_bird.draw_bird()

            pygame.display.flip()

game = Game()
game.run()
