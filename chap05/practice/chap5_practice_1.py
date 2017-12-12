

f = open('C:\\Users\\USER\\Downloads\\learning_python.txt','r')
lines = f.read()
result = lines.replace('python','c')
print(result)
f.close()

f = open('C:\\Users\\USER\\Downloads\\learning_python_copyed.txt','w')
f.write(result)
f.close()