""" File added to git repository"""


""" A turn based adventure game where the character will make choices that affect their final battle with the big boss
"""
class Car: #### WHY DO WE HAVE A CAR IN HERE???
    """A car in a dealership
    
    Attributes:
        model (str): the model of the car
        make (str): the make of the car
        year (str): the year the car was made"""
    
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