
list = [-1, 1, 3, -2, 2]

alist  = []
blist  = []

for n in list:
    if n < 0:
        alist.append(n)
    else:
        blist.append(n)

print(alist + blist)




