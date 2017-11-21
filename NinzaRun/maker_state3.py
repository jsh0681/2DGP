from pico2d import *
import random
import game_framework
import title_state
import pygame
from hero import Hero

grass = None
hero = None
mainBGM = None
background = None
start_time = 0
current_time = 0

global file, object_list


class Object:
    image = None
    def __init__(self):
        self.x = 800
        self.y = 90
        self.arr = []


    def insert(self, char):
        self.arr.append(char)
        if char == 'a':
            if self.image == None:
                self.image = load_image("pipe.png")
        #elif char == 's':
            #if self.image == None:
                #self.image = load_image("pipe.png")
        #elif char == 'd':
            #if self.image == None:
                #self.image = load_image("pipe.png")
        #elif char == 'f':
            #if self.image == None:
                #self.image = load_image("pipe.png")

    def update(self):
        self.x = self.x - 25

    def draw(self):
        #if self.y > 30:
        self.image.draw(self.x, self.y)


class Mainbgm:
    def __init__(self):
        self.bgm = pygame.mixer.Sound('Sounds\\main.wav')

    def playsong(self):
        global start_time # 시작 시간 변수
        self.bgm.set_volume(0.3)
        self.bgm.play()
        start_time = get_time()  # 음악이 처음 재생되는 현재 시각을 저장.

    def pausesong(self):
        self.bgm.stop()


class BackGround:
    PIXEL_PER_METER = (10.0/0.1)
    RUN_SPEED_KMPH = 0.5  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.frame = 640
        self.image = load_image('Graphics\\Stage.png')

    def update(self,frame_time):
        distance = BackGround.RUN_SPEED_PPS*frame_time
        self.frame -= distance

    def draw(self,frame_time):
        self.image.draw(self.frame, 300)


class Grass:
    PIXEL_PER_METER = (10.0/0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH*1000.0/60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS*PIXEL_PER_METER)
    def __init__(self,w,h):
        self.frame=0
        self.left =0
        self.speed = 0
        self.image = load_image('Graphics\\grass.png')
        self.screen_width = w
        self.screen_height = h
    def update(self,frame_time):
        self.speed = Grass.RUN_SPEED_PPS
        self.left = (self.left+frame_time*self.speed)%self.image.w
    def draw(self,frame_time):
        x = int(self.left)
        w = min(self.image.w-x,self.screen_width)
        self.image.clip_draw_to_origin(x,0,w,self.screen_height,0,0)
        self.image.clip_draw_to_origin(0,0,self.screen_width-w,self.screen_height,w,0)


grass_width = 800 # in tiles
grass_height = 70  # in tiles

def enter():
    global hero, grass, background, mainBGM
    mainBGM = Mainbgm()
    mainBGM.playsong()
    hero = Hero()
    grass = Grass(grass_width,grass_height)
    background = BackGround()
    pass

def exit():
    global hero, grass, background, mainBGM
    del(hero,grass,background, mainBGM)
    pass

def resume():
    pass

def pause():
    pass

def handle_events(frame_time):
    global file, start_time, current_time
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_a:
            file = open("data3.txt", 'a') # 파일을 이어서 쓰기 모드로 엶
            current_time = get_time()
            file.write('a ')
            file.write('%f' % (current_time - start_time))
            file.write('\n')
            file.write('e ')
            file.write('%f' % (current_time - start_time))
            file.write('\n')
            print(current_time - start_time)
            file.close()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
            file = open("data3.txt", 'a') # 파일을 이어서 쓰기 모드로 엶
            current_time = get_time()
            file.write('b ')
            file.write('%f' % (current_time - start_time))
            file.write('\n')
            file.write('f ')
            file.write('%f' % (current_time - start_time))
            file.write('\n')
            print(current_time - start_time)
            file.close()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_d:
            file = open("data3.txt", 'a') # 파일을 이어서 쓰기 모드로 엶
            current_time = get_time()
            file.write('c ')
            file.write('%f' % (current_time - start_time))
            file.write('\n')
            file.write('g ')
            file.write('%f' % (current_time - start_time))
            file.write('\n')
            print(current_time - start_time)
            file.close()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_f:
            file = open("data3.txt", 'a') # 파일을 이어서 쓰기 모드로 엶
            current_time = get_time()
            file.write('d ')
            file.write('%f' % (current_time - start_time))
            file.write('\n')
            print(current_time - start_time)
            file.close()
        else:
            hero.handle_events(event,frame_time)
            pass


def get_frame_time():
    global current_time
    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time


def update(frame_time):
    frame_time = get_frame_time()
    hero.update(frame_time)
    background.update(frame_time)
    grass.update(frame_time)

def draw(frame_time):
    global hero,grass,star,background
    clear_canvas()
    background.draw(frame_time)
    grass.draw(frame_time)
    hero.draw(frame_time)
    update_canvas()
    delay(0.05)