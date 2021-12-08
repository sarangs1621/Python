import pickle
f=open("binary.dat","wb")
n=[5,10,15,20,25]
n1=[100,200,300,400,500]
dict1={1:"python",2:"c++"}
pickle.dump(n,f)
pickle.dump(n1,f)
pickle.dump(dict1,f)
f.close()

f=open("binary.dat","rb")
try:
    while True:
        s=pickle.load(f)
        print(s)
except EOFError:
    f.close()
