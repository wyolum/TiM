# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 00:06:07 2011
@title: colors module
@author: Brock Glaze
"""

def hue(get_hue):
    
    hue_dict = {'aqua': (0, 255, 255),
                'black': (0, 0, 0),
                'blue': (0, 0, 255),
                'brown': (139, 69, 19),
                'cornflower blue': (100, 149, 237),
                'deep pink': (255, 20, 147),
                'fuchsia': (255, 0, 255),
                'grey': (128, 128, 128),
                'gray': (128, 128, 128),
                'green': (0, 128, 0),
                'pink': (255, 105, 180),
                'light purple': (132, 112, 255), 
                'lime': (0, 255, 0),
                'maroon': (128, 0, 0),
                'navy blue': (0, 0, 128),
                'olive': (128, 128, 0),
                'orange': (255, 165, 0),
                'orange red': (255, 69, 0),
                'purple': (128, 0, 128),
                'red': (255, 0, 0),
                'silver': (192, 192, 192),
                'teal': (0, 128, 128),
                'white': (255, 255, 255),
                'yellow': (255, 255, 0),
                }
    
    
    if get_hue.lower() == 'dict':
        return hue_dict
    
    elif get_hue.lower() == 'all':
        all_colors = []
        for i in hue_dict.keys():
            all_colors.append(hue_dict[i])
        return all_colors
    
    elif get_hue.lower() in hue_dict.keys():
        return hue_dict[get_hue.lower()]
    
    else:
        print("*** Color '%s' not in dict" % get_hue.lower())
        return



#------------------------------------------------------------------------------

if __name__ == '__main__':
    print('This is a module. Run cargo_carrier.py')