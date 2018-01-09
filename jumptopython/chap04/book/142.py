

def sum(a,b):
    if a < 0 and b <0:
        print("양수만 입력하세요")
        return 0
    return a+b

a= 3
b= 4
c=sum(a,b)
print(c)

a= 1
b= -3
c=sum(a,b)
print(c)
