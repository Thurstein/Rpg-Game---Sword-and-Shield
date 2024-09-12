import pygame

class CharacterSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 5  # Velocidad de movimiento por defecto

    def update(self, keys_pressed):
        """Movimiento básico para cualquier personaje."""
        if keys_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys_pressed[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys_pressed[pygame.K_DOWN]:
            self.rect.y += self.speed

    def draw(self, screen):
        """Dibuja el sprite en la pantalla."""
        screen.blit(self.image, self.rect)
