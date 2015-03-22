'''
Created on Dec 2, 2014

@author: Coleman
'''

import tkinter
import random
import time
from Aqua.SnakeEgg import Snake
from Aqua.Aquarium import Aquarium
from Aqua.Cell import Cell
from Aqua.Canvas import Canvas
from Aqua.Vec import Vec

def main():
    WIDTH = 750
    HEIGHT = 750
    ATTRACT = 1
    MAX_CELLS = 50
    MIN_DNA = 50
    MAX_DNA = 100
    RADIUS = 5
    DEATH_AGE = float("Inf")
    
    root = tkinter.Tk()
    
    root.minsize(width = WIDTH + 25, height = HEIGHT)
    root.maxsize(width = WIDTH + 25, height = HEIGHT)
    
    canvas = tkinter.Canvas(width = WIDTH, height = HEIGHT)
    
    aq = Aquarium(WIDTH, HEIGHT, ATTRACT, MAX_CELLS, MIN_DNA, MAX_DNA, DEATH_AGE, RADIUS)

    # runPopulationAttract(aq, MIN_DNA, MAX_DNA, WIDTH, HEIGHT)

    # runPopulation(aq, MIN_DNA, MAX_DNA, WIDTH, HEIGHT)

    runCyclicEngine(aq, MIN_DNA, MAX_DNA, WIDTH, HEIGHT)

    # runReverseEngine(aq, MIN_DNA, MAX_DNA, WIDTH, HEIGHT)

    # runEngine(aq, MIN_DNA, MAX_DNA, WIDTH, HEIGHT)
    
    # runSingle(aq, MIN_DNA, MAX_DNA, WIDTH, HEIGHT)

    # RunMove(aq, MIN_DNA, MAX_DNA, WIDTH, HEIGHT)
    
    # RunDual(aq, MIN_DNA, MAX_DNA, WIDTH, HEIGHT)

    # RunSnake(aq, WIDTH, HEIGHT)
    
    while(True):
        aq.step()
        canvas.destroy()
        canvas = tkinter.Canvas(width = WIDTH, height = HEIGHT, bg = "#FFFFFF")
        Canvas(aq, canvas)
        time.sleep(.015)
        canvas.update()
        
def RunSnake(aq, WIDTH, HEIGHT):
    for i in range(1):
        egg = Snake(aq, 15, Vec(WIDTH // 2, HEIGHT // 2))
        aq.cells.append(egg)
    aq.LINK_ENERGY = 0.865
    aq.ATTRACT = 0
    
def RunMove(aq, MIN_DNA, MAX_DNA, WIDTH, HEIGHT):
    randDNA = random.randint(MIN_DNA, MAX_DNA)
    cell = Cell(aq, randDNA, Vec(WIDTH // 2 + 100, HEIGHT // 2 + 100))
    aq.cells.append(cell)
    aq.SINGLE_CELLED = False
    aq.LINK_ENERGY = 0.001
    aq.MAX_CELL_COUNT = 32
    
def RunDual(aq, MIN_DNA, MAX_DNA, WIDTH, HEIGHT):
    randDNA = random.randint(MIN_DNA, MAX_DNA)
    cell = Cell(aq, randDNA, Vec(WIDTH // 2 + 100, HEIGHT // 2 + 100))
    aq.cells.append(cell)
    cell = Cell(aq, randDNA, Vec(WIDTH // 2 - 100, HEIGHT // 2 - 100))
    aq.cells.append(cell)
    cell.color = [150, 150, 150]
    aq.SINGLE_CELLED = False
    aq.LINK_ENERGY = 0.05
    aq.MAX_CELL_COUNT = 32
    
def runSingle(aq, MIN_DNA, MAX_DNA, WIDTH, HEIGHT):
        for i in range(aq.MAX_CELL_COUNT // 3):
            cell = Cell(aq, random.randint(MIN_DNA, MAX_DNA), Vec(WIDTH // 2 + random.randint(-100, 100), HEIGHT // 2 + random.randint(-100, 100)))
            aq.cells.append(cell)

def runEngine(aq, MIN_DNA, MAX_DNA, WIDTH, HEIGHT):
        aq.DEATH_AGE = 75
        for i in range(aq.MAX_CELL_COUNT // 5):
            cell = Cell(aq, random.randint(MIN_DNA, MAX_DNA), Vec(WIDTH // 2 + random.randint(-100, 100), HEIGHT // 2 + random.randint(-100, 100)))
            aq.cells.append(cell)
            cell.attract = -1

def runReverseEngine(aq, MIN_DNA, MAX_DNA, WIDTH, HEIGHT):
        aq.DEATH_AGE = 75
        aq.ATTRACT = -1
        for i in range(aq.MAX_CELL_COUNT // 5):
            cell = Cell(aq, random.randint(MIN_DNA, MAX_DNA), Vec(WIDTH // 2 + random.randint(-100, 100), HEIGHT // 2 + random.randint(-100, 100)))
            aq.cells.append(cell)
            cell.attract = 1

def runCyclicEngine(aq, MIN_DNA, MAX_DNA, WIDTH, HEIGHT):
        aq.DEATH_AGE = 75
        MIN_DNA = 75
        MAX_DNA = 75
        for i in range(aq.MAX_CELL_COUNT // 5):
            cell = Cell(aq, random.randint(MIN_DNA, MAX_DNA), Vec(WIDTH // 2 + random.randint(-100, 100), HEIGHT // 2 + random.randint(-100, 100)))
            aq.cells.append(cell)
            cell.attract = -1

def runPopulation(aq, MIN_DNA, MAX_DNA, WIDTH, HEIGHT):
    aq.DEATH_AGE = 1.4 * MAX_DNA // 1
    aq.ATTRACT = 0
    cell = Cell(aq, MIN_DNA, Vec(WIDTH // 2 + random.randint(-100, 100), HEIGHT // 2 + random.randint(-100, 100)))
    aq.cells.append(cell)
    cell.color = [150, 25, 25]
    cell = Cell(aq, (MIN_DNA + MAX_DNA) // 2, Vec(WIDTH // 2 + random.randint(-100, 100), HEIGHT // 2 + random.randint(-100, 100)))
    aq.cells.append(cell)
    cell.color = [25, 150, 25]
    cell = Cell(aq, MAX_DNA, Vec(WIDTH // 2 + random.randint(-100, 100), HEIGHT // 2 + random.randint(-100, 100)))
    aq.cells.append(cell)
    cell.color = [25, 25, 150]

def runPopulationAttract(aq, MIN_DNA, MAX_DNA, WIDTH, HEIGHT):
    aq.DEATH_AGE = 1.2 * MAX_DNA // 1
    cell = Cell(aq, MIN_DNA, Vec(WIDTH // 2 + random.randint(-100, 100), HEIGHT // 2 + random.randint(-100, 100)))
    aq.cells.append(cell)
    cell.color = [150, 25, 25]
    cell = Cell(aq, (MIN_DNA + MAX_DNA) // 2, Vec(WIDTH // 2 + random.randint(-100, 100), HEIGHT // 2 + random.randint(-100, 100)))
    aq.cells.append(cell)
    cell.color = [25, 150, 25]
    cell = Cell(aq, MAX_DNA, Vec(WIDTH // 2 + random.randint(-100, 100), HEIGHT // 2 + random.randint(-100, 100)))
    aq.cells.append(cell)
    cell.color = [25, 25, 150]
    
main()