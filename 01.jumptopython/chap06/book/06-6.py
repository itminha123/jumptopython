# def search(dirname):
    # print(dirname)

# search("c:/")

import os

def search(dirname):
    filenames = os.listdir(dirname)

    for filename in filenames:
        full_filename = os.path.join(dirname,filename)
        print(full_filename)

search("C:/")