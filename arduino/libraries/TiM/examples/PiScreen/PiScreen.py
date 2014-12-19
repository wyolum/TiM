from numpy import arange
import struct
import time
import numpy
import serial

A5 = 19
READY = 0b10101010
def Color(r, g, b):
    return numpy.array([g, r, b])

class PiScreen:
    def __init__(self, N, port, pin):
        self.ser = serial.Serial(port, baudrate=9600, timeout=.1)
        self.N = N
        self.buffer = numpy.zeros((8, N, 3), numpy.byte)
        # TODO: record pin

    def show(self):
        print self.ser.write(self.buffer.tostring()),
        total = 0
        next = 1
        while next > 0:
            next = sum(map(int, self.ser.read(1000).split()))
            total += next
        print 'total', total
    def setPixel(self, row, col, color):
        self.buffer[row, col] = color

    def off(self):
        self.buffer *= 0
        self.show()
        
    def __enter__(self):
        pass
    def __exit__(self, *args):
        self.off()
        
    def loop(self):
        last_row = 0
        while 1:
            msg = self.ser.read(1)
            if msg and ord(msg) == READY:
                row = ord(self.ser.read(1))
                if row < 8:
                    msg = self.buffer[row].tostring()
                    self.ser.write(msg)
                    if (row - last_row)%8 != 1:
                        print 'bad row', row, last_row
                    else:
                        print 'good row', row
                    last_row = row
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

def test():
    N = 64
    port = '/dev/ttyUSB0'
    port = '/dev/ttyACM0'

    strip = PiScreen(N, port, A5)
    count = 0
    print len(strip.buffer[0].tostring())
    for col in range(64):
        for row in range(8):
            strip.setPixel(col % 8, col, Color(25, 0,  0))
    strip.loop()
if __name__ == '__main__':
    test()
