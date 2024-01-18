#utils.py
import pygame

def load_image(file_path, target_size=None):
    try:
        image = pygame.image.load(file_path)
        if target_size:
            image = pygame.transform.scale(image, target_size)
        return image
    except pygame.error as e:
        print(f"Error loading image: {file_path}")
        raise SystemExit(e)
