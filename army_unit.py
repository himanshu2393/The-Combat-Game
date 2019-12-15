'''
 DEVELOPED BY: Himanshu Sharma
 DESCRIPTION: This file holds the Army Unit as an entity which has type(like archer knight etc.),
              buying price, owner of the unit and versus(a dictionary object which states its
              strength comparison against other unit types [if -1: unit loses, if 0: then tie,
              if 1: unit wins])
'''

class ArmyUnit:
    type = ''            # archer, knight, soldier, seige_equipment, wizard or blank for initializing
    price = 1            # buying price of the unit
    versus = {}
    unit_owner = ''
    health = 0

    # this method creates the class object.
    def __init__(self, type, unit_owner):  # this method creates the class object.
        self.type = type
        self.unit_owner = unit_owner

        if type == 'Archer':
            self.archer_unit()
        elif type == 'Knight':
            self.knight_unit()
        elif type == 'Soldier':
            self.soldier_unit()

    # this method instantiates the object with archer's properties.
    def archer_unit(self):
        self.versus = {'Knight': -1, 'Archer': 0, 'Soldier': 1}
        self.health = 1
        self.price = 1

    # this method instantiates the object with knight's properties.
    def knight_unit(self):
        self.versus = {'Knight': 0, 'Archer': 1, 'Soldier': -1}
        self.health = 3
        self.price = 3

    # this method instantiates the object with soldier's properties.
    def soldier_unit(self):
        self.versus = {'Knight': 1, 'Archer': -1, 'Soldier': 0}
        self.health = 2
        self.price = 2
