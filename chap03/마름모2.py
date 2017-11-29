 output_msg= "홀수를 입력하세요(0 <- 종료): "
blank = " "
star = "*"
print("마름모 출력 프로그램 ver1.0")
print("")

while True:
    print(output_msg, end='')
    customer_input = int(input())
    if customer_input == 0:
        print("")
        print("마름모 프로그램 출력을 이용해 주셔서 감사합니다.")
        break
    elif customer_input % 2 == 0:
        print("짝수를 입력하셨습니다. 재입력 부탁드립니다.")
        continue
    else:
        star_count = 1
        blank_count = int((customer_input - star_count) / 2)
        while True:
            print(blank * blank_count, end='')
            print(star * star_count)
            if star_count == customer_input:
                break
            star_count += 2
            blank_count -= 1
        count = 1
        b = (customer_input - (count * 2))
        blank_count = 1
        while True:
            print(blank * blank_count, end='')
            print(star * b)
            if b == 1:
                break
            b -= 2
            blank_count += 1
