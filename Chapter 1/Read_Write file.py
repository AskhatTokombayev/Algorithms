fp = open("ReadWriteExample.txt","w")
fp.write("This writes a .txt file\n")
fp.write("This is the last line in this .txt file\n")
fp.close()

fp = open("ReadWriteExample.txt","r")
Z = fp.read(20)

print(Z)