'''
Created on Dec 2, 2014

self.author: Coleman
'''
import random

from Aqua.Link import Link
from Aqua.Vec import Vec

class Cell:
    
    def __init__(self, aq, dna, pos):
        self.aq = aq
        self.dna = dna
        self.pos = pos
        self.age = 0
        self.agedna = 1
        self.rad = aq.RADIUS
        self.drag = 0.5
        self.vel = Vec() #curent velocity
        self.acc = Vec() #accumulated velocity rate, rebuilt every interact call
        self.bind = Vec()
        self.tailPos = Vec()
        
        self.child = None
        self.mitochondria = self.aq.MAX_MITOCHONDRIA // 2
        self.ribosomes = self.aq.MIN_PROTEINS * self.aq.MIN_PROTEINS * self.aq.DENATURE_RATE
        self.proteins = 0
        
        self.attract = self.aq.ATTRACT
        self.deathAge = float("Inf")
        
        c = random.randint(-25, 25)
        self.tint = (c, c, c)
        self.color = (150, 25, 25)
        
        self.links = []
        
    def getColor(self):
        color = "#%02x%02x%02x" % (self.tint[0] + self.color[0], self.tint[1] + self.color[1], self.tint[2] + self.color[2])
        return color
        
    def work(self):
        if self.age > self.deathAge:
            self.die()

        # while self.attract == 0:
        #     self.attract = random.randint(-1, 1)
         
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
             
        if self.agedna > self.dna and not self.aq.MAX_CELL_COUNT == len(self.aq.cells):
            self.divide()
         
    def interact(self, cells):
        for cell in cells:
            if cell is self:
                continue
            dif = self.pos.get().sub(cell.pos)
            combinedRad = self.rad + cell.rad
            f = dif.mag() - combinedRad
            if f > 0:
                f *= 5
                f = ((1 - f) / (f + 1)) * 0.2
                f *= self.attract
            else:
                f *= -1
                f *= (self.age * (1 / (2 * self.aq.MAX_DNA))) / ( (self.age * (1 / (2 * self.aq.MAX_DNA))) + 1 )
            f *= self.mitochondria / self.aq.MAX_MITOCHONDRIA + 1
            forceVector = dif.get().normalize().mul(f)
            self.acc.add(forceVector)
         
    def rebound(self):
        for link in self.links:
            if link.head == self and link.connection in self.aq.cells:
                link.bind()
            else:
                self.links.remove(link)
                
    def applyPhysics(self):
        self.age += 1
        self.agedna += 1
        self.vel.add(self.acc)
        self.vel.mul(1 - self.drag)
        self.pos.add(self.vel)
        self.acc.set(0, 0)
        
        if self.pos.x + self.rad >= self.aq.WIDTH:
            self.pos.x = self.aq.WIDTH - self.rad
        elif self.pos.x - self.rad <= 0:
            self.pos.x = self.rad
            
        if self.pos.y + self.rad >= self.aq.HEIGHT:
            self.pos.y = self.aq.WIDTH - self.rad
        elif self.pos.y - self.rad <= 0:
            self.pos.y = self.rad
        
    def applyPhysicsAir(self):
        self.age += 1
        self.agedna += 1
        self.vel.add(self.acc)
        self.vel.mul(1 - self.drag)
        self.pos.add(self.vel)
        self.acc.set(0, 0)
        
        if self.pos.x >= self.aq.WIDTH:
            self.pos.x = 0
        elif self.pos.x <= 0:
            self.pos.x = self.aq.WIDTH
            
        if self.pos.y >= self.aq.HEIGHT:
            self.pos.y = 0
        elif self.pos.y <= 0:
            self.pos.y = self.aq.HEIGHT
         
    def divide(self):
        self.mitochondria //= 2
        self.proteins //= 4
        self.ribosomes //= 2
        newCell = Cell(self.aq, self.dna + random.randint(-1, 1), self.pos.get().add(Vec(random.random() - 0.5, random.random() - 0.5)))
#         selfCell = Cell(self.aq, self.dna, self.pos.get())
        self.aq.cells.append(newCell)
#         self.aq.cells.append(selfCell)
        newCell.mitochondria = self.mitochondria
        newCell.ribosomes = self.ribosomes
        newCell.proteins = self.proteins
        newCell.color = self.color
        newCell.deathAge = self.aq.DEATH_AGE
#         selfCell.mitochondria = self.mitochondria
#         selfCell.ribosomes = self.ribosomes
#         selfCell.proteins = self.proteins
#         if not self.aq.SINGLE_CELLED:
#             link = Link(selfCell, newCell)
#             selfCell.links.append(link)
        if not self.aq.SINGLE_CELLED:
            link = Link(self, newCell)
            self.links.append(link)
#         self.die()
        self.agedna = 1
#         self.color = [25, 25, 150]
        return self
        
    def die(self):
        self.aq.delete(self)
        