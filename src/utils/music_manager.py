# music_manager.py
import pygame
import os

class MusicManager:
    def __init__(self, bgm_directory='assets/sounds/bgm'):
        """Inicializa el administrador de música."""
        self.bgm_directory = bgm_directory  # Directorio donde se almacenan las pistas de BGM
        pygame.mixer.init()  # Inicializar el mezclador de música
        self.current_bgm = None  # Para almacenar la música actual
    
    def play_bgm(self, filename, volume=0.5, loop=-1):
        """Reproduce una pista de BGM desde un archivo."""
        bgm_path = os.path.join(self.bgm_directory, filename)
        if bgm_path != self.current_bgm:  # Cambiar solo si la pista es diferente
            pygame.mixer.music.load(bgm_path)
            pygame.mixer.music.play(loop)
            pygame.mixer.music.set_volume(volume)
            self.current_bgm = bgm_path  # Almacenar la pista actual

    def stop_bgm(self):
        """Detiene la música de fondo."""
        pygame.mixer.music.stop()
        self.current_bgm = None

    def set_volume(self, volume):
        """Ajusta el volumen de la música."""
        pygame.mixer.music.set_volume(volume)
