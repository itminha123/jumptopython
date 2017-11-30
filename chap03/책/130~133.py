test_list=['one','two','three']
for i in test_list:
    print(i)

a=[(1,2),(3,4),(5,6)]
for (frist,last)in a:
    print(frist+last)

marks=[90,25,67,45,80]
number=0
for mark in marks:
    number=number+1
    if mark>=60:
        print("%d번 학생은 합격입니다."%number)
    else:
        print("%d번 학생은 불합격입니다."%number)

marks=[90,25,67,45,80]
number=0
for mark in marks:
    number=number+1
    if mark < 60: continue
    print("%d번 학생 축하합니다. 합격입니다."%number)

range(0,10)
