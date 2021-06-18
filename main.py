import pygame
import time
import game_classes



if __name__ == '__main__':
    # создаем игру и окно

    WIDTH = 600  # ширина игрового окна
    HEIGHT = 400  # высота игрового окна
    FPS = 30  # частота кадров в секунду

    pygame.init()
    pygame.mixer.init()  # для звука
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My first python")
    clock = pygame.time.Clock()

    snake = game_classes.Snake(screen, 4, (100, 100,))

    # Цикл игры
    running = True
    while running:
        if running:
            screen.fill((255,255,255))
        for event in pygame.event.get():
            # проверить закрытие окна
            if event.type == pygame.QUIT:
                running = False
    
        snake.draw()

        # pygame.display.update()

        time.sleep(1)
