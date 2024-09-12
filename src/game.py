import pygame, sys
from entities.hero import *
from ui.pause import PauseMenu

class Game:
    def __init__(self, screen):
        # Atributos del juego
        self.screen = screen
        # Inicializa el estado del juego
        self.paused = False
        self.pause = PauseMenu(screen)
        # Cargar la imagen de fondo
        background_path = "assets/images/scenes/test_bg.png"
        self.backgroung_image = pygame.image.load(background_path).convert_alpha()
        # Inicializa el personaje en la posición (100, 100) con la ruta de la imagen
        self.shield_hero = Shield_hero(name="Aegis", level=5, x=100, y=200, shield="Iron Shield")
        self.sword_hero = Sword_hero(name="Aegis", level=5, x=100, y=100, sword="Iron Shield")

    def toggle_pause(self):
        """Alternar entre juego pausado y reanudado."""
        self.paused = not self.paused

    def handle_quit():
        pygame.quit()
        sys.exit()

    def draw(self):
        """Dibujar todos los elementos en la pantalla."""
        if not self.paused:
            self.screen.blit(self.backgroung_image, (0, 0))
            self.shield_hero.draw(self.screen)
            self.sword_hero.draw(self.screen)
        else:
            self.pause.draw()

    def update(self, keys_pressed):
        """Actualizar el estado del juego."""
        if not self.paused:
            self.shield_hero.update(keys_pressed)
            self.sword_hero.update(keys_pressed)
        else:
            self.pause.update(keys_pressed)