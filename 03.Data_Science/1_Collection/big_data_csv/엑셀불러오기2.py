import csv

with open("C:\\Users\\USER\\Downloads\\Demographic_Statistics_By_Zip_Code.csv",newline='') as infile:
    data = list(csv.reader(infile))

countfemaleindex = data[0].index("COUNT FEMALE")
print("The index of 'COUNT FEMALE'" + str(countfemaleindex))

countfemale = []
for cloumn in data[1:]:
    countfemale.append(int(cloumn[countfemaleindex]))

print(countfemale)

for i in countfemale:
    print(i)

# countcitizenstatustotalindex=data[0].index("COUNT CITIZEN STATUS TOTAL")
# print("The index of 'COUNT CITIZEN STATUS TOTAL'"+str(countcitizenstatustotalindex))

# countcitizenstatustotal=[]

# for cloumn in data[1:]:
#     countcitizenstatustotal.append(int(cloumn[countcitizenstatustotalindex]))
#
# print(countcitizenstatustotal)
#
# for i in countcitizenstatustotal:
#     print(i,end=' ')