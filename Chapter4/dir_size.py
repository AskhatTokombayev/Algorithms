import os

def dir_size(path):

    total = os.path.getsize(path)
    list = os.listdir(path)
    for filename in os.listdir(path):
        childpath = os.path.join(path,filename)
        if os.path.isdir(childpath):
            total += dir_size(childpath)
        else:
            filesize = os.path.getsize(childpath)
            total += filesize
            print(str(childpath) + ': '+ str(filesize))
    return total


memory = dir_size('F:\Python\My projects')
print(memory)


