# 디지털 시계에 하루동안(00:00~23:59) 3이 표시되는 시간을 초로 환산하면 총 몇 초(second) 일까요?
# 디지털 시계는 하루동안 다음과 같이 시:분(00:00~23:59)으로 표시됩니다.
# 00:00 (60초간 표시됨)
# 00:01
# 00:02
# ...
# 23:59

sumSec=0    # 초의 총합을 저장할 변수
for hour in range(24) :     # 시간
    for minute in range(60) :   #분
        if '3' in str(hour) or '3' in str(minute) : # 시간이나 분에 3이 들어가면
            sumSec += 60            # 60초씩 더함
print(sumSec)
