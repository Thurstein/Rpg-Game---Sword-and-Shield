import pygame
from ui.menu import Menu

class PauseMenu(Menu):
    def __init__(self, screen):
        super().__init__(screen)
        self.screen = screen
        self.options = ["Volver al juego","Inventario", "Volver a título", "Salir del juego"]
        self.max_option_width = self.get_max_option_width()
        # Crea una superficie para la superposición
        self.overlay = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)
        self.overlay.fill((255, 255, 255, 180))  # Fondo blanco con transparencia 180

    def draw_overlay(self):
        """Dibuja la superposición transparente en la pantalla."""
        self.screen.blit(self.overlay, (0, 0))

    def draw(self):
        """Dibuja la superposición y el menú."""
        self.draw_overlay()
        # self.draw_menu()
        self.draw_options_box()
