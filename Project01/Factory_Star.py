import random

from pico2d import *
import pygame

pygame.mixer.init()
class Star:
    image = None;

    def __init__(self):
        self.x, self.y = 800, 90
        self.bgm = pygame.mixer.Sound('Sounds\\star.wav')
        if Star.image == None:
            Star.image = load_image('Graphics\\redstar.png')

    def playsong(self):
        self.bgm.set_volume(0.7)
        self.bgm.play()
    def update(self, frame_time):
        self.x -= 25

        pass

    def draw(self,frame_time):
        self.image.draw(self.x, self.y)
        #draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15

