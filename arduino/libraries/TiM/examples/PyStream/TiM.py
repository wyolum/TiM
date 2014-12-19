import pygame
import PIL.Image as Image
import time
import serial
from numpy import *
import copy
import os

CKSUM_FAIL = 'F'
READY = 'R'
SWAP_01 = True
SWAP_02 = False
SWAP_12 = False
CMD_COPYONLY = chr(0)
CMD_SHOW = 'S'

if os.uname()[1] == 'raspberrypi':
    port = '/dev/ttyS0'
    SYS = 'PI'
    N_READ = 1
else:
    if os.path.exists('/dev/ttyUSB0'):
        port = '/dev/ttyUSB0'
    elif os.path.exists('/dev/ttyACM0'):
        port = '/dev/ttyACM0'
    else:
        port = raw_input('enter serial port:')
    SYS = 'FTDI'
    N_READ = 2

s = serial.Serial(port, baudrate=115200, timeout=.01)

while 1:
    dat = s.read(10000) ## clear the buffer
    print dat
    if not dat:
        break
class Surface(pygame.Surface):
    def __init__(self, blocksize, *args, **kw):
        self.blocksize=blocksize
        super(Surface, self).__init__(*args, **kw)
    def flip(self):
        update_pixels(pygame.surfarray.pixels3d(self)
                      [self.blocksize//2::self.blocksize,
                       self.blocksize//2::self.blocksize]
                      .transpose((1, 0, 2)))        

NCOL = 16
NROW = 8
pixels = zeros((NCOL, NROW, 3), uint8)

RED   = [100, 0, 0]
GREEN = [0, 100, 0]
BLUE  = [0, 0, 100]
WHITE = [100, 100, 100]

def setPix(row, col, color):
    pixels[row, col,:] = color
    s.write(makeMSG(row, 0, cmd=CMD_COPYONLY))

scale = array([[1, 1, 1, 1, 1, 2, 1, 1],
               [1, 1, 1, 1, 2, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 2],
               [1, 1, 1, 1, 1, 1, 2, 2],
               [1, 1, 2, 1, 2, 1, 1, 1],
               [1, 1, 1, 1, 2, 1, 2, 2],
               [1, 1, 1, 1, 1.25, 1, 2, 1],
               [1, 1, 2, 1, 1.25, 2, 2, 2],
               [1, 1, 1, 2, 1, 2, 1, 1],
               [1, 1, 1, 1, 1, 2, 1, 2],
               [1, 1, 2, 1, 2, 2, 1, 2],
               [1, 1, 2, 1, 2, 2, 2, 2],
               [1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 2, 2, 2, 2, 1, 1],
               [2, 2, 2, 2, 2, 2, 2, 2]])

def fill(color):
    global pixels
    pixels *= 0
    pixels += color
    update_pixels(pixels)

def wheel(WheelPos, imax):
    ''' 
    Input a value 0 to 255 to get a color value.
    The colours are a transition r - g - b - back to r.
    '''
    if(WheelPos < 85):
        r = WheelPos * 3
        g = 255 - WheelPos * 3
        b = 0
    elif(WheelPos < 170):
        WheelPos -= 85
        r = 255 - WheelPos * 3
        g = 0
        b = WheelPos * 3
    else:
        WheelPos -= 170
        r = 0
        g = WheelPos * 3
        b = 255 - WheelPos * 3
    r = r * imax / 255
    g = g * imax / 255
    b = b * imax / 255
    return Color(r, g, b)

def Color(r, g, b):
    return array([g, r, b])

def gradient(maxv, center=(0,0)):
    for i in range(16):
        for j in range(8):
            d = sqrt((i - center[0] % 16) ** 2 + 
                     (j - center[1] % 8) ** 2) / sqrt(256 + 64)
            pixels[i, j] = wheel(d * 255, maxv)
    update_pixels(pixels)
def one_at_a_time():
    i = 8
    j = 4
    while 1:
        if random.random() > .5:
            j += 1
        else:
            j -= 1
        if random.random() > .5:
            i += 1
        else:
            i -= i
        i %= 8
        j %= 16
        gradient(100, (i, j))

last_msg = None
N_BYTE_PER_LED = 3
N_LED_PER_MSG = 16
MSG_LEN = (1                   + # CKSUM
           N_BYTE_PER_LED * N_LED_PER_MSG + 
           1                   + # ROW
           1                   + # COL
           1                   + # COMMAND
           1);                   # carrage return

def cksum(msg):
    n = len(msg)
    v = arange(n) + 1
    x = fromstring(msg, uint8)
    out = dot(v, x) % 256 == 0
    if not out:
        s = 0
        for i, y in zip(v, x):
            s += i * y
            print i, y, s % 256
            
    return out

def makeMSG(row, col, cmd=CMD_COPYONLY):
    buffer = pixels[col: col + 16, row].ravel()
    # buffer = ones((16, 3), uint8) * 25
    cksum_val = 256 - (dot(arange(16 * 3) + 2, buffer) + 
                       row * 50 +
                       col * 51 +
                       ord(cmd) * 52 + 
                       ord('\n') * 53)
    # cksum_val = -int(sum(buffer) + row + col + ord('\n'))
    cksum_val %= 256
    out = '%s%s%s%s%s\n' % (chr(cksum_val), buffer.tostring(), 
                            chr(row), chr(col), cmd)
    if not cksum(out):
        raise ValueError('Cksum reality check failed!?')
    return out
count = 0
row = 0
col = 0
BACKGROUND = array([15, 15, 20]) ## Just for MaTris
# COLOR_ADJUST = diag([1, 1, 1]) ## no adjust
COLOR_ADJUST = diag([1, .01, .01]) ## cut blue and green by 2

def setColorAdjust(r, g, b):
    global COLOR_ADJUST
    COLOR_ADJUST *= 0
    COLOR_ADJUST[0, 0] = r
    COLOR_ADJUST[1, 1] = g
    COLOR_ADJUST[2, 2] = b

def update_pixels(new_display):
    global row, col, count, last_msg

    ## for pylab
    # new_display[:,:,:] = new_display * scale[:,:,newaxis]
    # new_display[:,:,:] = new_display.astype(uint8)
    new_display = dot(new_display, COLOR_ADJUST).astype(uint8)
    new_display = new_display[::-1,::-1]
    
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
            last_msg = makeMSG(r, c, cmd=cmd)
            s.write(last_msg)
            alamode_resp = s.read(N_READ).strip()
            if alamode_resp:
                while alamode_resp[0] != READY:
                    s.read(1000)
                    s.write(last_msg)
                    time.sleep(.1)
                    alamode_resp = s.read(N_READ).strip()

def test_pattern(val):
    i = arange(8)
    for XX in range(100):
        print XX
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
