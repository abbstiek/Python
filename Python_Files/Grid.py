"""Map Grid Module for Poothon_Game"""

import random
from locations import Location

class Grid(object):
    def __init__(self):
        self.grid = [[None] * 5] * 5 #Blank 2D Map Grid
        self.location = Location()  #Blank location object

    def initGrid(self):
        #Generate an empty grid of location objects
        for i in range(len(self.grid)):
            self.grid.append(self.location)
            self.grid[i].append(self.location)

    def blockTerrain(self, x_coordinate, y_coordinate):
        #Close off a location
        self.grid[x_coordinate][y_coordinate].blockPath()

    def enableTerrain(self, x_coordinate, y_coordinate):
        #Enable traversing a location
        self.grid[x_coordinate][y_coordinate].enablePath()
