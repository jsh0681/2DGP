import os
#소스코드임과 동시에 모듈임과 동시에 다른 모듈에서도 import 가능함
#tools 밑어 파이썬 콘솔
#view 밑에 파이썬 콘솔을 하면
#아래에 idle이뜸
#view 밑에 toolswindow 밑에 terminal을 쓰면 커멘드 창이열림
file_name_list = os.listdir()
for name in file_name_list:
    print(name)
