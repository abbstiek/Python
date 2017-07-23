"""Locations class and subsequent relevant classes"""

import random

class Location(object):
    def __init__(self, name="", terrain="neutral"):
    self.name = name
    self.traversable = True

    def genTerrain(self):
        #Randomly generate a terrain
        self.terrain.append(random.choice(terrain_types))

    def enablePath(self):
        #Make location traversable
        self.traversable = True

    def blockPath(self):
        #Block movement along this location
        self.traversable = False
