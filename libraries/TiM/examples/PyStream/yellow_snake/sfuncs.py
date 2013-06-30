# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#           Name: sfuncs.py
#         Author: Brock Glaze
#        Created: 09/25/11
#    Description:
#------------------------------------------------------------------------------
import pygame, os, random
from colors import hue

# Modes
NORMAL, DRAW = range(2)
# Directions
LEFT, RIGHT, UP, DOWN = range(4)



#------------------------------------------------------------------------------
# Randomization Functions
#------------------------------------------------------------------------------

def rand_dir():
    dirs = [LEFT, RIGHT, UP, DOWN]
    
    random.shuffle(dirs)
    return dirs[0]

def rand_x(sprite):
    g = sprite.g
    return random.randint((sprite.rect.width*2),
                          (g.scrRect.width-(sprite.rect.width*2)))

def rand_y(sprite):
    g = sprite.g
    return random.randint((sprite.rect.height*2),
                          (g.scrRect.height-(sprite.rect.height*2)))



#------------------------------------------------------------------------------
# Sprite Movement Functions
#------------------------------------------------------------------------------

def head_start(sprite):
    g = sprite.g
    # Set snake speed for level
    if g.mode == NORMAL:
        if g.level == 1 and not g.head.speed == g.difficulty1[1]:
            g.head.speed = g.difficulty1[1]
        elif g.level == 2 and not g.head.speed == g.difficulty2[1]:
            g.head.speed = g.difficulty2[1]
        elif g.level == 3 and not g.head.speed == g.difficulty3[1]:
            g.head.speed = g.difficulty3[1]
    elif g.mode == DRAW:
        g.head.speed = g.draw_mode_speed


def body_start(sprite):
    g = sprite.g
    for square in g.body:
        if square.leader_block:
            square.speed = square.leader_block.speed


def head_stop(sprite):
    sprite.speed = 0


def body_stop(sprite):
    g = sprite.g
    for square in g.body:
        square.speed = 0


def move_head(sprite):
    g = sprite.g
    
    if sprite.speed and g.frames % sprite.speed == 0:
        
        if sprite.direction == LEFT:
            sprite.x_velocity = -sprite.x_speed
            sprite.y_velocity = 0
        elif sprite.direction == RIGHT:
            sprite.x_velocity = sprite.x_speed
            sprite.y_velocity = 0
        elif sprite.direction == UP:
            sprite.x_velocity = 0
            sprite.y_velocity = -sprite.y_speed
        elif sprite.direction == DOWN:
            sprite.x_velocity = 0
            sprite.y_velocity = sprite.y_speed
        
        sprite.last_pos = sprite.rect.center
        sprite.rect.move_ip((sprite.x_velocity, sprite.y_velocity))
    
        if sprite.rect.left < g.scrRect.left:
            if g.mode == NORMAL:
                sprite.rect.left = g.scrRect.left
                head_stop(sprite)
                body_stop(sprite)
                g.you_lose = True
            elif g.mode == DRAW:
                sprite.rect.right = g.scrRect.right
        
        elif sprite.rect.right > g.scrRect.right:
            if g.mode == NORMAL:
                sprite.rect.right = g.scrRect.right
                head_stop(sprite)
                body_stop(sprite)
                g.you_lose = True
            elif g.mode == DRAW:
                sprite.rect.left = g.scrRect.left
        
        if sprite.rect.top < g.scrRect.top:
            if g.mode == NORMAL:
                sprite.rect.top = g.scrRect.top
                head_stop(sprite)
                body_stop(sprite)
                g.you_lose = True
            elif g.mode == DRAW:
                sprite.rect.bottom = g.scrRect.bottom
        
        elif sprite.rect.bottom > g.scrRect.bottom:
            if g.mode == NORMAL:
                sprite.rect.bottom = g.scrRect.bottom
                head_stop(sprite)
                body_stop(sprite)
                g.you_lose = True
            elif g.mode == DRAW:
                sprite.rect.top = g.scrRect.top


def move_body(sprite):
    g = sprite.g
    if sprite.leader_block.last_pos:
        if sprite.speed and g.frames % sprite.speed == 0:
            sprite.last_pos = sprite.rect.center
            sprite.rect.center = sprite.leader_block.last_pos



#------------------------------------------------------------------------------
# Sprite Collide Functions
#------------------------------------------------------------------------------

