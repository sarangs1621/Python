from itertools import islice
n=int(input("no of lines:"))
#with open ("first.txt") as f::
f=open ("me.txt",'r')
for line in islice(f,n):
    print(line)

    
           
