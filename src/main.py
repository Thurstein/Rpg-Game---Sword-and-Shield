import pygame, sys, os
from pygame.locals import QUIT
from game import Game
from ui.menu import Menu
from ui.pause import PauseMenu
from utils.states import states

# Ajustar el PYTHONPATH para incluir el directorio raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Configuración inicial
def initialize_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)  # Tamaño de la ventana
    pygame.display.set_caption('My RPG Game')
    return screen

def handle_quit():
    pygame.quit()
    sys.exit()

def update_menu(menu, keys_pressed):
    menu.update(keys_pressed)
    menu.draw()

def update_game(game, keys_pressed):
    game.update(keys_pressed)
    game.draw()

def main():
    screen = initialize_game()
    pygame.mixer.init()  # Inicializa el mixer de sonido
    clock = pygame.time.Clock()  # Controla el frame rate
    
    # Inicializa el menú
    menu = Menu(screen)
    pause = PauseMenu(screen)
    game = None  # Inicializamos el juego como None para evitar inicializarlo antes de tiempo

    # Variable de control del estado actual del programa
    in_title = True
    in_pause = False
    waiting_for_key_release = False
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                handle_quit()

        keys_pressed = pygame.key.get_pressed()

        if in_title:
            # Si estamos en el menú de título
            update_menu(menu, keys_pressed)

            if keys_pressed[pygame.K_RETURN] and not waiting_for_key_release:
                waiting_for_key_release = True
                selected_option = menu.get_selected_option()
                if selected_option == menu.options[0]:
                    game = Game(screen)
                    in_title = False
                elif selected_option == menu.options[2]:
                    handle_quit()

        elif in_pause:
            # Si estamos en el menú de pausa, dibujamos solo una vez la superposición y luego actualizamos el menú
            if not game.paused:
                pause.draw_overlay()  # Dibuja el fondo una sola vez al entrar en pausa
                game.toggle_pause()
                in_pause = True
            else:
                pause.update(keys_pressed)
                pause.draw_options_box()

            if keys_pressed[pygame.K_RETURN] and not waiting_for_key_release:
                waiting_for_key_release = True
                selected_option = pause.get_selected_option()
                if selected_option == pause.options[0]:
                    game.toggle_pause()
                    in_pause = False
                    
                elif selected_option == pause.options[2]:
                    game = None
                    in_title = True
                    in_pause = False
                elif selected_option == pause.options[3]:
                    handle_quit()

        else:
            # Si estamos en el juego
            if keys_pressed[pygame.K_ESCAPE]:
                if not game.paused:
                    in_pause = True
                    waiting_for_key_release = False  # Permitir nuevo input al entrar en pausa
            else:
                if game is not None:
                    update_game(game, keys_pressed)
                    waiting_for_key_release = False  # Permitir nuevo input durante el juego

        # Resetea la espera de tecla al soltar `ENTER`
        if not keys_pressed[pygame.K_RETURN]:
            waiting_for_key_release = False

        # Actualiza la pantalla
        pygame.display.flip()

        # Limita el frame rate a 60 FPS
        clock.tick(60)

if __name__ == "__main__":
    main()
