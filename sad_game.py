import sys
import argparse
from random import randint, choice
import random

""" File added to git repository"""


""" 
A turn based adventure game where the character will make choices that affect their final battle with the big boss.

a quick note on the side: special weapons to be found in the story were added but the team did not have time to fully 
impliment them in a working fashion. Parts of the code for these still exist but do not currently impact the story or battles.
"""
class Attack:
    """ Donovan Fitzpatrick                  
                    
    Represents an attack with a name and power.

    Attributes:
    name (str): The name of the attack.
    power (int): The power or damage inflicted by the attack.
    """
    def __init__(self, name, power):
        """
    Initialize an Attack object with a name and power.

    Args:
    name (str): The name of the attack.
    power (int): The power or damage inflicted by the attack.
    """
        self.name = name
        self.power = power

class Character:
    """ Donovan Fitzpatrick: init, show_attacks,choose attacks
        Vivian Grev: Added def storyline() 
                    Added def alive(self) 
        
    Represents a character in the game with a name, health, and available attacks.

    Attributes:
    name (str): The name of the character.
    health (int): The health points of the character.
    attacks (list): A list of Attack objects representing the available attacks for the character.
    """
    def __init__(self, name, health=100):
        """Initialize an Attack object with a name and power.

    Args:
    name (str): The name of the attack.
    health (int): The power or damage inflicted by the attack.
    attacks (list): A list of Attack objects representing the available attacks for the character.
    """
        self.name = name
        self.health = health
        self.attacks = [Attack("Bite", power=10)]

    def storyline():
        """ 
        Display the storyline of the character from a .txt file.
        """
        with open("SadRats.txt", "r") as f:
            storyline = f.read().strip()
            print("\n", storyline)

    def show_attacks(self):
        """
        Display the available attacks.
        """
        print(f"{self.name}'s available attacks:")
        for i, attack in enumerate(self.attacks, start=1):
            print(f"{i}. {attack.name} (Power: {attack.power})")
            
    def choose_attacks(self):
        """
        Prompt the player to choose an attack and return the chosen attack index.
        """
        while True:
            try:
                choice = int(input("Choose an attack: "))
                if 1 <= len(self.attacks):
                    return choice
                else:
                    raise ValueError("Choose a valid attack.")
            except ValueError:
                print("Enter a number for the attack.")
                
    def alive(self):
        """
        Check if the character is alive based on their health.
        """
        return self.health > 0
        
class MiniBoss(Character):
    """ Mikel Reyes
    Represents a mini-boss character.

    Attributes:
    Inherits from Character and adds MiniBoss-specific attributes.
    """
    def __init__(self, name, health=50):
        super().__init__(name, health)
        self.attacks = [Attack("Mini Attack", power=randint(5, 15))]



class MagicRat(Character):
    """ Mikel Reyes: __init__, cast_spell(), use_flamethrower
        Vivian Grev: with open statement, print story

    Attributes:
    Inherits from Character and adds MagicRat-specific attributes.
    """
    
    def __init__(self, name, staff_material="Wood", has_flamethrower=False, health=100):
        """
        Initialize a MagicRat object with a name, staff material, flamethrower status, and optional health.

        Args:
        name (str): The name of the MagicRat.
        staff_material (str): The material of the staff (default is "Wood").
        has_flamethrower (bool): Whether the MagicRat has a flamethrower (default is False).
        health (int): The health points of the MagicRat (default is 100).
        """
        super().__init__(name)
        self.weapon = f"Staff ({staff_material})"
        self.has_flamethrower = has_flamethrower
        self.attacks.append(Attack("Magic Icicle", power=randint(8, 20)))
        self.attacks.append(Attack("Pebble Blast", power=randint(15, 18)))
        self.health = health
        with open("MagicRat.txt", "r") as f:
            mr_story = f.read().strip()
        print("\n", mr_story)
    

    def cast_spell(self):
        """
        Cast a spell using the MagicRat's magic.
        """
        spell = self.attacks[-1]
        damage_dealt = int(spell.power)
        print(f"{self.name} casts {spell.name}!")

    def use_flamethrower(self):
        """
        Use a flamethrower attack if available.
        """
        if self.has_flamethrower:
            print(f"{self.name} shoots flames using a flamethrower!")
            self.attacks.append(Attack("Flamethrower", power=randint(60, 100)))
        else:
            print(f"{self.name} does not have a flamethrower!")
            
    


