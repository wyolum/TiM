import pycam
import time
import serial
from pylab import *
from numpy import *

CKSUM_FAIL = 'F'
READY = 'R'
CMD_COPYONLY = chr(0)
CMD_SHOW = 'S'

class Dummy():
    def read(self, n=1):
        return 'R' * n
    def write(self, *args, **kw):
        pass
s = serial.Serial('/dev/ttyUSB1', baudrate=115200, timeout=.01)
# s = Dummy()

pixels = ones((64, 8, 3), uint8)

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
'''
### compute a checksum

0 = dot ([1, 2, 3, ..., k], [v, a, b, ..., c, '\n'])
0 = v + 2a + 3b + ... (k-1)c + k'\n'
v = -(2a + 3b + ... (k-1)c + k'\n')
v = -dot([2, 3, 4, ... k], [a, b, ..., v, '\n'])
v = -dot(arange(2, k + 1), [a, b, ...])
'''



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
makeMSG(0, 0)
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
        if col >= 16:
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

