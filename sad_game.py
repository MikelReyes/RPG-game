import sys
import argparse
from random import randint
import math

""" File added to git repository"""


""" A turn based adventure game where the character will make choices that affect their final battle with the big boss
"""
class Attack:
    def __init__(self, name, power):
        self.name = name
        self.power = power

class Character:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.attacks = [Attack("Bite", power=10)]


    def show_attacks(self):
        print(f"{self.name}'s available attacks:")
        for i, attack in enumerate(self.attacks, start=1):
            print(f"{i}. {attack.name} (Power: {attack.power})")
            
    def choose_attacks(self):
        while True:
            try:
                choice = int(input("Choose an attack: "))
                if 1 <= len(self.attacks):
                    return choice
                else:
                    print("Choose a valid attack.")
            except ValueError:
                print("Enter a number for the attack.")
        


class MagicRat(Character):
    def __init__(self, name, staff_material="Wood", has_flamethrower=False):
        super().__init__(name)
        self.weapon = f"Staff ({staff_material})"
        self.has_flamethrower = has_flamethrower
        self.attacks.append(Attack("Magic Icicle", power=randint(8, 20)))
        self.attacks.append(Attack("Pebble Blast", power=randint(15, 18)))

    def cast_spell(self):
        spell = self.attacks[-1]
        damage_dealt = int(spell.power)
        print(f"{self.name} casts {spell.name}!")

    def use_flamethrower(self):
        if self.has_flamethrower:
            print(f"{self.name} shoots flames using a flamethrower!")
            self.attacks.append(Attack("Flamethrower", power=randint(60, 100)))
        else:
            print(f"{self.name} does not have a flamethrower!")


class RatFu(Character):
    def __init__(self, name, has_galvaknuckles=False):
        super().__init__(name)
        self.weapon = "Fists"
        self.has_galvaknuckles = has_galvaknuckles
        self.attacks.append(Attack("Upper Cut", power=randint(15, 18)))
        self.attacks.append(Attack("Consecutive Serious Punches", power=randint(8, 18)))

    def punch(self):
        if self.has_galvaknuckles:
            print(f"{self.name} delivers an electrically charged punch with Galvaknuckles!")
            self.attacks.append(Attack("Galvaknuckle Punch", power=randint(60, 100)))
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
        self.attacks.append(Attack("Quick Slash", power=randint(10, 18)))
        self.attacks.append(Attack("Stab", power=randint(7, 15)))
        
    def swing_sword(self):
        if self.has_excalibur:
            print(f"{self.name} swings Excalibur with incredible power!")
        else:
            print(f"{self.name} swings the sword with precision.")

    def use_excalibur(self):
        if self.has_excalibur:
            print(f"{self.name} wields the mighty Excalibur!")
            self.attacks.append(Attack("Holy Strike", power=randint(60, 100)))
        else:
            print(f"{self.name} does not have Excalibur!")


class ShootyRat(Character):
    def __init__(self, name, bow_type="Longbow", has_ratolas=False):
        super().__init__(name)
        self.weapon = f"Bow ({bow_type})"
        self.has_ratolas = has_ratolas
        self.attacks.append(Attack("Bow Shot", power=randint(12, 19)))
        self.attacks.append(Attack("Precise Shot", power=randint(18,20)))

    def shoot_arrow(self):
        if self.has_ratolas:
            print(f"{self.name} shoots an arrow with the sacred bow Ratolas!")
        else:
            print(f"{self.name} shoots an arrow with accuracy.")

    def use_ratolas(self):
        if self.has_ratolas:
            print(f"{self.name} draws the sacred bow Ratolas!")
            self.attacks.append(Attack("Elven Shot", power=randint(60, 100)))
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
            self.attacks.append(Attack("Assasinate", power=randint(100, 105)))
        else:
            print(f"{self.name} does not have an invisibility cloak!")

class RatKing(Character):
    def __init__(self, name="Rat King", health=100):
        super().__init__(name, health)
        self.attacks.append(Attack("Great Scythe", power=20))
        self.attacks.append(Attack("Intimidate", power=0))
        self.attacks.append(Attack("Throw Cheese", power=5))
         
class Turn:
    """Making the turn-based combat system
    Attributes:
    __init__():
    attack(int): to damage the other character
    
    Side effects: reduce hp of of the target
    """
    def __init__(self, attacker, target):
        self.attacker = attacker
        self.target = target
        
    def attack(self, attack_choice):
        chosen_attack = self.attacker.attacks[attack_choice - 1]
        damage_dealt = int(chosen_attack.power)
        self.target.health -= damage_dealt
        
        print(f"{self.attacker.name} uses {chosen_attack.name}! {self.target.name} took {damage_dealt} damage!")
        
          
class Battle():
    """FIGHT!
    Args(): IDK YET 
    
    Returns:
    Who will win the big battle? Will you beat this game? Probably.
    """
    
    def __init__(self, hero, rat_king):
        self.hero = hero
        self.rat_king = rat_king
        
    def start_battle(self):    
        print(f"{self.hero.name} approaches the Rat King and readies their {self.hero.weapon}")
        while self.hero.alive() and self.rat_king.alive():
            self.turn()
        
        if self.hero.alive():
            print("The Rat King has been defeated. You have won!")
            

        else:
            print("You have died.")
            
    def turn(self):
        self.battle_status()
        self.player_choice()
        self.rat_king_choice()
        
    def battle_status(self):
        print(f"{self.hero.name} (Health: {self.hero.health}) // {self.rat_king.name} (Health: {self.rat_king.health})")
        
    def player_choice(self):
        print(f"{self.hero.name}'s turn:")
        self.hero.show_attacks()
        
        while True:
            try:
                choice =self.hero.choose_attack()
                turn = Turn(self.hero, self.rat_king)
                turn.attack(choice)
                break      
            except ValueError:
                print("Enter a number for the attack.")
                
    def rat_king_choice(self):
        choice = randint(1, len(self.rat_king.attacks))
        turn = Turn(self.rat_king, self.hero)
        turn.attack(choice)


def parse_args(args):
    """Parse command-line arguments.

    Args:
        args (list): Command-line arguments

    Returns:
        args: The parsed command-line arguments
    """
    parser = argparse.ArgumentParser(description="Turn-based adventure game with character choices.")
    parser.add_argument("--name", type=str, help="Name of the mousekateer.")
    parser.add_argument("--character_class", type=str, choices=["MagicRat", "RatFu", "SharpRat", "ShootyRat", "NakedRat"],
                        help="Choose a character class.")
    parser.add_argument("--hp", type=int, help="Level of health for the mousekateer.")
    parser.add_argument("--damage", type=int, help="The amount of damage a character takes.")
    parser.add_argument("--weapon", type=str, help="Choose the weapon for the mousekateer.")
    
    return parser.parse_args(args)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    character_class = args.character_class
    if character_class == "MagicRat":
        player = MagicRat(args.name)
    elif character_class == "RatFu":
        player = RatFu(args.name)
    elif character_class == "SharpRat":
        player = SharpRat(args.name)
    elif character_class == "ShootyRat":
        player = ShootyRat(args.name)
    elif character_class == "NakedRat":
        player = NakedRat(args.name)
    else:
        print("Invalid character class.")
        
    player.health = args.hp
    player.damage = args.damage
    player.weapon = args.weapon
    
    enemy = RatKing()
        
    battle_instance = Battle(player, enemy)
    battle_instance.start_battle()