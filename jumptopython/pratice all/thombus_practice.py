blank = ' '
star = '*'
while True:
    try:
        number = int(input('Please enter the number'))
        if number % 2 == 0:
            print('Hey!! Enter the odd number')
            continue
        elif number % 2 == 1:
            star_count = 1
            blank_count = int((number - 1) / 2)
            while True:
                print(blank * blank_count, end='')
                print(star * star_count)
                if star_count == number:
                    break
                star_count += 2
                blank_count -= 1
    except:
        print('Keep it straight.')


