# -*- coding: utf-8 -*-       # <= 추가
# // 네이버 음성합성 Open API 예제 # <= 주석으로 변경 또는 제거
import os
import sys
import urllib.request
import wave
import pygame
import winsound
from pygame import mixer
# import mp3play
import time


client_id = "CJsADWzyJq8m29Qm7l11"           # <= 변경
client_secret = "cv55RE05hD" # <= 변경
encText = urllib.parse.quote("안녕하세요. 전민하입니다. 스마트홈네트워크를 구동시키겠습니다. 오늘의 뉴스를 알려드리겠습니다. 홍준표 대표는 류여해의원의 성추행 고소관련하여 말도 안된다며 MBN뉴스와 싸우고 있습니다. 재미있어요? 그럼 안녕!")
data = "speaker=mijin&speed=0&text=" + encText;
url = "https://openapi.naver.com/v1/voice/tts.bin"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode('utf-8'))
rescode = response.getcode()
if(rescode==200):
    print("TTS mp3 저장")
    response_body = response.read()
    with open('11112.mp3', 'wb') as f:
        f.write(response_body)

else:
    print("Error Code:" + rescode)


# pygame.mixer.init()
# s = pygame.mixer.Sound("11112.mp3")
# s.play()
# mixer.init()
# pygame.mixer.music.load('11112.mp3')
# pygame.mixer.music.play()
# time.sleep(pygame.time)
# time.sleep(20)
# while True:
# pygame.mixer.music.stop()

# winsound.PlaySound("11112.mp3",winsound.SND_FILENAME)

# import pyglet
#
# music = pyglet.resource.media('music.mp3')
# music.play()
#
# pyglet.app.run()

# import os
# os.system("start 11112.mp3")
# os.system()

# clip = mp3play.load("11112.mp3")
# clip.play()
#
# time.sleep(min(30, clip.seconds()))
# clip.stop()