def collide_body(sprite):
    g = sprite.g
    if g.mode == NORMAL:
        body = pygame.sprite.spritecollideany(sprite, g.bGroup)
        if body:
            head_stop(sprite)
            g.you_lose = True


def eat_food(sprite):
    g = sprite.g
    food = pygame.sprite.spritecollideany(sprite, g.foodGroup)
    if food:
        g.lengthen(g.extend_by)
        food.move()
        if g.mode == NORMAL: g.score += (g.extend_by*10)


def food_body_spawn(sprite):
    g = sprite.g
    food = pygame.sprite.spritecollideany(sprite, g.foodGroup)
    if food:
        food.move()



#------------------------------------------------------------------------------
# Sprite Animation Functions
#------------------------------------------------------------------------------

def ani_body(sprite):
    g = sprite.g
    
    # Set body image based on level
    if g.mode == NORMAL:
        if sprite.g.level == 1 and not sprite.ani[1] == 1:
            sprite.ani = sprite.body1
            sprite.ani_frame = random.randint(0, (len(sprite.ani[0])-1))
    
        elif ((sprite.g.level == 2)
        or (sprite.g.level == 3 and g.you_lose)):
            sprite.ani = sprite.body2
            sprite.ani_frame = random.randint(0, (len(sprite.ani[0])-1))
    
        elif sprite.g.level == 3:
            sprite.ani = sprite.body3
            sprite.ani_frame = random.randint(0, (len(sprite.ani[0])-1))
    
    elif g.mode == DRAW:
        sprite.ani = sprite.body2
        sprite.ani_frame = random.randint(0, (len(sprite.ani[0])-1))
    
    # Run animation
    if sprite.ani_running:
        if (g.frames % sprite.frame_dly) == 0:
            if sprite.ani_frame < (len(sprite.ani[0])-1):
                sprite.ani_frame += 1
            else:
                sprite.ani_frame = 0
            sprite.image = sprite.ani[0][sprite.ani_frame]



#------------------------------------------------------------------------------
# Sprite Loop Functions
#------------------------------------------------------------------------------

def create_sprite_groups(g):
    # Create Sprite Groups
    g.hGroup = pygame.sprite.OrderedUpdates()
    g.bGroup = pygame.sprite.OrderedUpdates()
    g.foodGroup = pygame.sprite.RenderClear()


def group_update(g):
    # Call Groups' Update Method
    g.hGroup.update()
    g.bGroup.update()
    g.foodGroup.update()


def group_clear(g):
    # Erase old location of sprite with background color/image
    g.hGroup.clear(g.screen, g.background)
    g.bGroup.clear(g.screen, g.background)
    g.foodGroup.clear(g.screen, g.background)


def group_draw(g):
    # Draw sprite's new location
    g.bGroup.draw(g.screen)    
    # Keep this order to draw head on top
    g.hGroup.draw(g.screen)
    g.foodGroup.draw(g.screen)



#------------------------------------------------------------------------------
# Game Functions
#------------------------------------------------------------------------------

def pause_and_level_check(g):
    if g.paused and not g.you_lose:
        if g.head.speed > 0:
            head_stop(g.head)
            body_stop(g.head)
        print_paused(g)
    
    elif not g.you_lose:
        if g.mode == NORMAL:
            # Level up snake behavior if body count reached
            if g.level == 1 and len(g.body) >= g.difficulty2[2]:
                g.level = 2
                g.extend_by = g.difficulty2[0]
            elif g.level == 2 and len(g.body) >= g.difficulty3[2]:
                g.level = 3
                g.extend_by = g.difficulty3[0]
        
        elif g.mode == DRAW:
            g.extend_by = g.draw_mode_extend_by
        
        head_start(g.head)
        body_start(g.head)


def hs_file():
    if os.path.isfile('hsys'):
        return ('hsys')
    else:
        f = open('hsys', 'w')
        f.write('NOBODY 0')
        f.close()
        return('hsys')


def event_get_key():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return event.key
            else:
                pass


def hs_get_name(g):
    "ask(screen, question) -> answer"
    current_string = []
    print_input_box(g, "Name: %s" % ''.join(current_string))
    
    while True:
        inp_key = event_get_key()
        if inp_key == pygame.K_BACKSPACE:
            current_string = current_string[0:-1]
        elif inp_key == pygame.K_ESCAPE:
            break
        elif inp_key == pygame.K_RETURN:
            break
        elif inp_key == pygame.K_SPACE:
            current_string.append("_")
        elif inp_key == pygame.K_MINUS:
            current_string.append("_")
        elif inp_key <= 127:
            current_string.append((chr(inp_key).upper()))
        
        print_input_box(g, "Name: %s" % ''.join(current_string))
    
    return ''.join(current_string)



