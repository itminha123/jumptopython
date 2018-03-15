
S = "aaabbcccccca"
count = 1
blank_list = []

for i in range(len(S) - 1):
    if S[i] == S[i + 1]:
        count += 1
    elif S[i] != S[i + 1]:
        blank_list.append((count, S[i]))
        count = 1
    if i == len(S) - 2:
        blank_list.append((count, S[i + 1]))

answer = ""

for i in range(len(blank_list)):
    answer = answer + str(blank_list[i][1]) + str(blank_list[i][0])

print(answer)