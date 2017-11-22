import game_framework
from pico2d import *
import main_state
import pygame
import title_state
pygame.mixer.init()#초기화

name = "TitleState"
image = None
def playsong():
    pygame.mixer.music.load('Sounds\\main.wav')
    pygame.mixer.music.play()

def enter():
    global image
    playsong()
    image = load_image('Graphics\\gameover.png')

def exit():
    global image
    del(image)


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type , event.key) ==(SDL_KEYDOWN , SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type , event.key)==(SDL_KEYDOWN , SDLK_SPACE):
                pygame.mixer.music.pause()
                game_framework.change_state(title_state)
def draw(frame_time):
    clear_canvas()
    image.draw(400,300)
    update_canvas()

def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass






