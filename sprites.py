# sprites.py
import pygame


class Cat(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        cat_image = pygame.image.load("assets/cat.png")
        self.image = pygame.transform.scale(cat_image, (50, 50))  # Установка размера котика
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height - 50)
        self.speed = 5
        self.lives = 3
        self.mint_collected = 0
        self.max_speed = 20
        self.min_speed = 1
        self.current_speed = self.speed
        self.level = 1
        self.screen_width = screen_width
        self.screen_height = screen_height

    def increase_speed(self):
        if self.current_speed < self.max_speed:
            self.current_speed += 1

    def decrease_speed(self):
        if self.current_speed > self.min_speed:
            self.current_speed -= 1

    def increase_level(self):
        self.level += 1

    def decrease_lives(self):
        self.lives -= 1

    def increase_mint(self):
        self.mint_collected += 1

    def reset_mint(self):
        # Сбрасываем счетчик мяты при переходе на следующий уровень
        self.mint_collected = 0

    # В методе update обновим скорость движения
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.current_speed
        if keys[pygame.K_RIGHT] and self.rect.right < self.screen_width:
            self.rect.x += self.current_speed


class Food(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        food_image = pygame.image.load("assets/food.png")  # Замените "assets/food.png" на путь к изображению еды
        self.image = pygame.transform.scale(food_image, (30, 30))  # Установка размера еды
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 5

    def update(self):
        self.rect.y += self.speed


class Heart(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        heart_image = pygame.image.load("assets/heart.png")  # Замените "assets/heart.png" на путь к изображению сердца
        self.image = pygame.transform.scale(heart_image, (30, 30))  # Установка размера сердца
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 5

    def update(self):
        self.rect.y += self.speed


class Thorn(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        thorn_image = pygame.image.load("assets/thorn.png")  # Замените "assets/thorn.png" на путь к изображению колючки
        self.image = pygame.transform.scale(thorn_image, (30, 30))  # Установка размера колючки
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 5

    def update(self):
        self.rect.y += self.speed


class Mint(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        mint_image = pygame.image.load("assets/mint.png")  # Замените "assets/mint.png" на путь к изображению мяты
        self.image = pygame.transform.scale(mint_image, (30, 30))  # Установка размера мяты
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 5

    def update(self):
        self.rect.y += self.speed
