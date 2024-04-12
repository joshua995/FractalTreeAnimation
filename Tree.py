"""
Joshua Liu
2022-12-22
Fractal tree animation - looped
"""


import pygame
from math import pi, cos, sin
from random import randint

from pygame import RESIZABLE


class Apple(object):
    def __init__(self, x, y):
        self.x, self.y, self.fallSpeed = x, y, 0

    def draw_self(self):
        pygame.draw.circle(scr, (255, 0, 0), (self.x, self.y), 5)


pygame.init()

clock = pygame.time.Clock()

skyColor = (0, 0, 0)

screenWidth, screenHeight = 600, 600
scr = pygame.display.set_mode((screenWidth, screenHeight), RESIZABLE)
pygame.display.set_caption("Fractal Tree Animation")
scr.fill(skyColor)

done, initFrameRate = False, 25

treeColor, redishTreeColor = (0, 0, 0), (200, 0, 0)
branchLength, deltaTheta, theta = 100, pi / 10, pi / 2
multiplierRight, multiplierLeft, thickness, addingThickness = 0.8, 0.8, branchLength, False

sunColor, sunColorIncrementAmount, sunRadius = (20, 20, 0), 4.3, 50
sunPos, movement, diagonalUp, straight, sunStoppedPos, apples = (-sunRadius, 180), 2.25, True, False, (), []


def draw_sun(color):
    pygame.draw.circle(scr, color, sunPos, sunRadius)


def draw_branch(screen, x, y, color, length, theta, delta_theta):
    if length <= thickness:
        return
    x2, y2 = x - length * cos(theta), y - length * sin(theta)
    pygame.draw.line(screen, color, (x, y), (x2, y2))
    color, rand = (color[0], color[1] + 12.5, color[2]), randint(0, 10000)
    if rand == 0:
        apples.append(Apple(x2, y2))
    draw_branch(scr, x2, y2, color, length * multiplierRight, theta + delta_theta, delta_theta)
    draw_branch(scr, x2, y2, color, length * multiplierLeft, theta - delta_theta, delta_theta)


def set_frame_rate():
    if thickness < branchLength / 4:
        clock.tick(initFrameRate + 40)
    elif thickness < branchLength / 3:
        clock.tick(initFrameRate + 25)
    elif thickness < branchLength / 2:
        clock.tick(initFrameRate + 10)
    else:
        clock.tick(initFrameRate)


def add_apples(apple):
    if apple.fallSpeed == 0:
        apple.fallSpeed = randint(6, 7)
    apple.y += apple.fallSpeed
    apple.draw_self()
    if apple.y > screenHeight:
        apples.remove(apple)


def draw_apples(apple):
    apple.draw_self()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    draw_sun(sunColor)
    if not straight and diagonalUp and not addingThickness:
        skyColor = (0, skyColor[1] + 3, skyColor[2] + 4.5)
        sunColor = (sunColor[0] + sunColorIncrementAmount, sunColor[1] + sunColorIncrementAmount, sunColor[2])
        sunPos = (sunPos[0] + movement * 2, sunPos[1] - movement)
        if sunPos[0] >= 120 and sunPos[1] <= 60:
            sunStoppedPos, diagonalUp, straight = sunPos, False, True
    elif straight:
        sunPos = (sunPos[0] + movement, sunPos[1])
        if sunPos[0] >= screenWidth - sunStoppedPos[0] and sunPos[1] <= sunStoppedPos[1]:
            straight = False
    elif not diagonalUp:
        skyColor = (0, skyColor[1] - 3, skyColor[2] - 4.5)
        sunColor = (sunColor[0] - sunColorIncrementAmount, sunColor[1] - sunColorIncrementAmount, sunColor[2])
        sunPos = (sunPos[0] + movement * 2, sunPos[1] + movement)
        if sunPos[0] >= screenWidth + sunRadius and sunPos[1] <= 180:
            skyColor, sunColor, sunPos, diagonalUp = (0, 0, 0), (100, 100, 0), (-sunRadius, 180), True

    draw_branch(scr, screenWidth / 2 - branchLength / 1.9, screenHeight, treeColor, branchLength / 5.5, theta + 0.1,
                deltaTheta / 4)
    draw_branch(scr, screenWidth / 2 + branchLength / 1.9, screenHeight, treeColor, branchLength / 5.5, theta - 0.1,
                deltaTheta / 4)
    draw_branch(scr, screenWidth / 2 - branchLength * 1.2, screenHeight, redishTreeColor, branchLength / 2, theta - 0.2,
                deltaTheta / 2)
    draw_branch(scr, screenWidth / 2 + branchLength * 1.2, screenHeight, redishTreeColor, branchLength / 2, theta + 0.2,
                deltaTheta / 2)
    draw_branch(scr, screenWidth / 2, screenHeight, treeColor, branchLength, theta, deltaTheta)
    if addingThickness:
        list(map(add_apples, apples))
        thickness += 1
        if thickness >= branchLength:
            skyColor, sunColor, sunPos = (0, 0, 0), (20, 20, 0), (-sunRadius, 180)
            diagonalUp, addingThickness = True, False
    else:
        thickness -= 1
        if thickness <= 1:
            addingThickness = True
    list(map(draw_apples, apples))
    set_frame_rate()
    pygame.display.update()
    scr.fill(skyColor)
