import pygame
import time
import random


class rain_drop:

    def __init__(self,position_x,width,height):

        self.position_x = list(position_x)
        self.width = int(width)
        self.height = int(height)

    def draw_drop(self):
        color = [255,0,255]
        return pygame.draw.line(simulation_window,color,self.position_x,[self.position_x[0],self.position_x[1] + self.height],self.width)

def setup():

    global raining
    global simulation_window
    global game_rain_drops
    global sim_window_height
    global sim_window_width

    global velocity
    velocity = 20

    sim_window_height = 400
    sim_window_width = 840

    raining = True

    pygame.init()
    simulation_window = pygame.display.set_mode((sim_window_width,sim_window_height))
    pygame.display.set_caption("Purple Rain")
    game_rain_drops = []

    for i in range(10000):

        new_drop = rain_drop([random.randint(0,sim_window_width),random.randint(-sim_window_height,0)],random.randint(0,7),random.randint(0,4))
        game_rain_drops.append(new_drop)
"""
    for drop in game_rain_drops:
        print(f"Drop info: PositionX : {drop.position_x}\tWidth : {drop.width}\tHeight : {drop.height}\n")

"""

def draw():

    global raining
    global pause
    raining = True
    pause = False
    while raining:

        pygame.time.delay(100)
        simulation_window.fill((225,225,225))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raining = False
            if event.type == pygame.K_SPACE:
                pause = True

        if pause == True:
            velo = 0
        else:
            velo = velocity

        for drop in game_rain_drops:

            drop.position_x[1] += velo

            if drop.position_x[1] > sim_window_height:
                drop.position_x[1] = random.randint(-200,0)
            drop.draw_drop()
        pygame.display.update()


setup()
draw()