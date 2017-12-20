# DashInsert 함수는 숫자로 구성된 문자열을 입력받은 뒤,
# 문자열 내에서 홀수가 연속되면 두 수 사이에 - 를 추가하고,
# 짝수가 연속되면 * 를 추가하는 기능을 갖고 있다.
# (예, 454 => 454, 4546793 => 454*67-9-3) DashInsert 함수를 완성하자.
# •입력 - 화면에서 숫자로 된 문자열을 입력받는다.
# "4546793"
# •출력  *, - 가 적절히 추가된 문자열을 화면에 출력한다.
# "454*67-9-3"

input_umber=str(input('숫자:'))
number = list(input_umber)
result=''
for i in range(len(number)):
    if i >0 :
        left = int(number[i-1])
        right = int(number[i])
        if left % 2 == 1 and right % 2 == 1 :
            result += '-'
        elif left % 2 ==0 and right % 2 == 0 :
            result += '*'
    result +=number[i]
print(result)



