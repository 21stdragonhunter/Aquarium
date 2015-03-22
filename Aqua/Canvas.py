'''
Created on Dec 2, 2014

@author: Coleman
'''

class Canvas:
    
    def __init__(self, aquarium, canvas):
        
        for cell in aquarium.cells:
            color = cell.getColor()
            canvas.create_oval(cell.pos.x + cell.rad, cell.pos.y + cell.rad, cell.pos.x - cell.rad, cell.pos.y - cell.rad, fill = color, outline = color)
            canvas.pack()