import pdb
import math










class Circle:
    _PI = math.pi

    def __init__(self, radius):
        self.radius = radius

    @property
    def get_radius(self):
        return self.radius