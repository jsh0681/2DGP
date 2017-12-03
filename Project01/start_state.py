import game_framework
import title_state

from pico2d import *


name = "StartState"
image = None
logo_time = 0.0

#게임에 들어왔을 때 가장 먼저 해야 할 일 1.캔버스를 열고 이미지를 가져옴
def enter():
    global image
    open_canvas()
    image = load_image('Graphics\\kpu_credit.png')
#캔버스를 닫아줌 가져온 이미지를 삭제
def exit():
    global image
    del(image)
    close_canvas()
#이미지가 logotime보다 작을때 계속 업데이트


def update(frame_time):
    global logo_time
    if(logo_time>1.0):
        logo_time = 0
        game_framework.push_state(title_state)
    delay(0.01)
    logo_time+= 0.01

def draw(frame_time):
    global image
    clear_canvas()
    image.draw(400,300)
    update_canvas()

def handle_events(frame_time):
    pass


def pause(): pass


def resume(): pass