class RatFu(Character):
    """ Mikel Reyes: __init__, punch(), use_galvaknuckles
        Vivian Grev: with open statement, print story
        
    Represents a martial arts-based character with unique attacks.

    Attributes:
    Inherits from Character and adds RatFu-specific attributes.
    """
    def __init__(self, name, has_galvaknuckles=False, health=100):
        """ 
        Initialize a RatFu object with a name, Galvaknuckles status, and optional health.

        Args:
        name (str): The name of the RatFu.
        has_galvaknuckles (bool): Whether the RatFu has Galvaknuckles (default is False).
        health (int): The health points of the RatFu (default is 100).
        """
        super().__init__(name)
        self.weapon = "Fists"
        self.has_galvaknuckles = has_galvaknuckles
        self.attacks.append(Attack("Upper Cut", power=randint(15, 18)))
        self.attacks.append(Attack("Consecutive Serious Punches", power=randint(8, 18)))
        self.health = health
        with open("RatFu.txt", 'r') as f:
            rf_story = f.read().strip()
        print("\n", rf_story)



    def punch(self):
        """
        Perform a punch attack with or without Galvaknuckles.
        """
        if self.has_galvaknuckles:
            print(f"{self.name} delivers an electrically charged punch with Galvaknuckles!")
            self.attacks.append(Attack("Galvaknuckle Punch", power=randint(60, 100)))
        else:
            print(f"{self.name} throws a powerful punch!")

    def use_galvaknuckles(self):
        """
        Activate Galvaknuckles if available.
        """
        if self.has_galvaknuckles:
            print(f"{self.name} activates Galvaknuckles!")
        else:
            print(f"{self.name} does not have Galvaknuckles!")

class SharpRat(Character):
    """ Mikel Reyes: __init__, swing_sword(), use_excalibur
        Vivian Grev: with open statement, print story
    Represents a sword-wielding character with unique attacks.

    Attributes:
    Inherits from Character and adds SharpRat-specific attributes.
    """
    def __init__(self, name, sword_material="Steel", has_excalibur=False, health=100):
        """
        Initialize a SharpRat object with a name, sword material, Excalibur status, and optional health.

        Args:
        name (str): The name of the SharpRat.
        sword_material (str): The material of the sword (default is "Steel").
        has_excalibur (bool): Whether the SharpRat has Excalibur (default is False).
        health (int): The health points of the SharpRat (default is 100).
        """
        super().__init__(name)
        self.weapon = f"Sword ({sword_material})"
        self.has_excalibur = has_excalibur
        self.attacks.append(Attack("Quick Slash", power=randint(10, 18)))
        self.attacks.append(Attack("Stab", power=randint(7, 15)))
        self.health = health
        with open("SharpRat.txt", 'r') as f:
            sr_story = f.read().strip()
        print("\n", sr_story)
        
        
    def swing_sword(self):
        """
        Swing the sword with or without Excalibur.
        """
        if self.has_excalibur:
            print(f"{self.name} swings Excalibur with incredible power!")
        else:
            print(f"{self.name} swings the sword with precision.")

    def use_excalibur(self):
        """
        Wield Excalibur if available.
        """
        if self.has_excalibur:
            print(f"{self.name} wields the mighty Excalibur!")
            self.attacks.append(Attack("Holy Strike", power=randint(60, 100)))
        else:
            print(f"{self.name} does not have Excalibur!")


