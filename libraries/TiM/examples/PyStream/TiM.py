import PIL.Image as Image
import time
import serial
from numpy import *

CKSUM_FAIL = 'F'
READY = 'R'
SWAP_01 = True
SWAP_02 = False
SWAP_12 = False
CMD_COPYONLY = chr(0)
CMD_SHOW = 'S'

port = '/dev/ttyUSB0'
port = '/dev/ttyS0'

s = serial.Serial(port, baudrate=115200, timeout=.01)

while s.read(): ## clear the buffer
    pass
NCOL = 16
NROW = 8
pixels = zeros((NCOL, NROW, 3), uint8)
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

def update_pixels(new_display):
    global row, col, count, last_msg
    ## for pylab
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
            alamode_response = s.read()
            print alamode_response
            if alamode_response == CKSUM_FAIL and False:
                print '"%s"' % last_msg
                print s.read(MSG_LEN);
            while alamode_response != READY:
                alamode_response = s.read()
                pass
            last_msg = makeMSG(r, c, cmd=cmd)
            s.write(last_msg)

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
