#main.py
import pygame
from game import Game

def main():
    pygame.init()

    # Определение размеров экрана
    screen_width = 800
    screen_height = 600

    # Создание экрана
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("МЯТА - мания")

    # Создание объекта игры
    game = Game(screen)
    game.show_start_screen()
    clock = pygame.time.Clock()
    FPS = 60

    # Основной цикл игры
    while not game.game_over:
        game.handle_events()
        game.update()
        game.draw()
        pygame.display.flip()
        clock.tick(FPS)

    game.show_game_over_screen()
    pygame.quit()

if __name__ == "__main__":
    main()
