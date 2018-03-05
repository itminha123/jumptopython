
import csv

with open("C:\\Users\\USER\\Downloads\\Demographic_Statistics_By_Zip_Code.csv",newline='') as infile:
    data = list(csv.reader(infile))

countparticipantsindex= data[0].index("COUNT PARTICIPANTS")
print("The index of 'COUNT PARTICIPANTS': "+ str(countparticipantsindex))

countparticipants=[]

for cloumn in data[1:]:
    countparticipants.append(int(cloumn[countparticipantsindex]))

print(countparticipants)