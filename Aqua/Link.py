'''
Created on Dec 2, 2014

@author: Coleman
'''

class Link:
    def __init__(self, head, connection = None):
        self.head = head
        self.connection = connection
        self.thrust = 0
        
    def bind(self):
        dif = self.head.pos.get().sub(self.connection.pos)
        self.head.acc.sub(dif.mul(self.head.aq.LINK_ENERGY))
        dif = self.connection.pos.get().sub(self.head.pos)
        self.connection.acc.sub(dif.mul(self.connection.aq.LINK_ENERGY))