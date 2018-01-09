

while True:
    result = []
    numbers = input('숫자 입력해!!')
    for i in numbers:
        if i not in result:
            result.append(i)
            continue
    if len(result) == 10 :
        print('true')
    else:
        print('false')


