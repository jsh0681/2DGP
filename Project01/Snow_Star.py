from pico2d import *
import pygame
class Star:
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 10.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image = None;


    def __init__(self):
        self.x, self.y = 800, 90
        self.bgm = pygame.mixer.Sound('Sounds\\Snowstar.wav')
        if Star.image == None:
            Star.image = load_image('Graphics\\snowstar.png')

    def update(self, frame_time):
        self.x -= 25
    def playsong(self):
        self.bgm.set_volume(0.25)
        self.bgm.play()

        pass

    def draw(self,frame_time):
        self.image.draw(self.x, self.y)
       # draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15