class ShootyRat(Character):
    """ Mikel Reyes: __init__, shoot_arrow(), use_ratolas
        Vivian Grev: with open statement, print story
    Represents an archery-based character with unique attacks.

    Attributes:
    Inherits from Character and adds ShootyRat-specific attributes.
    """
    def __init__(self, name, bow_type="Glock-o", has_ratolas=False, health=100):
        """
        Initialize a ShootyRat object with a name, bow type, Ratolas status, and optional health.

        Args:
        name (str): The name of the ShootyRat.
        bow_type (str): The type of bow (default is "Glock-o").
        has_ratolas (bool): Whether the ShootyRat has Ratolas (default is False).
        health (int): The health points of the ShootyRat (default is 100).
        """
        super().__init__(name)
        self.weapon = f"Gun ({bow_type})"
        self.has_ratolas = has_ratolas
        self.attacks.append(Attack("Rat at at at", power=randint(12, 19)))
        self.attacks.append(Attack("Snipe", power=randint(18,20)))
        self.health = health
        with open("ShootyRat.txt", 'r') as f:
            sr_story = f.read().strip()
        print("\n", sr_story)

    def shoot_arrow(self):
        """
        Shoot an arrow with or without Ratolas.
        """
        if self.has_ratolas:
            print(f"{self.name} shoots an arrow with the sacred bow Ratolas!")
        else:
            print(f"{self.name} shoots an arrow with accuracy.")

    def use_ratolas(self):
        """
        Draw the Ratolas bow if available.
        """
        if self.has_ratolas:
            print(f"{self.name} draws the sacred bow Ratolas!")
            self.attacks.append(Attack("Elven Shot", power=randint(60, 100)))
        else:
            print(f"{self.name} does not have the sacred bow Ratolas!")
            
class NakedRat(Character):
    """ Mikel Reyes: __init__, dance(), use_invisibility_cloak
        Vivian Grev: with open statement, print story
        
    Represents a character without a weapon, using unique attacks.

    Attributes:
    Inherits from Character and adds NakedRat-specific attributes.
    """
    def __init__(self, name, has_invisibility_cloak=True, health=100):
        """
        Initialize a NakedRat object with a name, invisibility cloak status, and optional health.

        Args:
        name (str): The name of the NakedRat.
        has_invisibility_cloak (bool): Whether the NakedRat has an invisibility cloak (default is True).
        health (int): The health points of the NakedRat (default is 100).
        """
        super().__init__(name)
        self.weapon = f"Nakedness"
        self.has_invisibility_cloak = has_invisibility_cloak
        self.health = health
        with open("NakedRat.txt", 'r') as f:
            nr_story = f.read().strip()
        print("\n", nr_story)


    def dance(self):
        """
        Perform a lively dance.
        """
        print(f"{self.name} performs a lively dance!")

    def use_invisibility_cloak(self):
        """
        Use the invisibility cloak to perform an assassination.
        """
        if self.has_invisibility_cloak is True:
            print(f"{self.name} puts on the invisibility cloak and disappears!")
            self.attacks.append(Attack("Assasinate", power=randint(100, 105)))
        else:
            print(f"{self.name} does not have an invisibility cloak!")
            
class MasterSplinter(MiniBoss):
    """ Mikel Reyes
    Represents a mini-boss character named Master Splinter.

    Attributes:
    Inherits from MiniBoss and adds MasterSplinter-specific attacks.
    """
    def __init__(self, health=25):
        """
        Initialize a MasterSplinter object with optional health.

        Args:
        health (int): The health points of Master Splinter (default is 50).
        """
        super().__init__("Master Splinter", health)
        self.attacks.append(Attack("Ninja Swipe", power=randint(8, 15)))
        self.attacks.append(Attack("Zen Meditation", power=randint(5, 10)))

class MasterShifu(MiniBoss):
    """ Mikel Reyes
    Represents a mini-boss character named Master Shifu.

    Attributes:
    Inherits from MiniBoss and adds MasterShifu-specific attacks.
    """
    def __init__(self, health=25):
        """
        Initialize a MasterShifu object with optional health.

        Args:
        health (int): The health points of Master Shifu (default is 50).
        """
        super().__init__("Master Shifu", health)
        self.attacks.append(Attack("Kung Fu Kick", power=randint(10, 18)))
        self.attacks.append(Attack("Inner Peace Palm", power=randint(5, 12)))

