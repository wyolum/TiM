# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#           Name: sobj.py
#         Author: Brock Glaze
#        Created: 09/25/11
#    Description:
#------------------------------------------------------------------------------
import pygame, sfuncs

# Modes
NORMAL, DRAW = range(2)
# Directions
LEFT, RIGHT, UP, DOWN = range(4)



#------------------------------------------------------------------------------
# Sprites
#------------------------------------------------------------------------------

class Head(pygame.sprite.Sprite):
    def __init__(self, g):
        pygame.sprite.Sprite.__init__(self)
        self.g = g
        self.image = self.g.loads.head
        self.rect = self.image.get_rect()
        #---
        self.direction = sfuncs.rand_dir()
        #---
        self.speed = self.g.difficulty1[1]
        #---
        self.x_speed = self.rect.width
        self.y_speed = self.rect.height
        #---
        self.x_velocity = 0
        self.y_velocity = 0
        #--- This formula sets the snake along the same grid as the food
        self.rect.x = (g.scrRect.centerx//self.rect.width)*self.rect.width
        self.rect.y = (g.scrRect.centery//self.rect.height)*self.rect.height
        #---
        self.leader_block = None
        self.last_pos = 0
    
    def update(self):
        sfuncs.move_head(self)
        sfuncs.collide_body(self)
        sfuncs.eat_food(self)


class Body(pygame.sprite.Sprite):
    def __init__(self, g):
        pygame.sprite.Sprite.__init__(self)
        self.g = g
        #--- Different body animation images
        self.body1 = (self.g.loads.body1[0], 1)
        self.body2 = (self.g.loads.body2[0], 2)
        self.body3 = (self.g.loads.body3[0], 3)
        #---
        self.ani = self.body1
        self.ani_running = True
        self.ani_frame = 0
        self.frame_dly = self.g.animation_delay
        #---
        self.image = self.ani[0][self.ani_frame]
        self.rect = self.image.get_rect()
        self.rect.centerx = -100
        self.rect.centery = -100
        #---
        self.speed = 0
        #---
        self.leader_block = self.g.body[-1]
        self.last_pos = 0
    
    def update(self):
        sfuncs.move_body(self)
        self.speed = self.leader_block.speed
        sfuncs.food_body_spawn(self)
        sfuncs.ani_body(self)


class Food(pygame.sprite.Sprite):
    def __init__(self, g):
        pygame.sprite.Sprite.__init__(self)
        self.g = g
        self.image = self.g.loads.food
        self.rect = self.image.get_rect()
        #---
        self.rect.x = (sfuncs.rand_x(self)//self.rect.width)*self.rect.width
        self.rect.y = (sfuncs.rand_y(self)//self.rect.height)*self.rect.height
    
    def move(self):
        self.rect.x = (sfuncs.rand_x(self)//self.rect.width)*self.rect.width
        self.rect.y = (sfuncs.rand_y(self)//self.rect.height)*self.rect.height



#------------------------------------------------------------------------------
# Pre-Load Objects
#------------------------------------------------------------------------------

class Loads(object):
    def __init__(self, g):
        self.g = g
        # Sound Files
        #self.a_sound = sfuncs.load_sound('data/a_sound.wav')
        
        #--- Images ---
        self.head = sfuncs.load_image('data/head.png', True)
        self.food = sfuncs.load_image('data/food.png', True)
        
        #--- Animations ---
        self.body1 = sfuncs.load_tile_map(15, 15, 'data/body1.png', True)
        self.body2 = sfuncs.load_tile_map(15, 15, 'data/body2.png', True)
        self.body3 = sfuncs.load_tile_map(15, 15, 'data/body3.png', True)



#------------------------------------------------------------------------------

if __name__ == '__main__':
    print('This is a module.')
