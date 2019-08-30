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

    def __str__(self):
        return (f"{self.address} was purchased by {self.designer} on {self.date_constructed} and has {self.stories} stories.")