f=open("diary.txt","r")
read=f.readline()
print(read)
f.close()
time=0
time2=0
chk=input("enter a string:")
count=0
for sentence in read:
    line=sentence.split()
    time+=1
    #print(line)
    for each in line:
        line2=each
        time2+=1
        if chk==line2:
            count+=1
print("the search string ",chk,"is present:",count,"times")
print(time)
print(time2)
       
