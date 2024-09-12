import pygame
import numpy as np
from utils.animation_loader import import_folder

class Entity:
    def __init__(self,name,level, x, y):
        # Atributos independientes
        self.name = name
        self.level = level
        self.image_path = "assets/images/players/shield hero/idle/1.png"
        self.image = pygame.image.load(self.image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        # Atributos dependientes del nivel
        self.health = int(30*np.log(self.level)+100)
        self.attack = int(30*np.log(self.level)+10)
        self.defense = int(30*np.log(self.level)+10)
        self.magic = int(30*np.log(self.level)+10)
        self.magic_resistance = int(30*np.log(self.level)+10)
        self.evasion = int(30*np.log(self.level)+10)
        self.speed = int(30*np.log(self.level)+10)
        # Atributos constantes (estadísticas)
        self.movement_speed = 3     
        self.crit_chance = 9
        # Animación
        self.status = 'idle'
        self.frame_index = 0
        self.animation_speed = 0.12
        self.facing_right = True

    # Animación
    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animations):
            self.frame_index = 0
        self.image = pygame.transform.scale(self.animations[int(self.frame_index)], (90, 90))
                # Si está mirando hacia la izquierda, invierte la imagen
        if not self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)

    def draw(self, screen):
        """Dibuja el sprite en la pantalla."""
        screen.blit(self.image, self.rect)

    def damage_dealt(self, enemy, attack_type='physical'):
        # Evasión: El enemigo puede esquivar el ataque
        evasion_roll = np.random.uniform(0, 100)
        if evasion_roll < enemy.evasion:
            print(f"{enemy.name} evaded the attack!")
            return 0
        # Críticos: Posibilidad de golpe crítico
        crit_roll = np.random.uniform(0, 100)
        critical_multiplier = 1.5 if crit_roll < self.crit_chance else 1.0
        # Daño físico o mágico
        if attack_type == 'physical':
            # Para daño físico: se tiene en cuenta la defensa del enemigo
            damage = (self.attack - enemy.defense) * critical_multiplier
        elif attack_type == 'magical':
            # Para daño mágico: se tiene en cuenta la resistencia mágica del enemigo
            damage = (self.attack - enemy.magic_resistance) * critical_multiplier
        # Daño mínimo: asegurarse de que el daño no sea negativo
        damage = int(max(damage, 0)*np.random.uniform(0.9, 1.1))
        return damage

    def show_hero(self):
        print(f"Name: {self.name},\n Level: {self.level},\n Health: {self.health},\n Attack: {self.attack},\n Defense: {self.defense},\n Magic: {self.magic}")

    def is_alive(self):
        return self.health > 0
    
    def is_dead(self):
        return self.health <= 0
        print(self.name,"is dead")
    
    def attacking(self, enemy):
        damage = self.damage_dealt(enemy)
        enemy.health -= damage
        print(f"{self.name} has inflicted {damage} points of damage to {enemy.name}")
        if enemy.is_alive():
            print(f"{enemy.name}'s health is {enemy.health}")
        else:
            enemy.is_dead()

class Shield_hero(Entity):
    def __init__(self,name,level, x, y, shield):
        super().__init__(name,level, x, y)
        # Stats
        self.health = int(50*np.log(self.level)+150)           # Gran salud
        self.attack = int(15*np.log(self.level)+8)             # Ataque bajo
        self.defense = int(40*np.log(self.level)+15)           # Defensa alta
        self.magic = int(20*np.log(self.level)+5)              # Magia baja
        self.magic_resistance = int(30*np.log(self.level)+10)  # Resistencia mágica moderada
        self.evasion = int(5*np.log(self.level)+1)             # Evasión baja
        self.speed = int(10*np.log(self.level)+5)              # Velocidad baja
        self.crit_chance = 10 
        # Shield
        self.shield = shield
        # Animación
        self.animations = import_folder('assets/images/players/shield hero/'+self.status+'/')

    def update(self, keys_pressed):
        """Actualiza la posición en base a las teclas presionadas (movimiento básico)."""
        
        # Por defecto, el estado es 'idle'
        initial_position = self.rect.topleft  # Guardamos la posición inicial para comparar después

        # Movimiento horizontal
        if keys_pressed[pygame.K_LEFT]:
            self.rect.x -= self.movement_speed
            self.facing_right = False
        elif keys_pressed[pygame.K_RIGHT]:
            self.rect.x += self.movement_speed
            self.facing_right = True

        # Movimiento vertical
        if keys_pressed[pygame.K_UP]:
            self.rect.y -= self.movement_speed
        elif keys_pressed[pygame.K_DOWN]:
            self.rect.y += self.movement_speed

        # Detectar si ha habido algún cambio en la posición
        movement_detected = self.rect.topleft != initial_position

        # Actualizar el estado en base a si se detectó movimiento
        self.status = 'walk' if movement_detected else 'idle'

        # Actualiza las animaciones y el estado
        self.animations = import_folder(f'assets/images/players/shield hero/{self.status}/')
        self.animate()


class Sword_hero(Entity):
    def __init__(self,name,level, x, y, sword):
        super().__init__(name,level, x, y)
        self.image_path = "assets/images/players/sword hero/idle/1.png"
        # Stats
        self.health = int(25*np.log(self.level)+80)            # Salud baja
        self.attack = int(40*np.log(self.level)+12)            # Ataque alto
        self.defense = int(20*np.log(self.level)+5)            # Defensa baja
        self.magic = int(30*np.log(self.level)+10)             # Magia moderada
        self.magic_resistance = int(20*np.log(self.level)+5)   # Resistencia mágica baja
        self.evasion = int(35*np.log(self.level)+10)           # Evasión alta
        self.speed = int(40*np.log(self.level)+12)             # Velocidad alta
        self.crit_chance = 25                                  # Alta posibilidad de crítico
        # Sword
        self.sword = sword
        # Animación
        self.animations = import_folder('assets/images/players/sword hero/idle/')

    def update(self, keys_pressed):
        """Actualiza la posición en base a las teclas presionadas (movimiento básico)."""
        
        # Por defecto, el estado es 'idle'
        initial_position = self.rect.topleft  # Guardamos la posición inicial para comparar después

        # Movimiento horizontal
        if keys_pressed[pygame.K_a]:
            self.rect.x -= self.movement_speed
            self.facing_right = False
        elif keys_pressed[pygame.K_d]:
            self.rect.x += self.movement_speed
            self.facing_right = True

        # Movimiento vertical
        if keys_pressed[pygame.K_w]:
            self.rect.y -= self.movement_speed
        elif keys_pressed[pygame.K_s]:
            self.rect.y += self.movement_speed

        # Detectar si ha habido algún cambio en la posición
        movement_detected = self.rect.topleft != initial_position

        # Actualizar el estado en base a si se detectó movimiento
        self.status = 'walk' if movement_detected else 'idle'

        # Actualiza las animaciones y el estado
        self.animations = import_folder(f'assets/images/players/sword hero/{self.status}/')
        self.animate()
