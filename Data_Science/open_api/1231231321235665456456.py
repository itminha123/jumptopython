# -*- coding: utf-8 -*-       # <= 추가
# // 네이버 음성합성 Open API 예제 # <= 주석으로 변경 또는 제거
import os
import sys
import urllib.request
client_id = "QuStly4CvlpyMUh0H5rj"           # <= 변경
client_secret = "leuZfZihj3" # <= 변경
encText = urllib.parse.quote("반갑습니다 네이버")
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
    with open('1111.mp3', 'wb') as f:
        f.write(response_body)
else:
    print("Error Code:" + rescode)
