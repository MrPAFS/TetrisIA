# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 20:56:13 2019

@author: Casa
"""

import pygame
from random import randint
from Mesh import Mesh
from Block import Block

def adjust_block_position_x(position_x,block,mesh_size_x):
    array_of_block = block.get_array_of_block()
    
    if position_x < 0:
        for k in range(0,(-1)*position_x):
            for i in range(0,5):
                if array_of_block[i][k] == 1:
                    return (-1)*k
    elif position_x > mesh_size_x - 5:
        temp = position_x + 5 - mesh_size_x
        for k in range(4,4-temp,-1):
            for i in range(0,5):
                if array_of_block[i][k] == 1:
                    return mesh_size_x - 1 - k
          
    return position_x

def generate_random_Block(mesh_shape):
    
    possible_blocs_name = ['I','T','L','S-NORMAL','S-INVERTED','O']
    block_name = possible_blocs_name[randint(0,5)]
    block = Block(block_name)
    
    how_many_rotation = randint(0,4)
    for i in range(how_many_rotation):
        block.rotate_clockwise()
    
    return block

def draw_block(block, background,color,position_x,position_y,square_size):
    array_of_block = block.get_array_of_block()
    for i in range(5):
        for k in range(5):
            if array_of_block[i][k] == 1:
                pygame.draw.rect(background,color,((position_x + k)*20,(position_y + i)*20, square_size, square_size))

def switch(movent):
    return {
            'DOWN':(0,1),
            'LEFT':(-1,0),
            'RIGHT':(1,0)}[movent];
    
def move(block,movement,position_x,position_y,mesh_shape):
    move_x,move_y = switch(movement)
    
    position_x = adjust_block_position_x(position_x+move_x,block,mesh_shape[0])
    position_y += move_y
    
    return (position_x,position_y)

def rotate(block,direction):
    if(direction == 'CLOCKWISE'):
        block.rotate_clockwise()
    elif(direction == 'ANTICLOCKWISE'):
        block.rotate_anticlockwise()

#             WHITE      DeepSkyBlue    RED      YELLOW   SpringGreen  DarkViolet     Silver
colors = [(255,255,255),(0,191,255),(255,0,0),(255,255,0),(0,255,127),(148,0,211),(192,192,192)]
screen_shape = (480,640)
square_size = 20
drop_speed = 0.1
mesh_shape = (int(screen_shape[0]/square_size),int(screen_shape[1]/square_size))

mesh = Mesh(mesh_shape)

pos_x = 0
pos_y = 0

pygame.display.init()
background = pygame.display.set_mode(screen_shape)

play = True

block = Block('T')

"""pos_x,pos_y = move(block,'RIGHT',21,0,mesh_shape)

print(pos_x)
print(pos_y)"""

while play:
    
    for event in pygame.event.get():
        print(event)
        
        if event.type == pygame.QUIT:
            play = False
        elif event.type == pygame.KEYDOWN:
            if event.key == 275:
                pos_x,pos_y = move(block,'RIGHT',pos_x,pos_y,mesh_shape)
            elif event.key == 276:
                pos_x,pos_y = move(block,'LEFT',pos_x,pos_y,mesh_shape)
            elif event.key == 273:
                rotate(block,'CLOCKWISE')
            elif event.key == 274:
                rotate(block,'ANTICLOCKWISE')
    
    background.fill(colors[0])
    draw_block(block,background,colors[1],pos_x,pos_y,square_size)
    pygame.display.update()
    
pygame.display.quit()
