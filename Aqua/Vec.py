'''
Created on Dec 2, 2014

@author: Coleman
'''

class Vec:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def set(self, x, y):
        self.x = x
        self.y = y
        return self
    def get(self):
        newVec = Vec(self.x, self.y)
        return newVec
    def add(self, o):
        self.x += o.x
        self.y += o.y
        return self
    def sub(self, o):
        self.x -= o.x
        self.y -= o.y 
        return self
    def mul(self, n):
        self.x *= n
        self.y *= n
        return self
    def div(self, n):
        if self.x / n < 0.01:
            self.x = 0
        else:
            self.x = self.x / n
        if self.y / n < 0.01:
            self.y = 0
        else:
            self.y = self.y / n
        return self
    def neg(self):
        self.x = -self.x
        self.y = -self.y
    def mag(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    def normalize(self):
        mag = self.mag()
        if mag == 0:
            mag = 0.01
        self.x /= mag
        self.y /= mag
        return self