# 2진법이란, 어떤 자연수를 0과 1로만 나타내는 것이다.
#  예를 들어 73은 64(2^6)+8(2^3)+1(2^0)이기 때문에
# 1001001으로 표현한다. 어떤 숫자를 입력받았을 때
#  그 숫자를 2진법으로 출력하는 프로그램을 작성하시오.


number = int(input('숫자:'))
result =[]
while number:
    result.append(number%2)
    number = int(number/2)
# result=list(map(str,result))
result= list(str(i) for i in result)
result.reverse()

print(''.join(result))