# levels.py
import pygame
from sprites import Food, Heart, Thorn, Mint
import random


class Level:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.all_sprites = pygame.sprite.Group()
        self.food_sprites = pygame.sprite.Group()
        self.heart_sprites = pygame.sprite.Group()
        self.thorn_sprites = pygame.sprite.Group()
        self.mint_sprites = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.difficulty = 1
        self.mint_banks = 0

    def update(self):
        # Обновление уровня
        self.all_sprites.update()
        self.spawn_objects()

    def increase_difficulty(self):
        # Увеличение сложности уровня
        self.difficulty += 1
        # Дополнительная логика, если нужно

    def spawn_objects(self):
        # Логика появления объектов на экране
        pass

    def draw(self, screen):
        # Отрисовка объектов на экране
        screen.fill((255, 255, 255))  # Замените на ваш цвет фона
        self.all_sprites.draw(screen)

    def handle_collision(self, cat):
        pass
        # Обработка столкновений котика с объектами
        # Реализуйте логику обработки столкновений для Food, Heart, Thorn и Mint
        # ...

    def check_game_over(self, cat):
        # Проверка условий завершения игры (когда у котика заканчиваются жизни)
        if cat.lives <= 0:
            return True
        return False


# Класс Level1, который будет наследоваться от базового класса Level
class Level1(Level):
    def __init__(self, cat):
        super().__init__(cat.screen_width, cat.screen_height)
        self.cat = cat
        self.items = pygame.sprite.Group()
        self.active = False  # Добавленный атрибут
        self.last_update_time = pygame.time.get_ticks()
        self.last_item_time = pygame.time.get_ticks()
        self.item_interval = 500  # Интервал (в миллисекундах) между появлением новых предметов
        self.remaining_items = float('inf')  # Бесконечное количество предметов

    def init_level(self):
        # Устанавливаем self.active в True после добавления всех предметов
        self.active = True

    def spawn_objects(self):
        current_time = pygame.time.get_ticks()

        # Проверяем, прошло ли достаточно времени с момента последнего создания объекта
        if current_time - self.last_update_time >= self.item_interval and self.remaining_items > 0:
            # Создаем новый объект (здесь добавим логику для выбора случайного объекта)
            item_type = random.choice(['food', 'heart', 'thorn', 'mint'])
            item = None

            # Фиксированная координата Y (например, 0)
            y_coordinate = 100

            if item_type == 'food':
                item = Food(random.randint(0, self.screen_width - 30), y_coordinate)
            elif item_type == 'heart':
                item = Heart(random.randint(0, self.screen_width - 30), y_coordinate)
            elif item_type == 'thorn':
                item = Thorn(random.randint(0, self.screen_width - 30), y_coordinate)
            elif item_type == 'mint':
                item = Mint(random.randint(0, self.screen_width - 30), y_coordinate)

            # Выводим координаты для проверки
            print(f"{item_type} coordinates: {item.rect.x}, {item.rect.y}")

            # Добавляем объект в группу
            self.items.add(item)

            # Уменьшаем количество оставшихся предметов
            self.remaining_items -= 1

            # Обновляем время последнего создания объекта
            self.last_update_time = current_time

    def increase_difficulty(self):
        super().increase_difficulty()
        # Увеличиваем скорость падения колючек с каждым новым уровнем
        self.item_interval -= 50
        if self.item_interval < 100:
            self.item_interval = 100  # Устанавливаем минимальный интервал

    def update(self):
        # Обновляем состояние предметов только, если игра активна
        if self.active:
            # Вызываем метод spawn_objects для создания объектов
            self.spawn_objects()

            # Обновляем состояние предметов
            self.items.update()

            # Добавляем объекты в общую группу
            self.all_sprites.add(self.items)

            # Проверяем столкновения и обрабатываем их, как ранее
            collisions = pygame.sprite.spritecollide(self.cat, self.items, True)
            # Обрабатываем столкновения
            for item in collisions:
                if isinstance(item, Mint):
                    # Обработка мяты (например, переход на следующий уровень)
                    self.cat.increase_mint()
                elif isinstance(item, Heart):
                    if self.cat.lives < 3:  # Увеличиваем жизни только если их меньше 3
                        self.cat.lives += 1  # Используем непосредственное увеличение жизней
                elif isinstance(item, Thorn):
                    self.cat.lives -= 1
                    self.cat.decrease_speed()  # Уменьшаем скорость при попадании в колючку
                elif isinstance(item, Food):
                    self.cat.increase_speed()  # Увеличиваем скорость при съедании еды

            # self.handle_collisions()

            # Проверяем, набрано ли достаточно мяты для перехода на следующий уровень
            if self.cat.mint_collected >= 20:
                self.cat.increase_level()
                self.cat.reset_mint()  # Сбрасываем счетчик мяты после перехода на следующий уровень
                self.increase_difficulty()
