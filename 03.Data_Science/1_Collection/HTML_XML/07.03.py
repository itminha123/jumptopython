# import  os
#
# os.system("mkdir data1")

# for i in range(1, 30, 3):
#     print(i)

a = ["경기도", "대구광역시", "부산광역시","부산광역시"]

b= ["경기", "부산", "대구"]


result = []
cnt = 0;
for i in b:
    for j in a:
        if i in j:
            cnt += 1
    area_count = [i, cnt]
    result.append(area_count)
    cnt = 0

print(result)
