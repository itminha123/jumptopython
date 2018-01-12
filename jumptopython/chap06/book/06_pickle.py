import pickle
f = open("test.txt",'wb')
data = {1:'python', 2:'you need'}
pickle.dump(data, f)
f.close()