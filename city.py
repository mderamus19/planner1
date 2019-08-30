class City:
    '''building a replica of a city'''
    def __init__(self, name, mayor):
        '''initialize city attributes'''
        self.name = name
        self.mayor = mayor
        self.year_est = 0
        self.all_buildings = []

    def add_building(self, building):
        '''add building to the city'''
        self.all_buildings.append(building)