class RatKing(Character):
    """ Donovan Fitzpatrick
    Represents the final boss character named Rat King.

    Attributes:
    Inherits from Character and adds RatKing-specific attacks.
    """
    def __init__(self, name="Rat King", health=100):
        """
        Initialize a RatKing object with optional name and health.

        Args:
        name (str): The name of the Rat King (default is "Rat King").
        health (int): The health points of the Rat King (default is 100).
        """
        super().__init__(name, health)
        self.attacks.append(Attack("Great Scythe", power=20))
        self.attacks.append(Attack("Intimidate", power=0))
        self.attacks.append(Attack("Throw Cheese", power=5))
        self.health = health
         
    
class Turn:
    """ Donovan Fitzpatrick
    Making the turn-based combat system
    Attributes:
    __init__(attacker, target): Initializes a Turn object.
    attack(attack_choice): Damages the other character.

    Side effects: reduces the health points of the target
    """
    def __init__(self, attacker, target):
        """
        Initialize a Turn object with an attacker and a target.

        Args:
        attacker (Character): The character initiating the turn.
        target (Character): The character receiving the attack.
        """
        self.attacker = attacker
        self.target = target

    def attack(self, attack_choice):
        """
        Execute an attack during a turn, reducing the target's health.

        Args:
        attack_choice (int): The index of the chosen attack from the attacker's available attacks.

        Side effects: Reduces the target's health based on the chosen attack,
                    and prints a message describing the attack.
        """
        chosen_attack = self.attacker.attacks[attack_choice - 1]
        damage_dealt = int(chosen_attack.power)
        self.target.health -= damage_dealt

        print(f"{self.attacker.name} uses {chosen_attack.name}! {self.target.name} took {damage_dealt} damage! \n \n")
        
          
class Battle:
    """ Donovan Fitzpatrick -- Code referenced (https://codereview.stackexchange.com/questions/100852/pok%C3%A9mon-style-battle-game)
                                reference code used to get an idea of how to class the different characters and elements of the turn based combat. 
                                Additionally used to reference instantiating these elements in the battle.
                                
    Represents a battle between a hero and an enemy with a storyline.

    Attributes:
    hero (Character): The player-controlled character.
    enemy (Character): The opponent character.
    story (str): The storyline for the battle.
    original_enemy (Character): The original enemy character for restart.
    """
    def __init__(self, hero, enemy, story):
        """
        Initialize a Battle object with a hero, an enemy, and a storyline.

        Args:
        hero (Character): The player-controlled character.
        enemy (Character): The opponent character.
        story (str): The storyline for the battle.
        original_enemy (Character): The original enemy character for restart.
        """
        self.hero = hero
        self.enemy = enemy
        self.story = story
        self.original_enemy = enemy  

    def start_battle(self):
        """Mikel Reyes - added mini boss elements
        Initiates the battle and handles the turn-based combat."""
        print(self.story)

        
        for i in range(1):  
            self.enemy = self.choose_random_mini_boss()
            print(f"{self.hero.name} approaches {self.enemy.name} and readies their {self.hero.weapon}")
            while self.hero.alive() and self.enemy.alive():
                self.turn()
            if not self.hero.alive():
                print("You have died. Game Over.")
                return
            
        self.enemy = self.original_enemy
        print(f"{self.hero.name} approaches the {self.enemy.name} and readies their {self.hero.weapon}")
        while self.hero.alive() and self.enemy.alive():
            self.turn()

        if self.hero.alive():
            print(f"The {self.enemy.name} has been defeated. You have won!")
        else:
            print("You have died. Game Over.")


    def turn(self):
        """
        Execute a turn in the battle.

        Side effects: Calls methods to display battle status, prompt player choice,
                    and determine the enemy's choice.
        """
        self.battle_status()
        self.player_choice()
        self.enemy_choice()

    def battle_status(self):
        """ 
        Display the current health status of the hero and the enemy.
        """
        print(f"{self.hero.name} (Health: {self.hero.health}) // {self.enemy.name} (Health: {self.enemy.health})")

    def player_choice(self):
        """
        Prompt the player to choose an attack and execute the chosen attack.

        Side effects: Calls methods to display available attacks, prompt player input,
                    and execute the chosen attack.
        """
        print(f"{self.hero.name}'s turn:")
        self.hero.show_attacks()
        while True:
            try:
                choice = self.hero.choose_attacks()
                turn = Turn(self.hero, self.enemy)
                turn.attack(choice)
                break
            except ValueError:
                print("Enter a number for the attack.")

    def enemy_choice(self):
        """
        Determine the enemy's choice of attack randomly and execute the chosen attack.

        Side effects: Calls methods to determine a random attack choice for the enemy
                    and execute the chosen attack.
        """
        choice = randint(1, len(self.enemy.attacks))
        turn = Turn(self.enemy, self.hero)
        turn.attack(choice)

    def restart_battle(self):
        """ Mikel Reyes
        Restart the battle if the player chooses to do so.

        Side effects: Prompts the player for a restart choice, resets the enemy
                    to the original enemy, restores hero's health, and restarts the battle.
        """
        restart_choice = input("Do you want to restart the battle? (yes/no): ").lower()
        if restart_choice == 'yes':
            self.enemy = self.original_enemy
            self.hero.health = 100
            self.start_battle()
        else:
            print("Thanks for playing!")

    def choose_random_mini_boss(self):
        """ Mikel Reyes
        Choose a random mini-boss from predefined mini-boss classes.

        Returns:
        Character: A randomly selected mini-boss character.
        """
        mini_boss_classes = [MasterSplinter(), MasterShifu()]
        return random.choice(mini_boss_classes)
                
    def rat_king_choice(self):
        """ 
        Determine the Rat King's choice of attack randomly and execute the chosen attack.

        Side effects: Calls methods to determine a random attack choice for the Rat King
                    and execute the chosen attack.
        """
        choice = randint(1, len(self.enemy.attacks))
        turn = Turn(self.enemy, self.hero)
        turn.attack(choice)
        


