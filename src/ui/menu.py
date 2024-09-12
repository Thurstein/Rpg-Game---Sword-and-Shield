import pygame, os
from utils.title_maker import draw_text_with_border

class Menu:
    def __init__(self, screen):
        self.screen = screen
        # Cargar la fuente personalizada
        self.font_path = os.path.join('assets', 'fonts', 'JMHarkhamRegular.ttf')
        self.font = pygame.font.Font(self.font_path, 50)  # Tamaño 50 para las opciones
        self.title_font = pygame.font.Font(self.font_path, 80)  # Tamaño 80 para el título
        # Atributos del menú de opciones
        self.options = ["Play", "Options", "Exit"]
        self.selected_index = 0
        self.max_option_width = self.get_max_option_width()
        # Cooldown de imputs
        self.cooldown_time = 200  # Tiempo en milisegundos
        self.last_move_time = pygame.time.get_ticks()

    def get_max_option_width(self):
        """Obtiene el ancho en píxeles de la palabra más larga en self.options."""
        max_width = 0
        for option in self.options:
            width, _ = self.font.size(option)  # Obtener ancho y alto de la opción
            if width > max_width:
                max_width = width
        return max_width

    def draw_options_box(self):
        # Dimensiones y estilo del recuadro para las opciones
        box_width, box_height = self.max_option_width+100, 80*len(self.options)  # Tamaño del recuadro
        box_x = (self.screen.get_width() - box_width) // 2
        box_y = (self.screen.get_height() - box_height) // 2

        # Fondo transparente con un gris levemente transparente
        surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
        surface.fill((128, 128, 128, 180))  # Gris traslúcido (RGBA)

        # Borde con un gris claro y grosor de 5 píxeles
        pygame.draw.rect(surface, (200, 200, 200), surface.get_rect(), border_radius=20, width=5)

        # Dibujar el recuadro en la pantalla
        self.screen.blit(surface, (box_x, box_y))

        # Dibujar las opciones del menú de forma centrada
        option_height = self.font.size(self.options[0])[1]  # Altura de una opción
        total_options_height = option_height * len(self.options)  # Altura total de todas las opciones
        start_y = box_y + (box_height - total_options_height) +option_height//3 // 2 # Y inicial para centrar las opciones

        for index, option in enumerate(self.options):
            color = (0, 31, 153) if index == self.selected_index else (4, 224, 0)
            label = self.font.render(option, True, color)
            label_rect = label.get_rect(center=(self.screen.get_width() // 2, start_y + index * option_height))
            self.screen.blit(label, label_rect)
    
    def draw(self):
        # Cargar y escalar la imagen de fondo
        self.background_image = pygame.image.load(os.path.join('assets', 'images', 'scenes', 'bg_title.jpg')).convert_alpha()
        window_size = self.screen.get_size()
        background_image_scaled = pygame.transform.scale(self.background_image, window_size)
        self.screen.blit(background_image_scaled, (0, 0))

        # Dibujar el título con borde negro y centrado
        title_text = "Sword and Shield"
        title_position = (self.screen.get_width() // 2, 100)  # Centrado horizontalmente en la parte superior
        draw_text_with_border(
            self.screen,  # Pasar la pantalla como primer argumento
            title_text,
            self.title_font,
            (255, 255, 255),  # Color blanco para el texto
            (0, 0, 0),  # Color negro para el borde
            3,  # Grosor del borde
            title_position
        )

        # Dibujar el recuadro y las opciones del menú
        self.draw_options_box()

    def update(self, keys_pressed):
        # Obtener el tiempo actual
        current_time = pygame.time.get_ticks()

        # Verificar si el tiempo de espera (cooldown) ha pasado
        if current_time - self.last_move_time > self.cooldown_time:
            # Navegación en el menú
            if keys_pressed[pygame.K_DOWN]:
                self.selected_index = (self.selected_index + 1) % len(self.options)
                self.last_move_time = current_time  # Actualiza el tiempo de la última acción
            elif keys_pressed[pygame.K_UP]:
                self.selected_index = (self.selected_index - 1) % len(self.options)
                self.last_move_time = current_time  # Actualiza el tiempo de la última acción

    def get_selected_option(self):
        """Retorna la opción seleccionada."""
        print(f"Selected option: {self.options[self.selected_index]}")
        return self.options[self.selected_index]
