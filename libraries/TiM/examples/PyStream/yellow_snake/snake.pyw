#!/usr/bin/python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#           Name: snake.py
#         Author: Brock Glaze
#        Created: 09/25/11
#    Description:
#------------------------------------------------------------------------------
import sfuncs, sobj, pygame
from colors import hue
import sys
sys.path.append('..')
import TiM
# Modes
NORMAL, DRAW = range(2)
# Directions
LEFT, RIGHT, UP, DOWN = range(4)



#------------------------------------------------------------------------------
# Game Object
#------------------------------------------------------------------------------

class Snake(object):
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        #---
        ## (extend_by, snake.speed, blocks_to_level)
        self.difficulty1 = (2, 6, 0)
        self.difficulty2 = (4, 5, 60)
        self.difficulty3 = (6, 4, 120)
        #---
        self.draw_mode_speed = 10
        #---
        self.fps = 80
        self.animation_delay = 15
        #---
        self.BLOCKSIZE  = 15
        self.MATRIX_W = 8
        self.MATRIX_H = 16
        self.SW = self.BLOCKSIZE * self.MATRIX_W
        self.SH = self.BLOCKSIZE * self.MATRIX_H
        #---
        self.screen = pygame.display.set_mode((self.SW, self.SH))
        self.scrRect = self.screen.get_rect()
        self.background = TiM.Surface(self.BLOCKSIZE, (self.SW, self.SH))
        #---
        self.caption = ("Yellow Snake - F5 to restart | SPACE to pause | "
        "F12 to draw")
        self.icon = pygame.image.load('data/icon.png')
        #---
        self.loads = sobj.Loads(self)
        #---
        self.head = None
        self.body = None
        #---
        self.food = None
        self.extend_by = None
        self.draw_mode_extend_by = 6
        #---
        self.frames = None
        #---
        self.mode = NORMAL
        self.paused = None
        self.score = None
        self.level = None
        #--- Sprite Groups ---
        self.hGroup = None
        self.bGroup = None
        self.foodGroup = None
        #---
        self.you_lose = None
        self.current_hs = None
        self.check_hs = None
        #---
        self.start_over()
    
    def lengthen(self, length):
        for block in range(length):
            self.body.append(sobj.Body(self))
            self.bGroup.add(self.body[len(self.body)-1])
    
    def start(self):
        game_loop(self)
    
    def start_over(self):
        self.head = sobj.Head(self)
        self.head.speed = self.difficulty1[1]
        self.body = []
        self.food = sobj.Food(self)
        self.extend_by = self.difficulty1[0]
        #---
        self.frames = 0
        #---
        self.paused = False
        self.score = 0
        self.level = 1
        #---
        self.hGroup = None
        self.bGroup = None
        self.foodGroup = None
        #---
        self.you_lose = False
        self.current_hs = sfuncs.get_current_high_score(self)
        self.check_hs = 0
        
        # Display caption and icon
        pygame.display.set_caption(self.caption)
        pygame.display.set_icon(self.icon)
        
        # Fill and blit background color
        self.background.fill(hue('BLACK'))
        self.screen.blit(self.background, (0, 0))
        
        # Create Sprite Groups
        sfuncs.create_sprite_groups(self)
        
        # Add Snake head to hGroup
        self.body.append(self.head)
        self.hGroup.add(self.body[0])
        
        # Add Snake body to hGroup
        self.lengthen(self.extend_by)
        
        # Add Food to foodGroup
        self.foodGroup.add(self.food)



#------------------------------------------------------------------------------



#------------------------------------------------------------------------------
# Main Loop
#------------------------------------------------------------------------------

def game_loop(g):
    
    running = True
    while running:
        g.clock.tick(g.fps)
        g.frames+=1



#------------------------------------------------------------------------------
# Events
#------------------------------------------------------------------------------
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_F5:
                    g.start_over()
                elif event.key == pygame.K_SPACE:
                    if g.paused: g.paused = False
                    else: g.paused = True
                elif event.key == pygame.K_F12:
                    if g.mode == NORMAL:
                        g.mode = DRAW
                        g.score = 0
                        if g.you_lose:
                            g.start_over()
                    else:
                        g.mode = NORMAL
                        g.start_over()
                
                # Snake Movement
                elif ((event.key == pygame.K_LEFT or event.key == pygame.K_a)
                and (not g.head.direction == RIGHT
                and not g.head.last_pos[1] == g.head.rect.centery)
                and not g.paused):
                    g.head.direction = LEFT
                
                elif ((event.key == pygame.K_RIGHT or event.key == pygame.K_d)
                and (not g.head.direction == LEFT
                and not g.head.last_pos[1] == g.head.rect.centery)
                and not g.paused):
                    g.head.direction = RIGHT
                
                elif ((event.key == pygame.K_UP or event.key == pygame.K_w)
                and (not g.head.direction == DOWN
                and not g.head.last_pos[0] == g.head.rect.centerx)
                and not g.paused):
                    g.head.direction = UP
                
                elif ((event.key == pygame.K_DOWN or event.key == pygame.K_s)
                and (not g.head.direction == UP
                and not g.head.last_pos[0] == g.head.rect.centerx)
                and not g.paused):
                    g.head.direction = DOWN



#------------------------------------------------------------------------------
# Sprite Methods
#------------------------------------------------------------------------------
        
        sfuncs.group_update(g)
        sfuncs.group_clear(g)
        
        # Blit Background Color/Image
        g.screen.blit(g.background, (0, 0))
        
        sfuncs.group_draw(g)
        
        sfuncs.pause_and_level_check(g)
        
        if g.mode == DRAW:
            sfuncs.print_mode_draw(g)
        else:
            sfuncs.print_current_hs(g)
            sfuncs.print_score(g)
        
        if g.you_lose:
            if not g.check_hs:
                g.check_hs = sfuncs.check_high_score(g)
            elif g.check_hs == 1:
                sfuncs.print_new_hs2(g)
            elif g.check_hs == 2:
                sfuncs.print_you_lose(g)
                
        
        pygame.display.flip()



#------------------------------------------------------------------------------

if __name__ == '__main__':
    game = Snake()
    game.start()
    pygame.quit()
