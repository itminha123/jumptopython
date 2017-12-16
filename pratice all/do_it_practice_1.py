
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
        for i in range(1,10):
            print('%d*%d=%d' % (number, i, i*number))
    except ValueError:
        print('Please Enter the positive number')
    except:
        print('Please Enter the number')