#------------------------------------------------------------------------------
# Printing
#------------------------------------------------------------------------------

def print_input_box(g, inp_text):
    
    fontObject = pygame.font.SysFont("Verdana", 30, False, True)
    if len(inp_text) != 0:
        group_update(g)
        group_clear(g)
        g.screen.blit(g.background, (0, 0))
        group_draw(g)
        print_score(g)
        print_current_hs(g)
        g.screen.blit(topText, topRect)
        g.screen.blit(fontObject.render(inp_text, 1, hue('WHITE')),
                      ((g.scrRect.centerx - 160), (topRect.bottom + 5)))
        
    pygame.display.flip()


def print_score(g):
    text = 'Score: %d ' % g.score
    
    reportFont = pygame.font.SysFont("Courier", 15, True, False)
    dispText = reportFont.render(text, True, hue('WHITE'))
    textRect = dispText.get_rect()
    textRect.left = g.scrRect.left
    textRect.top = g.scrRect.top + 15
    
    g.screen.blit(dispText, textRect)


def print_mode_draw(g):
    text = 'Mode: Draw'
    
    reportFont = pygame.font.SysFont("Courier", 15, True, False)
    dispText = reportFont.render(text, True, hue('WHITE'))
    textRect = dispText.get_rect()
    textRect.topleft = g.scrRect.topleft
    
    g.screen.blit(dispText, textRect)


def print_paused(g):
    top_text = ' Paused '
    bottom_text = ' Press [SPACE BAR] to Resume '
    
    topFont = pygame.font.SysFont("Verdana", 40, True, False)
    topText = topFont.render(top_text, True, hue('WHITE'))
    topRect = topText.get_rect()
    topRect.centerx = g.scrRect.centerx
    topRect.centery = (g.scrRect.centery - 30)
    g.screen.blit(topText, topRect)

    bottomFont = pygame.font.SysFont("Verdana", 30)
    bottomText = bottomFont.render(bottom_text, True, hue('WHITE'))
    bottomRect = bottomText.get_rect()
    bottomRect.centerx = g.scrRect.centerx
    bottomRect.y = (topRect.bottom + 5)
    g.screen.blit(bottomText, bottomRect)


def print_you_lose(g):
    top_text = ' Your Score: %d! ' % g.score
    bottom_text = ' Press [F5] to Start Over '
    
    topFont = pygame.font.SysFont("Verdana", 40, True, False)
    topText = topFont.render(top_text, True, hue('WHITE'))
    topRect = topText.get_rect()
    topRect.centerx = g.scrRect.centerx
    topRect.centery = (g.scrRect.centery - 30)
    g.screen.blit(topText, topRect)

    bottomFont = pygame.font.SysFont("Verdana", 30)
    bottomText = bottomFont.render(bottom_text, True, hue('WHITE'))
    bottomRect = bottomText.get_rect()
    bottomRect.centerx = g.scrRect.centerx
    bottomRect.y = (topRect.bottom + 5)
    g.screen.blit(bottomText, bottomRect)



#------------------------------------------------------------------------------
# Load Data Files
#------------------------------------------------------------------------------

def load_tile_map(w, h, file_name, trans):
    # Load a tiled map image and a return a list of row-lists
    tile_map = []
    master_image = load_image(file_name, trans)
    master_width, master_height = master_image.get_size()
    
    for tile_y in range(0, master_height // h):
        row = []
        tile_map.append(row)
        
        for tile_x in range(0, master_width // w):
            rect = (tile_x*w, tile_y*h, w, h)
            row.append(master_image.subsurface(rect))
    
    return tile_map


def load_image(file_name, use_color_key = False):
    image = pygame.image.load(file_name)
    
    # To speed things up, convert the images to SDL's internal format
    image = image.convert()
    
    if use_color_key is True:
        # Use the color of the pixel located at (0, 0) as our color key
        colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    
    return image


def load_sound(file_name):
    class DummySound:
        def play(self): pass
    
    if not pygame.mixer or not pygame.mixer.get_init():
        return DummySound()
    
    full_name = os.path.join(file_name)
    
    sound = pygame.mixer.Sound(full_name)
    
    return sound



#------------------------------------------------------------------------------
'''
if __name__ == '__main__':
    print('This is a module.')
'''
