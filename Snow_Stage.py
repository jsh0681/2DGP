from pico2d import *
import game_framework
import title_state
import pygame
from Main_Character import Ninja
from Snow_Star import Star
import maker_state3
import gameover_state
grass = None
ninja = None
mainBGM = None
star = None
background = None
start_time = 0
current_time = 0
index = 0
length = 0
TimeInUpdate =0
ScoreDown=0.3
k=0
object_list = None
global file
pygame.mixer.init()

class Ui:
    def __init__(self):
        self.score = 500
        self.font = load_font('font.ttf', 30)
        self.time = 0.0

    def update(self, frame_time):
        self.time = get_time() - start_time

    def draw(self,frame_time):
        print('score %d time %f' % (self.score, self.time))
        self.font.draw(550, 550, 'SCORE %d' % (self.score))


class Object:
    image = None
    def __init__(self):
        self.x = 900
        self.y = 80
        self.a = 0
        self.b = 0
        self.arr = []
        self.state = 0
        self.state = 1
        self.bgm = pygame.mixer.Sound('Sounds\\pipe.wav')
    def playsong(self):
        self.bgm.set_volume(0.7)
        self.bgm.play()

    def insert(self, char, time):
        self.arr.append([char, time])
        if char == 'a':
            if self.image == None:
                self.image = load_image("Graphics\\ssnowman.png")
                self.a = 25
                self.b = 20
                self.state = 0
        elif char == 'e':
            if self.image == None:
                self.image = load_image("Graphics\\snowstar.png")
                self.a = 15
                self.b = 15
                self.y = 155
                self.state = 1

        elif char == 'b':
            if self.image == None:
                self.image = load_image("Graphics\\snowman.png")
                self.a =20
                self.b =40
                self.state = 0
        elif char == 'f':
            if self.image == None:
                self.image = load_image("Graphics\\snowstar.png")
                self.a = 15
                self.b = 15
                self.y = 170
                self.state = 1

        elif char == 'c':
            if self.image == None:
                self.image = load_image("Graphics\\snowball.png")
                self.a =40
                self.b =40
                self.state = 0
        elif char == 'g':
            if self.image == None:
                self.image = load_image("Graphics\\snowstar.png")
                self.a = 15
                self.b = 15
                self.y = 180
                self.state = 1
        elif char == 'd':
            if self.image == None:
                self.image = load_image("Graphics\\icicle.png")
                self.y = 380
                self.a = 1
                self.b = 225
                self.state = 0

    def update(self, frame_time):
        self.x = self.x - 25

    def draw(self, frame_time):
        self.image.draw(self.x, self.y)
        #draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - self.a, self.y - self.b, self.x + self.a, self.y + self.b


class Mainbgm:
    def __init__(self):
        self.bgm = pygame.mixer.Sound('Sounds\\Snow_stage.wav')

    def playsong(self):
        global start_time # 시작 시간 변수
        self.bgm.set_volume(0.3)
        self.bgm.play()
        start_time = get_time()  # 음악이 처음 재생되는 현재 시각을 저장.

    def pausesong(self):
        self.bgm.stop()


class BackGround:
    PIXEL_PER_METER = (10.0/0.3)
    RUN_SPEED_KMPH = 2.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH*1000.0/60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS*PIXEL_PER_METER)
    def __init__(self,w,h):
        self.frame=0
        self.left =0
        self.speed = 0
        self.image = load_image('Graphics\\snowback.png')
        self.screen_width = w
        self.screen_height = h
    def update(self,frame_time):
        self.speed = background.RUN_SPEED_PPS
        self.left = (self.left+frame_time*self.speed)%self.image.w
    def draw(self,frame_time):
        x = int(self.left)
        w = min(self.image.w-x,self.screen_width)
        self.image.clip_draw_to_origin(x,0,w,self.screen_height,0,0)
        self.image.clip_draw_to_origin(0,0,self.screen_width-w,self.screen_height,w,0)

background_width = 1067 # in tiles
background_height = 600 # in tiles

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
        self.image = load_image('Graphics\\snow.png')
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
grass_height = 60  # in tiles


def LengthOfFile():
    global length, line
    file = open("data3.txt", 'r')
    length = 0
    line = None
    while True:
        line = file.readline()
        if not line:
            break
        length = length + 1
    file.close()
    return length


def enter():
    global ninja, grass, background, mainBGM, file, object_list, index, line, ui,star
    file = open("data3.txt", 'r')  # 파일을 읽기 모드로 엶
    object_list = [Object() for i in range(LengthOfFile())]
    line = None
    index = 0
    while True:
        line = file.readline() #한 줄씩 읽는다
        if not line: break
        object_list[index].insert(line[0], float(line[2:]))
        index = index + 1
    file.close()
    star = [Star()]
    mainBGM = Mainbgm()
    mainBGM.playsong()
    ninja = Ninja()
    grass = Grass(grass_width,grass_height)
    background = BackGround(background_width,background_height)
    ui = Ui()
    pass

def exit():
    global ninja, grass, background, mainBGM,star
    del(ninja,grass,background, mainBGM,star)
    pass

def resume():
    pass

def pause():
    pass

def handle_events(frame_time):
    global file, start_time, current_time,ninja, mainBGM
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif ui.score<=0:
            mainBGM.pausesong()
            game_framework.change_state(gameover_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key  == SDLK_END:
            mainBGM.pausesong()
            game_framework.change_state(maker_state3)
        else:
            ninja.handle_events(event,frame_time)
            pass


def get_frame_time():
    global current_time
    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def update(frame_time):
    global object_list, ui, ninja,star,k,TimeInUpdate ,ScoreDown
    frame_time = get_frame_time()
    if k >= 5:
        star.append(Star())
        k = 0

    ninja.update(frame_time)
    background.update(frame_time)
    grass.update(frame_time)
    ui.update(frame_time)
    for stars in star:
        stars.update(frame_time)

    for i in range(len(object_list)):
        if (object_list[i].arr[0][1] - 1 <= float(ui.time)):
            object_list[i].update(frame_time)

    for object in object_list:
        if collide(object, ninja):
            if object.state == 0:
                object.playsong()
                object_list.remove(object)
                ui.score -=40
            elif object.state == 1:
                object_list.remove(object)
                ui.score +=30

    for stars in star:
        if collide(ninja, stars):
            stars.playsong()
            ui.score += 25
            star.remove(stars)

    for object in object_list:
        for stars in star:
            if collide(object,stars):
                star.remove(stars)

    ui.score -= 3
    if TimeInUpdate>=100:
        ScoreDown+=0.3
        TimeInUpdate=0

    ui.score -= ScoreDown
    TimeInUpdate +=0.5
    k += 1
def draw(frame_time):
    global ninja,grass,star,background, object_list,ui
    handle_events(frame_time)
    clear_canvas()
    background.draw(frame_time)
    grass.draw(frame_time)
    for stars in star:
        stars.draw(frame_time)
    for i in range(len(object_list)):
        object_list[i].draw(frame_time)
    ui.draw(frame_time)
    ninja.draw(frame_time)
    update_canvas()
    delay(0.05)