# game.py
import pygame
import sys
from sprites import Cat, Food, Heart, Thorn, Mint
from levels import Level1
from utils import load_image


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.game_over = False
        self.cat = Cat(screen.get_width(), screen.get_height())
        self.level = Level1(self.cat)  # Передаем cat в Level1
        self.victory_level = 10  # Уровень победы

        # Создание текстовых поверхностей для отображения информации о жизнях и мяте
        self.font = pygame.font.Font(None, 36)
        self.lives_text = self.font.render("", True, (255, 0, 0))
        self.mint_text = self.font.render("", True, (0, 255, 0))

        # Загрузка данных (изображений, звуков и т.д.)
        self.load_data()

        # Инициализация начального состояния
        self.init_state()

    def init_state(self):
        # Установка начальных координат кота
        self.cat.rect.center = (self.screen.get_width() // 2, self.screen.get_height() - 50)

        # Добавление кота в группу спрайтов
        self.level.all_sprites.add(self.cat)

        # Инициализация первого уровня
        self.level.init_level()

        # Другие инициализации, если необходимо
        # ...

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

    def update(self):
        self.level.update()
        self.cat.update()

        # Обработка столкновений
        self.level.handle_collision(self.cat)

        # Проверка условий завершения игры
        if self.level.check_game_over(self.cat):
            self.game_over = True
        elif self.level.difficulty >= self.victory_level:
            self.game_over = True
            self.show_victory_screen()  # Показываем экран победы

        # Увеличение сложности уровня
        # if self.cat.mint_collected >= 50 * (self.level.mint_banks + 1):
        #    self.level.increase_difficulty()

        # Обновление текстовых поверхностей для отображения актуальной информации
        self.lives_text = self.font.render(f"Lives: {self.level.cat.lives}", True, (255, 0, 0))
        self.mint_text = self.font.render(f"Mint: {self.level.cat.mint_collected}", True, (0, 255, 0))
        self.speed_text = self.font.render(f"Speed: {self.cat.current_speed}", True, (255, 0, 255))
        self.level_text = self.font.render(f"Level: {self.cat.level}", True, (0, 0, 255))

    def draw(self):
        self.screen.fill((255, 255, 255))  # Очистка экрана

        # Отрисовка уровня и кота
        self.level.draw(self.screen)

        # Отображение жизней и мяты
        self.screen.blit(self.lives_text, (10, 10))
        self.screen.blit(self.mint_text, (10, 50))
        self.screen.blit(self.speed_text, (10, 90))
        self.screen.blit(self.level_text, (10, 130))

        pygame.display.flip()
        self.clock.tick(30)  # Устанавливаем частоту кадров

    def show_start_screen(self):
        # Отображение стартового экрана
        font = pygame.font.Font(None, 36)
        text = font.render("Press any key to start", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        waiting_for_key = True
        while waiting_for_key:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    waiting_for_key = False

    def show_game_over_screen(self):
        # Отображение текста "Конец игры" на экране
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over", True, (255, 0, 0))
        text_rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(3000)  # Пауза перед завершением игры

        # код для завершения программы
        pygame.quit()
        sys.exit()

    def show_victory_screen(self):
        # Отображение текста "ПОБЕДА!" на экране
        font = pygame.font.Font(None, 36)
        text = font.render("ПОБЕДА!", True, (0, 255, 0))  # Зеленый цвет для текста победы
        text_rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(3000)  # Пауза перед завершением игры

        # код для завершения программы
        pygame.quit()
        sys.exit()

    def load_data(self):
        # Загрузка изображений
        self.cat.image = load_image("assets/cat.png", target_size=(50, 50))  # Пример размера
        print("Cat image loaded successfully!")
        self.level.food_image = load_image("assets/food.png", target_size=(50, 50))  # Пример размера
        print("Cat image loaded successfully!")
        self.level.heart_image = load_image("assets/heart.png", target_size=(50, 50))  # Пример размера
        print("Cat image loaded successfully!")
        self.level.thorn_image = load_image("assets/thorn.png", target_size=(50, 50))  # Пример размера
        print("Cat image loaded successfully!")
        self.level.mint_image = load_image("assets/mint.png", target_size=(50, 50))  # Пример размера
        print("Cat image loaded successfully!")

        # Другие загрузки данных (например звуки)
