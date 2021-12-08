f=open("para.txt","r")
read=f.readlines()
f.close()
id=[]
for ln in read:
    if ln.startswith("t"):
        id.append(ln)
print(id)
