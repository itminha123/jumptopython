# 프로그램 실행 순서
# 1.입력할 정수의 개수를 사용자로부터 입력 받는다.
# 2.입력받은 정수의 개수만큼 정수를 입력받는다.
# 3.입력받은 정수의 합과 평균 값을 출력한다.
# 4.할당된 메모리공간을 비운다.
# 요구사항
# 1.메모리공간은 사용자의 입력 수의 따라 변동된다.
# 2.사용한 공간은 마지막에 비워야 한다.
# 3.배열을 사용하면 안된다.

n= input('정수 갯수를 입력하세요.')
integer = input('정수를 입력하세요.').split(' ')
sum= 0
for i in integer:
    sum += int(i)
average=sum/len(integer)
print(sum)
print(average)

del n , integer , sum