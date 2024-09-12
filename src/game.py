import pygame, sys
from entities.hero import *
from ui.pause import PauseMenu

class Game:
    def __init__(self, screen):
        # Atributos del juego
        self.screen = screen
        self.base_resolution = (800, 600)  # Resolución base del juego
        self.game_surface = pygame.Surface(self.base_resolution)  # Superficie base del juego

        # Inicializa el estado del juego
        self.paused = False
        self.pause = PauseMenu(screen)

        # Cargar la imagen de fondo
        background_path = "assets/images/scenes/test_bg.png"
        self.background_image = pygame.image.load(background_path).convert_alpha()

        # Inicializa los personajes
        self.shield_hero = Shield_hero(name="Aegis", level=5, x=100, y=200, shield="Iron Shield")
        self.sword_hero = Sword_hero(name="Aegis", level=5, x=100, y=100, sword="Iron Shield")

    def toggle_pause(self):
        """Alternar entre juego pausado y reanudado."""
        self.paused = not self.paused

    def handle_quit():
        """Salir del juego."""
        pygame.quit()
        sys.exit()

    def draw(self):
        """Dibujar todos los elementos en la pantalla."""

        if not self.paused:
            # Dibujar en la superficie base de 800x600
            self.game_surface.blit(self.background_image, (0, 0))
            self.shield_hero.draw(self.game_surface)
            self.sword_hero.draw(self.game_surface)

            # Obtener el tamaño actual de la ventana
            window_size = self.screen.get_size()

            # Escalar la superficie base a la resolución de la ventana actual
            scaled_surface = pygame.transform.scale(self.game_surface, window_size)

            # Dibujar la superficie escalada en la pantalla
            self.screen.blit(scaled_surface, (0, 0))

        else:
            # Dibujar el menú de pausa
            self.pause.draw()

    def update(self, keys_pressed):
        """Actualizar el estado del juego."""
        if not self.paused:
            # Actualizar el estado de los personajes
            self.shield_hero.update(keys_pressed)
            self.sword_hero.update(keys_pressed)
        else:
            # Actualizar el menú de pausa
            self.pause.update(keys_pressed)
