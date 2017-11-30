


while True:
    multiples=int(input("7과 9의 공배수"))
    if multiples == 0:
        break
    else:
        for i in range(10000):
            if i % 7 == 0 and i % 9 == 0:
                print(i)








