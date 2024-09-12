import pygame, sys, os
from pygame.locals import QUIT
from game import Game
from ui.menu import Menu
from ui.pause import PauseMenu
from utils.music_manager import MusicManager

# Ajustar el PYTHONPATH para incluir el directorio raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Configuración inicial
def initialize_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption('My RPG Game')
    return screen

def handle_events(game):
    """Manejo de eventos globales"""
    for event in pygame.event.get():
        if event.type == QUIT:
            if game:
                game.handle_quit()
            pygame.quit()
            sys.exit()

def update_menu(menu, keys_pressed, waiting_for_key_release, music_manager):
    """Actualiza el menú y la música"""
    menu.update(keys_pressed)
    menu.draw()

    if keys_pressed[pygame.K_RETURN] and not waiting_for_key_release:
        selected_option = menu.get_selected_option()
        if selected_option == menu.options[0]:  # Play
            music_manager.play_bgm('bgm01.mp3', volume=0.5)  # Cambiar música al iniciar juego
            return 'game', True  # Cambia al estado de juego y activa la espera de tecla
        elif selected_option == menu.options[2]:  # Exit
            pygame.quit()
            sys.exit()
    return 'menu', waiting_for_key_release

def update_game(game, keys_pressed):
    """Actualiza y dibuja el juego"""
    game.update(keys_pressed)
    game.draw()
    if keys_pressed[pygame.K_ESCAPE]:
        return 'pause'
    return 'game'

def update_pause(pause, keys_pressed, game, waiting_for_key_release, music_manager):
    """Actualiza el menú de pausa"""
    if not game.paused:
        pause.draw_overlay()
        game.toggle_pause()

    pause.update(keys_pressed)
    pause.draw_options_box()

    if keys_pressed[pygame.K_RETURN] and not waiting_for_key_release:
        selected_option = pause.get_selected_option()
        if selected_option == pause.options[0]:  # Continue
            game.toggle_pause()
            return 'game', True  # Cambiar a estado de juego y activar espera de tecla
        elif selected_option == pause.options[1]:  # Inventory
            print("Inventario seleccionado. Aquí se mostrará el inventario.")
            return 'pause',True
        elif selected_option == pause.options[2]:  # Back to Title
            music_manager.play_bgm('title_bgm01.mp3', volume=0.5)  # Volver a la música del título
            return 'menu', True
        elif selected_option == pause.options[3]:  # Exit
            game.handle_quit()
    return 'pause', waiting_for_key_release

def main():
    screen = initialize_game()
    music_manager = MusicManager()
    clock = pygame.time.Clock()

    # Inicializar los estados
    menu = Menu(screen)
    pause = PauseMenu(screen)
    game = None
    current_state = 'menu'

    # Reproducir música del menú al inicio
    music_manager.play_bgm('title_bgm01.mp3', volume=0.5)

    running = True
    waiting_for_key_release = False  # Variable para evitar repetir la selección con una tecla presionada

    while running:
        handle_events(game)

        keys_pressed = pygame.key.get_pressed()

        if current_state == 'menu':
            current_state, waiting_for_key_release = update_menu(menu, keys_pressed, waiting_for_key_release, music_manager)
            if current_state == 'game':
                game = Game(screen)
        
        elif current_state == 'game':
            current_state = update_game(game, keys_pressed)

        elif current_state == 'pause':
            current_state, waiting_for_key_release = update_pause(pause, keys_pressed, game, waiting_for_key_release, music_manager)

        # Resetea la espera de tecla al soltar `ENTER`
        if not keys_pressed[pygame.K_RETURN]:
            waiting_for_key_release = False

        # Actualizar pantalla
        pygame.display.flip()

        # Limitar a 60 FPS
        clock.tick(60)

if __name__ == "__main__":
    main()
