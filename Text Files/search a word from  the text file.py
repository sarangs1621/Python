# prgramm to search a word from  the text file

f = open("me.txt","r")
word=input("enter the word to be search: ")
s=" "
count=1
L=f.readlines()
for i in L:
    L2=i.split()
    if word in L2:
        print("line number",count,":",i)
    count+=1
