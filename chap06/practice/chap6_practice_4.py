

while True:
    print('\nwelcome!! gugu')
    number = input('What do you want to know about the multiplication table?')
    list = []
    # list_str=str(list)
    for i in range(1,10):
        result = int(number)*i
        list.append(result)
        # print(result,end=' ')
    print(list)

