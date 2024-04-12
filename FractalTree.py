import pygame
import math

theta = math.pi / 2


def drawBranch(screen, x, y, color, index, length, theta, deltaTheta, multiplierRight, multiplierLeft):
    if length <= 1:
        return
    x2 = x - length * math.cos(theta)
    y2 = y - length * math.sin(theta)
    if index == 0:
        pygame.draw.line(screen, (color, 0, 0), (x, y), (x2, y2))
    elif index == 1:
        pygame.draw.line(screen, (0, color, 0), (x, y), (x2, y2))
    else:
        pygame.draw.line(screen, (color, color, 0), (x, y), (x2, y2))
    color += 12.5
    drawBranch(screen, x2, y2, color, index, length * multiplierRight, theta + deltaTheta, deltaTheta, multiplierRight,
               multiplierLeft)
    drawBranch(screen, x2, y2, color, index, length * multiplierLeft, theta - deltaTheta, deltaTheta, multiplierRight,
               multiplierLeft)
