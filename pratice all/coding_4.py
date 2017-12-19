

n= input('정수 갯수를 입력하세요.')
integer = input('정수를 입력하세요.').split(' ')
sum= 0
for i in integer:
    sum += int(i)
average=sum/len(integer)
print(sum)
print(average)

del n , integer , sum