


number = input('뭐가 궁금해?')

result = number[0]  # 첫번째 값을 결과에 넣는다
count  = 0

for st in number:
    if st == result[-1]:
        count += 1
    else:
        result += str(count) + st
        count = 1
result += str(count)

print(result)
