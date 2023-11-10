import sys
import argparse
import random
import math

""" File added to git repository"""


""" A turn based adventure game where the character will make choices that affect their final battle with the big boss
"""
class Character:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def attack(self):
        pass

    def defend(self):
        pass


class MagicRat(Character):
    def __init__(self, name, staff_material="Wood", has_flamethrower=False):
        super().__init__(name)
        self.weapon = f"Staff ({staff_material})"
        self.has_flamethrower = has_flamethrower

    def cast_spell(self):
        print(f"{self.name} casts a spell!")

    def use_flamethrower(self):
        if self.has_flamethrower:
            print(f"{self.name} shoots flames using a flamethrower!")
        else:
            print(f"{self.name} does not have a flamethrower!")


class RatFu(Character):
    def __init__(self, name, has_galvaknuckles=False):
        super().__init__(name)
        self.weapon = "Fists"
        self.has_galvaknuckles = has_galvaknuckles

    def punch(self):
        if self.has_galvaknuckles:
            print(f"{self.name} delivers an electrically charged punch with Galvaknuckles!")
        else:
            print(f"{self.name} throws a powerful punch!")

    def use_galvaknuckles(self):
        if self.has_galvaknuckles:
            print(f"{self.name} activates Galvaknuckles!")
        else:
            print(f"{self.name} does not have Galvaknuckles!")


class SharpRat(Character):
    def __init__(self, name, sword_material="Steel", has_excalibur=False):
        super().__init__(name)
        self.weapon = f"Sword ({sword_material})"
        self.has_excalibur = has_excalibur

    def swing_sword(self):
        if self.has_excalibur:
            print(f"{self.name} swings Excalibur with incredible power!")
        else:
            print(f"{self.name} swings the sword with precision.")

    def use_excalibur(self):
        if self.has_excalibur:
            print(f"{self.name} wields the mighty Excalibur!")
        else:
            print(f"{self.name} does not have Excalibur!")


class ShootyRat(Character):
    def __init__(self, name, bow_type="Longbow", has_ratolas=False):
        super().__init__(name)
        self.weapon = f"Bow ({bow_type})"
        self.has_ratolas = has_ratolas

    def shoot_arrow(self):
        if self.has_ratolas:
            print(f"{self.name} shoots an arrow with the sacred bow Ratolas!")
        else:
            print(f"{self.name} shoots an arrow with accuracy.")

    def use_ratolas(self):
        if self.has_ratolas:
            print(f"{self.name} draws the sacred bow Ratolas!")
        else:
            print(f"{self.name} does not have the sacred bow Ratolas!")
            
class NakedRat(Character):
    def __init__(self, name, has_invisibility_cloak=False):
        super().__init__(name)
        self.weapon = None
        self.has_invisibility_cloak = has_invisibility_cloak

    def dance(self):
        print(f"{self.name} performs a lively dance!")

    def use_invisibility_cloak(self):
        if self.has_invisibility_cloak:
            print(f"{self.name} puts on the invisibility cloak and disappears!")
        else:
            print(f"{self.name} does not have an invisibility cloak!")

        
    
        
            
    
class Character:
    """Its a character, all right. 
    Attributes:
    alive(int): evaluates if hp is above 0
    take_damage(int): reduces hp based on damage taken
    
    Side effects:
    """
    def __init__(self, name, hp, damage, weapon, skill, speed, moves):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.weapon = weapon
        self.skill = skill
        self.speed = speed
        self.moves = moves
        
    def alive(self):
        return self.hp > 0
    
    def take_damage(self, damage):
        self.hp -= damage
        
class Turn:
    """Making the turn-based combat system
    Attributes:
    __init__():
    attack(int): to damage the other character
    
    Side effects: reduce hp of of the target
    """
    def __init__(Character):
        pass
        
    def attack(self, attacker, target, weapon):
        damage_delt = attacker.damage + weapon.damage
        target.take_damage(damage_delt)
        
          
def battle():
    """FIGHT!
    Args(): IDK YET 
    
    Returns:
    Who will win the big battle? Will you beat this game? Probably.
    """
    hero = Character(self.name, self.hp, self.damage, self.weapon, self.skill, self.speed, self.moves)
    Tzeech = Character("Tzeech", 100, 12, "Great Sythe", 
                       "Intimidate", 3, 2)
    while hero.alive and Tzeech.alive:
        pass
        
    if hero.alive:
        pass
    else:
        print("You have died.")



def parse_args(args):
    """Parse command-line arguments.

    Args:
        args (list): Command-line arguments

    Returns:
        args: The parsed command-line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("", help="")
    parser.add_argument("", help="")
    parser.add_argument("", help="")
    return parser.parse_args(args)