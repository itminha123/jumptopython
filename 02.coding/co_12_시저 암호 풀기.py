# 시저 암호는, 고대 로마의 황제 줄리어스 시저가 만들어 낸 암호인데,
# 예를 들어 알파벳 A를 입력했을 때, 그 알파벳의 n개 뒤에 오는
# (여기서는 예를 들 때 3으로 지정하였다)알파벳이 출력되는 것이다.
# 예를 들어 바꾸려는 단어가 'CAT"고, n을 5로 지정하였을 때 "HFY"가 되는 것이다.
# 어떠한 암호를 만들 문장과 n을 입력했을 때 암호를 만들어 출력하는 프로그램을 작성해라.


result_list = ["A","B","C","D","E","F","G","H","I","J","K","L","N","M",
               "O","P","Q","R","S","T", "U","V","W","X","Y","Z"]

secret_text = input("암호 문장을 입력하세요: ")
secret_count = int(input("숫자를 입력하세요: "))
# print(secret_text[0])
result = ""
for i in range(len(secret_text)):
    for j in range(len(result_list)):
        if secret_text[i] == result_list[j]:
            if j+secret_count > len(result_list):
                over_index = (j + secret_count) % len(result_list)
                result += result_list[over_index]
            else:
                result += result_list[j+secret_count]


print(result)
