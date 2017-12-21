# 예로, 10~15까지의 각 숫자 분해하여 곱하기의 전체 합은 다음과 같다.
# 10 = 1 * 0 = 0
# 11 = 1 * 1 = 1
# 12 = 1 * 2 = 2
# 13 = 1 * 3 = 3
# 14 = 1 * 4 = 4
# 15 = 1 * 5 = 5
# 그러므로, 이 경우의 답은 0+1+2+3+4+5 = 15

while True:
    number = input('숫자:').split()
    if len(number) == 2 :
        first = int(number[0])
        second = int(number[1])
        sum = 0
        for i in range(first,second+1):
            result = 1
            for j in str(i):
                result *= int(j)
            sum += result
        print(sum)
    else:
        print('뭐하냐?')