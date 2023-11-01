""" File added to git repository"""

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