def parse_args(args):
    """ Vivian Grev
    
    Parse command-line arguments for the game.

    Args:
    args (list): List of command-line arguments.

    Returns:
    (Namespace) Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Turn-based adventure game with character choices.")
    parser.add_argument("--name", type=str, help="Name of the mousekateer.")
    parser.add_argument("--character_class", type=str, choices=["MagicRat", "RatFu", "SharpRat", "ShootyRat", "NakedRat"],
                        help="Choose a character class.")
    parser.add_argument("--health", type=int, help="Level of health for the mousekateer.")
    parser.add_argument("--damage", type=int, help="The amount of damage a character takes.")
    parser.add_argument("--weapon", type=str, help="Choose the weapon for the mousekateer.")
    parser.add_argument("--storyline_file", type=str, help="Path to the storyline file.")
    parser.add_argument("--mini_boss", action="store_true", help="Fight Mini Bosses.")

    return parser.parse_args(args)

def choose_character_class():
    """ 
    Prompt the player to choose a character class.

    Returns:
    (str) Chosen character class.
    """
    print("Choose your character class:")
    print("1. ShootyRat")
    print("2. NakedRat")
    print("3. MagicRat")
    print("4. SharpRat")
    print("5. RatFu")

    while True:
        try:
            choice_num = int(input("Enter the number of your chosen class: "))
            if 1 <= choice_num <= 5:
                return ["ShootyRat", "NakedRat", "MagicRat", "SharpRat", "RatFu"][choice_num - 1]
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    """ Vivian Grev, Donovan Fitzpatrick, Mikel Reyes """
    Character.storyline()
    args = parse_args(sys.argv[1:])

    if args.character_class is None:
        args.character_class = choose_character_class()

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
        sys.exit(1)

    if args.mini_boss:
        for i in range(0):
            mini_boss = choice([MasterSplinter(), MasterShifu()])
            battle_instance = Battle(player, mini_boss, args.storyline_file)
            battle_instance.start_battle()
            if not player.alive():
                break  

        if player.alive():
            rat_king = RatKing()
            battle_instance = Battle(player, rat_king, args.storyline_file)
            battle_instance.start_battle()

    else:
        print("Battle")
        
    enemy = RatKing()
    battle_instance = Battle(player, enemy, args.storyline_file)
    battle_instance.start_battle()