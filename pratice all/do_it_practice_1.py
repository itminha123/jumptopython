
while True:
    print('\nwelcome!! gugu')
    number = input('What do you want to know about the multiplication table?'
                   '\n-1 = end , all = multiplication table')
    if number == '-1' :
        break
    if number == 'all':
        for i in range(2,10):
            for j in range(1,10):
                print('%d*%d=%d'%(i,j,i*j))
        continue
    try:
        number = int(number)
        if number < 0:
            raise ValueError
        for i in range(10):
            result = number * i
            print('%d*%d=%d' % (number, i, result))
    except ValueError:
        print('please Enter the positive number')
