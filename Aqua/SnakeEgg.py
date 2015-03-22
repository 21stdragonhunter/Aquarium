'''
Created on Dec 5, 2014

@author: Coleman
'''

import random
from Aqua.Cell import Cell
from Aqua.Vec import Vec
from Aqua.Link import Link

class Snake(Cell):
    def __init__(self, aq, dna, pos):
        aq.SINGLE_CELLED = False
        Cell.__init__(self, aq, dna, pos)
        
    def work(self):
        while self.attract == 0:
            self.attract = random.randint(-1, 1)
         
        self.proteins *= 1 - self.aq.DENATURE_RATE
        self.proteins += self.ribosomes
        self.ribosomes += self.aq.MIN_PROTEINS
        
        if self.proteins < self.aq.MIN_PROTEINS:
            self.die()
         
        for i in range(0, self.mitochondria):
            if random.random() > self.aq.MITOCHONDRIA_RATE:
                self.mitochondria += 1
            
            if self.mitochondria > self.aq.MAX_MITOCHONDRIA:
                self.mitochondria = self.aq.MAX_MITOCHONDRIA
             
        if self.agedna > self.dna and self.age == self.dna and not self.aq.MAX_CELL_COUNT == len(self.aq.cells):
            self.divide()
            
    def divide(self):
        self.mitochondria //= 2
        self.proteins //= 4
        self.ribosomes //= 2
        newCell = Snake(self.aq, self.dna + random.randint(-1, 1), self.pos.get().add(Vec(random.random() - 0.5, random.random() - 0.5)))
        self.aq.cells.append(newCell)
        newCell.mitochondria = self.mitochondria
        newCell.ribosomes = self.ribosomes
        newCell.proteins = self.proteins
        newCell.color = self.color
        link = Link(self, newCell)
        self.links.append(link)
        self.agedna = 1
        return self