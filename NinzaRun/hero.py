import random

import pygame
pygame.mixer.init
from pico2d import *

class Hero:
    image = None

    SLIDE, JUMP, RUN = 0, 1, 2

    def __init__(self):
        self.x, self.y = 100, 90
        self.b=70
        self.jump = False
        self.slide = False
        self.frame = random.randint(0, 7)
        self.state = self.RUN
        if Hero.image == None:
            Hero.image = load_image('Graphics\\Ninja.png')

    def handle_events(self,event,frame_time):
        if (event.type,event.key) == (SDL_KEYDOWN,SDLK_DOWN):
            if self.jump == False and self.y<200:
                self.state = self.SLIDE
                pygame.mixer.music.load('Sounds\\slide.wav')
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play()
                self.b=50
                self.slide = True

        elif (event.type,event.key)==(SDL_KEYDOWN,SDLK_UP):
            if self.state in (self.RUN,self.JUMP):
                self.state = self.JUMP
                pygame.mixer.music.load('Sounds\\jump.wav')
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play()
                self.b=70
                self.jump = True

        elif (event.type,event.key) == (SDL_KEYUP,SDLK_DOWN):
            if self.state in (self.SLIDE,):
                self.state = self.RUN
                self.b = 70
                self.slide = False

        elif (event.type,event.key)==(SDL_KEYUP,SDLK_UP):
            if self.state in (self.JUMP,):
                self.state = self.JUMP
                self.b = 70
                self.slide = False
                self.jump=False

    def update(self,frame_time):
        self.frame = (self.frame+1)%10
        if self.jump == True:
            if self.y<250:
                if self.y>240:
                    self.jump=False
                else:
                    self.y +=30
        else:
            if self.y>90:
                self.y-=30
            else:
                self.state = self.RUN
        if self.slide == True:
            self.state = self.SLIDE

        pass

    def draw(self,frame_time):
        self.image.clip_draw(self.frame * 100, self.state * 150, 94,150, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x-30,self.y-self.b+20,self.x+15,self.y+self.b
