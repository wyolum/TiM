import PIL.Image as Image
import time
import serial
from pylab import *
from numpy import *

CKSUM_FAIL = 'F'
READY = 'R'
SWAP_01 = True
SWAP_02 = False
SWAP_12 = False
CMD_COPYONLY = chr(0)
CMD_SHOW = 'S'

s = serial.Serial('/dev/ttyUSB0', baudrate=115200, timeout=.01)
while s.read():
    pass
NCOL = 16
NROW = 8
pixels = zeros((NCOL, NROW, 3), uint8)

def cksum(msg):
    return int((sum([ord(c) for c in msg])) % 256) == 0

def makeMSG(row, col, cmd=CMD_COPYONLY):
    buffer = pixels[col: col + 16, row]
    cksum_val = -int(sum(buffer) + row + col + ord(cmd) + ord('\n'))
    cksum_val %= 256
    out = '%s%s%s%s%s\n' % (buffer.tostring(), chr(row), chr(col), chr(cksum_val), cmd)
    if not cksum(out):
        raise ValueError('Cksum reality check failed!?')
    return out

count = 0
row = 0
col = 0
BACKGROUND = array([15, 15, 20]) ## Just for MaTris

def update_pixels(new_display):
    global row, col, count
    ## for pylab
    new_display = new_display[:,::-1]
    
    display = new_display
    ## black and white?
    # xsdisplay[:,:] = sum(display, axis=2)[:,:,newaxis] ## comment out for color
    if False:
        pixels[:16] = display[:16,8:]
        pixels[16:32] = display[:16,:8]
        pixels[32:48] = display[16:,:8]
        pixels[48:] = display[16:,8:]
    else:
        pixels[:16] = display[:16]
    # pixels[:,:,0] += 100 ### GREEN
    # pixels[:,:,1] += 100 ### RED
    # pixels[:,:,2] += 100 ### BLUE
    if SWAP_01:
        tmp = array(pixels[:,:,0], copy=True)
        pixels[:,:,0] = pixels[:,:,1]
        pixels[:,:,1] = tmp
    elif SWAP_02:
        tmp = array(pixels[:,:,0], copy=True)
        pixels[:,:,0] = pixels[:,:,2]
        pixels[:,:,2] = tmp
    elif SWAP_12:
        tmp = array(pixels[:,:,1], copy=True)
        pixels[:,:,1] = pixels[:,:,2]
        pixels[:,:,2] = tmp


    for r in range(8):
        for c in range(0, NCOL, 16):
            if c == 48:
                cmd = CMD_SHOW
            else:
                cmd = CMD_COPYONLY
            alamode_response = s.read()
            while alamode_response != READY:
                alamode_response = s.read()
                pass
            s.write(makeMSG(r, c, cmd=cmd))

def test_pattern(val):
    i = arange(8)
    for XX in range(100):
        for j in range(8):
            px = zeros((NCOL, NROW, 3), uint8) 
            px[i + j, i] = val
            px[8-i + j, i] = val
            update_pixels(px)
        for j in range(7, -1, -1):
            px = zeros((NCOL, NROW, 3), uint8) 
            px[i + j, i] = val
            px[8-i + j, i] = val
            update_pixels(px)
