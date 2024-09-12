# title_maker.py
import pygame

def draw_text_with_border(screen, text, font, text_color, border_color, border_thickness, center_position):
    # Renderizar el texto principal
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=center_position)

    # Dibujar el borde alrededor del texto
    for dx in range(-border_thickness, border_thickness + 1):
        for dy in range(-border_thickness, border_thickness + 1):
            if dx != 0 or dy != 0:  # Evitar dibujar en el centro
                border_surface = font.render(text, True, border_color)
                border_rect = border_surface.get_rect(center=(center_position[0] + dx, center_position[1] + dy))
                screen.blit(border_surface, border_rect)

    # Dibujar el texto original encima del borde
    screen.blit(text_surface, text_rect)
