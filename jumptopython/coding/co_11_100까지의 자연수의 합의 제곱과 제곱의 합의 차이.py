# 안녕하세요. '프로젝트 오일러'에서 문제를 가져왔습니다.
# 1부터 10까지 자연수를 각각 제곱해 더하면 다음과 같습니다
# (제곱의 합). 1^2 + 2^2 + ... + 10^2 = 385
# 1부터 10을 먼저 더한 다음에 그 결과를 제곱하면 다음과 같습니다
# (합의 제곱). (1 + 2 + ... + 10)^2 = 55^2 = 3025
# 따라서 1부터 10까지 자연수에 대해 "합의 제곱"과 "제곱의 합" 의 차이는
# 3025 - 385 = 2640 이 됩니다.
# 그러면 1부터 100까지 자연수에 대해 "합의 제곱"과 "제곱의 합"의 차이는 얼마입니까?
number = int(input('숫자:'))
square_sum = 0
total_sum = 0
for i in range(1,number+1):
    square_sum += i**2
    total_sum += i

print(total_sum)
print(square_sum)
print((total_sum*total_sum)-square_sum)