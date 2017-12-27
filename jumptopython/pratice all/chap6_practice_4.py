

while True:
    print('\nwelcome!! gugu')
    number = int(input('What do you want to know about the multiplication table?'))
    # list = []
    # list_str=str(list)
    try:
        number > 0
        for i in range(1,10):
            result = number*i
            # list.append(result)
            # print(result,end=' ')
            print(result, end=' ')
    except :
        print('please Enter the positive number')

