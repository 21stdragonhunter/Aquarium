'''
Created on Dec 2, 2014

@author: Coleman
'''

class Aquarium:
    
    def __init__(self, width, height, attract, maxcell, mindna, maxdna, death, radius):
        self.cells = []
        self.MAX_CELL_COUNT = maxcell
        self.MIN_DNA = mindna
        self.MAX_DNA = maxdna
        self.ATTRACT = attract
        self.WIDTH = width
        self.HEIGHT = height
        self.DEATH_AGE = death
        self.RADIUS = radius

        self.MAX_MITOCHONDRIA = 50
        self.MITOCHONDRIA_RATE = 0.5
        self.DENATURE_RATE = 0.5
        self.MIN_PROTEINS = 100
        self.SINGLE_CELLED = True
        self.LINK_ENERGY = 0.1
        
    def step(self):
        for cell in self.cells:
            cell.work()
            cell.interact(self.cells)
            cell.rebound()
            cell.applyPhysics()
            # if len(self.cells) == self.MAX_CELL_COUNT:
            #     self.cells = self.cells[0 : len(self.cells) // 5 + 1]
        
    def delete(self, cell):
        if cell in self.cells:
            self.cells.remove(cell)