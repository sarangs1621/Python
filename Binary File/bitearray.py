f=open('filebin.dat','wb')
n=[5,10,15,20,25]
a=bytearray (n)
f.write(a)
f.close()
f=open('filebin.dat','rb')
n=list(f.read())
print(n)
f.close()
