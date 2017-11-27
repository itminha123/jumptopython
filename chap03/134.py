sum=0
for i in range(1,11):
    sum=sum+i

print(sum)

marks=[90,25,67,25,80]
for number in range(len(marks)):
    if marks[number]<60: continue
    print("%d번 학생 축하합니다. 합격입니다."%(number+1))

