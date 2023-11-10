""" File added to git repository"""


""" A turn based adventure game where the character will make choices that affect their final battle with the big boss
"""
class Car:
    """A car in a dealership
    
    Attributes:
        model (str): the model of the car
        make (str): the make of the car
        year (str): the year the car was made"""
    
    def __init__(self, model, make, year):
        self.model = model
        self.make = make
        self.year = year
        
        
class Character():
    def __init__(self, name, skill, weapon, health):
        self.name = name
        self.skill = skill
        self.weapon = weapon
        self.health = health 
        #stage
        