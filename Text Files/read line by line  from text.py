# programm to read line by line  from text
'''
f = open('me.txt', 'r')
lines = f.readlines()
 
for line in lines:
    print(line)
 
f.close()

'''
'''
file=open("me.txt","r")

doc=file.readlines()

for i in doc:

   words=i.split()

   for a in words:

       print(a+"#")

file.close()
'''
file=open("me.txt","r")
lines=file.readlines()
for line in lines:
    words=line.split()
    for word in words:
        print(word+'#',end=" ")
    print(" ")
file.close()
