
while True:
    number= int(input('숫자:'))
    first = []
    for i in range(1,number+1):
        for j in str(i):
            first.append(j)
    for i in range(10):
        print(i, ':', first.count(str(i)))