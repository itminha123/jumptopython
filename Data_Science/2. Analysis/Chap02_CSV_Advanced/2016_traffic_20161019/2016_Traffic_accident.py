#2016년 교통사고 유형별 자료를 모아 한파일에 나타냄.
import pandas as pd
import sys
import glob
import os

input_path = sys.argv[1]

all_files = glob.glob(os.path.join(input_path, '2016년_사고유형별_*'))
all_file_list = []
first_file = True
for file in all_files:
    print(os.path.basename(file))
    data_frame = pd.read_csv(file, engine='python') #한글 파일 읽을때 오류남 (engine ='python')으로 해결
    if first_file: #동일된 프라이머리키를 한번 출력하기 위해
        all_file_list.append(data_frame)
        first_file = False
        continue
    data_frame_add = data_frame.ix[:,2:] #프라이머리키가 같아서 처리함
    all_file_list.append(data_frame_add)

data_frame_concat = pd.concat(all_file_list, axis=1, ignore_index=False)
data_frame_concat.to_csv("2016년_사고유형별통계.csv", encoding='cp949', index=False) # encoding= 'cp949' 없다면 한글 쓸때 오류남