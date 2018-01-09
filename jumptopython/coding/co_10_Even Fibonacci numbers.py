# 피보나치 수열의 각 항은 바로 앞의 항 두 개를 더한 것이 됩니다.
# 1과 2로 시작하는 경우 이 수열은 아래와 같습니다.
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# 짝수이면서 4백만 이하인 모든 항을 더하면 얼마가 됩니까?

number = int(input('숫자'))
number_list = list(range(1,number+1))
third=[number_list[0],number_list[1]]
total = 0
for i in range(number):
    first = third[i]
    second = third[i+1]
    if first+second < number:
        third.append(first+second)
    elif first + second >number:
        break
print(third)
for j in third:
    if j % 2 == 0:
        total += j
print(total)







