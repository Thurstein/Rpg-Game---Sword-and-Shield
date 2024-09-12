import numpy as np
from hero import *

class Slime(Entity):
    def __init__(self,name,level,slime_type):
        super().__init__(name,level)
        self.slime_type = slime_type
        # Stats
        self.health = int(10*np.log(self.level)+50)
        self.attack = int(20*np.log(self.level)+7)
        self.defense = int(10*np.log(self.level)+2)
        self.magic = int(10*np.log(self.level)+2)
        self.magic_resistance = int(10*np.log(self.level)+2)
        self.evasion = int(10*np.log(self.level)+2)
        self.speed = int(10*np.log(self.level)+2)       
        self.crit_chance = 5

def combat(entity_1, entity_2):
    turn = 0
    while entity_1.is_alive() and entity_2.is_alive():
        print("\nTurn", turn)
        print(f"\n >>> Acción de {entity_1.name}:")
        entity_1.attacking(entity_2)
        print(f"\n >>> Acción de {entity_2.name}:")
        entity_2.attacking(entity_1)
        turn = turn + 1
    if entity_1.is_alive():
        print(f"\n {entity_1.name} has won")
    elif entity_2.is_alive():
        print(f"\n {entity_2.name} has won")
    else:
        print("\nTie")


# # swordsman_1 = Swordsman("Raftalia",100,"Iron dagger")
# # swordsman_1.show_hero()
# # print("---------------------------------------------")

# shield_hero_1 = Shield_hero("Naofumi",10,"Standard Shield")
# shield_hero_1.show_hero()

# green_slime_1 = Slime("Green Slime",10,"Green")
# green_slime_1.show_hero()

# combat(shield_hero_1, green_slime_1)