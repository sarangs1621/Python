import pickle
f=open ("stud.dat","rb")
print("%5s"%"rollnum","%15s"%"name","%5s"%"marks")
while True:
    try:
        rec=pickle.load(f)
        print("%5s"%rec["rollnum"],"%15s"%rec["name"],"%5s"%rec["marks"])
    except EOFError:
        break
f.close()
