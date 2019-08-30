# Create 5 building instances
# Have each one get purchased by a real estate magnate
# After purchased, construct each one
# Once all building are purchased and constructed, print the address,
# owner, stories, and date constructed to the terminal for each one.

import datetime
# class creates objects
class Building:
    '''build a building'''
    def __init__(self, address, stories):
        '''initialize the building properties'''
        self.designer = "Misty"
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories
# these are methods and objects of class
    def constructor(self):
        self.date_constructed = datetime.datetime.now().strftime("%x")

    def purchase(self, owner):
        self.owner = owner


# creating instances of building
# print(datetime.datetime.now().strftime("%x"))
Smithsonian = Building("Washington DC", 4)
Smithsonian.constructor()
Smithsonian.purchase("Fred")
Parthenon = Building("Tennessee", 3)
Parthenon.purchase("John")
Parthenon.constructor()
Belle_Meade = Building("Tennessee", 2)
Belle_Meade.purchase("Geraldine")
Belle_Meade.constructor()
Taj_Mahal = Building("India", 4)
Taj_Mahal.purchase("Ghandi")
Taj_Mahal.constructor()
Colosseum = Building("Rome", 2)
Colosseum.purchase("Hannah")
Colosseum.constructor()
new_building = Building("Alabama State Capital", 2)
new_building.constructor()
print(f'{new_building.address} was purchased by {new_building.designer} on {new_building.date_constructed} and has {new_building.stories} stories.')
# print(new_building.constructor)


