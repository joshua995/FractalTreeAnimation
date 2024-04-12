"""
Joshua Liu
2022-12-22
Fractal tree animation with procedural generation - looped
"""

import math
import random
import pygame
import FractalTree


class Tile(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.hasTree = False
        self.land = False
        self.whichWater = ""

        self.rect = pygame.Rect(self.x, self.y, blockSize, blockSize)

        self.neighbours = []

    def updateSelf(self, land, whichWater):
        if whichWater == "":
            if land:
                pygame.draw.rect(scr, grass, self.rect)
            else:
                pygame.draw.rect(scr, waterC, self.rect)
        else:
            if whichWater == "top":
                pygame.draw.rect(scr, topWaterC, self.rect)
                if random.randint(0, 2) == 0:
                    pygame.draw.rect(scr, waterWaveC, (self.x, self.y + blockSize / 2.5, blockSize, blockSize / 5))
                    pygame.draw.rect(scr, waterC, (self.x, self.y + blockSize * 0.6, blockSize, blockSize / 2.5))
                else:
                    pygame.draw.rect(scr, waterWaveC, (self.x, self.y + blockSize * 0.6, blockSize, blockSize / 5))
                    pygame.draw.rect(scr, waterC, (self.x, self.y + blockSize * 0.8, blockSize, blockSize / 5))
            elif whichWater == "left":
                pygame.draw.rect(scr, waterC, self.rect)
                pygame.draw.rect(scr, waterWaveC, (self.x, self.y, blockSize / 5, blockSize))
            elif whichWater == "right":
                pygame.draw.rect(scr, waterC, self.rect)
                pygame.draw.rect(scr, waterWaveC, (self.x + blockSize * 0.8, self.y, blockSize / 5, blockSize))
            elif whichWater.__contains__("bot") and whichWater.__contains__("left"):
                pygame.draw.rect(scr, waterC, self.rect)
                pygame.draw.rect(scr, waterWaveC, (self.x, self.y, blockSize / 5, blockSize))
            elif whichWater.__contains__("bot") and whichWater.__contains__("right"):
                pygame.draw.rect(scr, waterC, self.rect)
                pygame.draw.rect(scr, waterWaveC, (self.x + blockSize * 0.8, self.y, blockSize / 5, blockSize))
            elif whichWater.__contains__("top") and whichWater.__contains__("left"):
                pygame.draw.rect(scr, topWaterC, self.rect)
                if random.randint(0, 2) == 0:
                    pygame.draw.rect(scr, waterWaveC, (self.x, self.y + blockSize / 2.5, blockSize, blockSize / 5))
                    pygame.draw.rect(scr, waterC, (self.x, self.y + blockSize * 0.6, blockSize, blockSize / 2.5))
                    pygame.draw.rect(scr, waterWaveC,
                                     (self.x, self.y + blockSize * 0.6, blockSize / 5, blockSize / 2.5))
                else:
                    pygame.draw.rect(scr, waterWaveC, (self.x, self.y + blockSize * 0.6, blockSize, blockSize / 5))
                    pygame.draw.rect(scr, waterC, (self.x, self.y + blockSize * 0.8, blockSize, blockSize / 5))
                    pygame.draw.rect(scr, waterWaveC, (self.x, self.y + blockSize * 0.8, blockSize / 5, blockSize / 5))
            elif whichWater.__contains__("top") and whichWater.__contains__("right"):
                pygame.draw.rect(scr, topWaterC, self.rect)
                if random.randint(0, 2) == 0:
                    pygame.draw.rect(scr, waterWaveC, (self.x, self.y + blockSize / 2.5, blockSize, blockSize / 5))
                    pygame.draw.rect(scr, waterC, (self.x, self.y + blockSize * 0.6, blockSize, blockSize / 2.5))
                    pygame.draw.rect(scr, waterWaveC, (
                        self.x + blockSize * 0.8, self.y + blockSize * 0.6, blockSize / 5, blockSize / 2.5))
                else:
                    pygame.draw.rect(scr, waterWaveC, (self.x, self.y + blockSize * 0.6, blockSize, blockSize / 5))
                    pygame.draw.rect(scr, waterC, (self.x, self.y + blockSize * 0.8, blockSize, blockSize / 5))
                    pygame.draw.rect(scr, waterWaveC,
                                     (self.x + blockSize * 0.8, self.y + blockSize * 0.8, blockSize / 5, blockSize / 5))
            elif whichWater.__contains__("left") and whichWater.__contains__("right"):
                pygame.draw.rect(scr, waterC, self.rect)
                pygame.draw.rect(scr, waterWaveC, (self.x, self.y, blockSize / 5, blockSize))
                pygame.draw.rect(scr, waterWaveC, (self.x + blockSize * 0.8, self.y, blockSize / 5, blockSize))

    def getInitNeighbours(self):
        for tile in tiles:
            if (tile.x == self.x + blockSize and tile.y == self.y) or \
                    (tile.x == self.x - blockSize and tile.y == self.y) or \
                    (tile.x == self.x and tile.y == self.y + blockSize) or \
                    (tile.x == self.x and tile.y == self.y - blockSize):
                self.neighbours.append(tile)

    def changeTile(self):
        isWaterCount = 0
        for neighbour in self.neighbours:
            if not neighbour.land:
                isWaterCount += 1
        if isWaterCount >= 3:
            self.land = False
        isLandCount = 0
        for neighbour in self.neighbours:
            if neighbour.land:
                isLandCount += 1
        if isLandCount >= 3:
            self.land = True


pygame.init()

clock = pygame.time.Clock()

screenWidth = 500
screenHeight = 500
scr = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("The Land")

done = False

# multiple of 5
blockSize = 15

tiles = []
waterTiles = []
landTiles = []
treeTiles = []

grass = (0, 255, 0)
waterC = (0, 0, 255)
topWaterC = (0, 0, 110)
waterWaveC = (0, 150, 255)

size = width, height = (screenWidth, screenHeight)
night = pygame.Surface(size)
night.fill((0, 0, 0))
alpha = 0
addingAlpha = True


def createGrid():
    for row in range(0, screenHeight, blockSize):
        for col in range(0, screenWidth, blockSize):
            tiles.append(Tile(row, col))
            rand = random.randint(0, 1)
            if rand == 1 or rand == 2:
                tiles[len(tiles) - 1].land = True
            else:
                tiles[len(tiles) - 1].land = False


def getNeighbours():
    for tile in tiles:
        tile.getInitNeighbours()


def generateRandomLand(amount):
    tiles.clear()
    waterTiles.clear()
    landTiles.clear()
    treeTiles.clear()
    createGrid()
    getNeighbours()
    for i in range(amount):
        for tile in tiles:
            tile.changeTile()
    getLandAndWaterTiles()
    for tile in tiles:
        for wTile in waterTiles:
            if wTile.neighbours.__contains__(tile) and tile.land:
                if tile.x == wTile.x and tile.y == wTile.y - blockSize:
                    wTile.whichWater += "top"
                    wTile.updateSelf(wTile.land, wTile.whichWater)
                elif tile.x == wTile.x and tile.y == wTile.y + blockSize:
                    wTile.whichWater += "bot"
                    wTile.updateSelf(wTile.land, wTile.whichWater)
                elif tile.x == wTile.x - blockSize and tile.y == wTile.y:
                    wTile.whichWater += "left"
                    wTile.updateSelf(wTile.land, wTile.whichWater)
                elif tile.x == wTile.x + blockSize and tile.y == wTile.y:
                    wTile.whichWater += "right"
                    wTile.updateSelf(wTile.land, wTile.whichWater)
            else:
                wTile.updateSelf(wTile.land, wTile.whichWater)
    for tile in landTiles:
        globals()["grass"] = (0, random.randint(240, 255), 0)
        tile.updateSelf(tile.land, tile.whichWater)
        if globals()["grass"][1] == 240 and tile.y != 0:
            tile.hasTree = True
            treeTiles.append(tile)
    for tile in treeTiles:
        multiplerRight = random.uniform(0.6, 0.8)
        multiplerLeft = random.uniform(0.6, 0.8)
        branchLength = random.uniform(10, 15)
        diviser = random.uniform(6, 10)
        rgbIndex = random.randint(0, 2)
        FractalTree.drawBranch(scr, tile.x + blockSize / 2, tile.y + blockSize / 2, 0, rgbIndex, branchLength,
                               FractalTree.theta, math.pi / diviser, multiplerRight, multiplerLeft)


def getLandAndWaterTiles():
    for tile in tiles:
        if tile.land:
            landTiles.append(tile)
        else:
            waterTiles.append(tile)


generateRandomLand(random.randint(3, 10))
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    night.set_alpha(alpha)
    scr.blit(night, (0, 0))
    alpha += .2
    if alpha >= 16:
        alpha = 0
        night = pygame.Surface(size)
        night.fill((0, 0, 0))
        generateRandomLand(random.randint(3, 10))
    pygame.display.update()
    clock.tick(10)
