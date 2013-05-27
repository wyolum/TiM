import pygame
import pygame.camera
from pygame.locals import *


class Capture(object):
    def __init__(self, callback):
        self.going = False
        self.callback = callback;
        pygame.init()
        pygame.camera.init()
        self.size = (640,480)

        # create a display surface. standard pygame stuff
        self.display = pygame.display.set_mode(self.size, 0)
        
        # this is the same as what we saw before
        self.clist = pygame.camera.list_cameras()
        if not self.clist:
            raise ValueError("Sorry, no cameras detected.")
        ## self.cam = pygame.camera.Camera(self.clist[0], self.size)
        self.cam = pygame.camera.Camera(self.clist[0], self.size, "RGB")
        self.cam.start()

        # create a surface to capture to.  for performance purposes
        # bit depth is the same as that of the display surface.
        self.snapshot = pygame.surface.Surface(self.size, 0, self.display)

    def get_and_flip(self):
        # if you don't want to tie the framerate to the camera, you can check 
        # if the camera has an image ready.  note that while this works
        # on most cameras, some will never return true.
        if self.cam.query_image():
            self.snapshot = self.cam.get_image(self.snapshot)

        # blit it to the display surface.  simple!
        self.display.blit(self.snapshot, (0,0))
        if self.going:
            self.callback(pygame.surfarray.pixels3d(self.display))
        pygame.display.flip()

    def main(self):
        self.going = True
        while self.going:
            events = pygame.event.get()
            for e in events:
                if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                    # close the camera safely
                    self.cam.stop()
                    self.going = False
            self.get_and_flip()
def old():

    cam = pygame.camera.Camera("/dev/video0",(640,480))
    cam.start()
    image = cam.get_image()
    print dir(image)
