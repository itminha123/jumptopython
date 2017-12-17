result_sum = 0
first=[]
second=[]
third=[]
while True:
    print('범위, 첫 번째 수, 두 번째 수를 입력하세요.(종료: 프로그램 종료): 예)15 3 5')
    number = input('숫자를 입력하세요:').split()
    if number[0] == '종료':
        break
    if len(number) == 3 :
        a=int(number[0])
        b=int(number[1])
        c=int(number[2])
        for i in range(1,a+1):
            if i % b == 0:
                result= str(i)
                first.append(result)
            if i % c == 0 :
                result= str(i)
                second.append(result)
            if i % b==0 and i % c==0:
                result=str(i)
                third.append(result)
            if i % b==0 or i % c==0 :
                result_sum += i
        print('%d의 배수는 %s 입니다.' % (b,','.join(first)))
        print('%d의 배수는 %s 입니다.' % (c,','.join(second)))
        print('%d와 %d의 공배수는 %s 입니다.' % (b, c,','.join(third)))
        print('따라서 0부터 %d까지의 합은 %d 입니다.'%(a,result_sum))
    else:
        print('다시 입력해주세요.')
