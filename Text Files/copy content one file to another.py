#programm to copy the content from one file to another

f=open("me.txt")  
f1=open("output.txt","a")
for x in f.readlines():
    f1.write(x)
f.close()
f1.close()




