# 다음 입사문제 중에서
# 1차원의 점들이 주어졌을 때, 그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하시오.
# (단 점들의 배열은 모두 정렬되어있다고 가정한다.)

import random
while True:
    try:
        number = int(input('숫자:'))
        # points = list({1, 3, 5, 8, 9, 13, 17, 20})
        points = list(set(list(random.randint(1, 100) for i in range(number))))
        points.sort()
        print("수직선 위 점들은 ", points)

        # 최소 거리의 점쌍을 모음
        distances = [[points[0], points[1], points[1] - points[0]]]
        for p1 in range(1, len(points) - 1):
            left = points[p1]
            right = points[p1 + 1]
            distance = right - left
            if distances[0][2] > distance:
                distances = [[left, right, distance]]
            elif distances[0][2] == distance:
                distances += [[left, right, distance]]

        print("가장 짧은 거리는", distances[0][2], ": ", end='')

        for i in range(len(distances)):
            if i == len(distances) - 1:
                print(distances[i][0], "~", distances[i][1])
            else:
                print(distances[i][0], "~", distances[i][1], end=', ')
    except:
        print('하하하하하')



