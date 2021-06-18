class Snake:
    import pygame
    from random import randint

    size: int
    pos = tuple
    block_size: int

    def __init__(self, screen, size=4, pos=(100, 100,), block_size=10):
        self.size = size
        self.pos = pos
        self.block_size = block_size
        self.screen = screen
        self.pygame.display.update()

    def draw(self):
        self.pygame.draw.rect(self.screen, (0, 0, 0),
                             (self.randint(200,200), self.randint(200,200), self.block_size, self.block_size))
        for i in range(self.size):

            lst = list(self.pos)
            lst[0] = self.pos[0] + self.block_size
            self.pos = tuple(lst)

            print(self.pos)
            self.pygame.draw.rect(self.screen, (0, 0, 0),
                                  (self.pos[0], self.pos[1], self.block_size, self.block_size))


        self.pygame.display.update()
            #self.screen.fill((255,255,255))

            #break