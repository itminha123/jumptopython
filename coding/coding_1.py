# 예로 10 ~ 15 까지의 각 숫자의 개수를 구해보자
# 10 = 1, 0
# 11 = 1, 1
# 12 = 1, 2
# 13 = 1, 3
# 14 = 1, 4
# 15 = 1, 5
# 그러므로 이 경우의 답은 0:1개, 1:7개, 2:1개, 3:1개, 4:1개, 5:1개

while True:
    try:
        number = int(input('숫자:'))
        first = []
        for i in range(1, number + 1):
            for j in str(i):
                first.append(j)
        for i in range(10):
            print(i, ':', first.count(str(i)))
    except:
        print('똑바로 해라잉!!!')

