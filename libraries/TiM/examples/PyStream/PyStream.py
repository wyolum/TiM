import pycam
import time
import serial
from pylab import *
from numpy import *

CKSUM_FAIL = 'F'
READY = 'R'
CMD_COPYONLY = chr(0)
CMD_SHOW = 'S'

s = serial.Serial('/dev/ttyUSB0', baudrate=115200, timeout=.01)

pixels = ones((64, 8, 3), uint8)

def cksum(msg):
    return int((sum([ord(c) for c in msg])) % 256) == 0

def makeMSG(row, col, cmd=CMD_COPYONLY):
    buffer = pixels[col: col + 16, row]
    # buffer = ones((16, 3), uint8) * 25

    cksum_val = -int(sum(buffer) + row + col + ord('\n'))
    cksum_val %= 256
    out = '%s%s%s%s%s\n' % (buffer.tostring(), chr(row), chr(col), chr(cksum_val), cmd)
    if not cksum(out):
        raise ValueError('Cksum reality check failed!?')
    return out

count = 0
row = 0
col = 0
def update_pixels(image):
    global row, col, count

    ## resize for display

    ## image is 640x480
    ## pixels is 32x16
    display = (image[::20,::30] // 16) ** 1.5

    ## black and white?
    # xsdisplay[:,:] = sum(display, axis=2)[:,:,newaxis] ## comment out for color

    ## swap channels 0 and 1
    tmp = display[:,:,0]
    display[:,:,0] = display[:,:,1]
    display[:,:,1] = tmp
    
    pixels[:16] = display[:16,8:]
    pixels[16:32] = display[:16,:8]
    pixels[32:48] = display[16:,:8]
    pixels[48:] = display[16:,8:]
    c = s.read(1)
    if c == READY:
        s.write(makeMSG(row, col))
        col += 16
        if col >= 64:
            col *= 0
            row += 1
            if row == 8:
                row *= 0
                count += 1
    else:
        pass
        # print 'not ready, c = %s' % c

cam = pycam.Capture(update_pixels)
cam.main()

