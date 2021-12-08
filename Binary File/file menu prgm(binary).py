import pickle
#reading data for dictionary
def insertRec():
    rollno=int(input("enter roll number:"))
    name=input("enter name:")
    marks=int(input("enter the mark:"))
    #creating the dictionary
    rec={"rollno": rollno,"name": name,"marks": marks}
    #writing the dictionary
    f=open("D:/stud.dat","ab")
    pickle.dump(rec,f)
    f.close()

#reading the records from file
def readRec():
    f=open("D:/stud.dat","rb")
    while True:
        try:
            rec=pickle.load(f)
            print("roll num:",rec["rollno"])
            print("name:",re["name"])
            print("marks:",rec["marks"])
        except EOFError:
            break
    f.close()

#searching a record
def searchingRollno(r):
    f=open("D:/stud.dat","rb")
    flag=False
    while True:
        try:
            rec=pickle.load(f)
            if rec["rollno"]==r:
                print("roll num:",rec["rollno"])
                print("name:",re["name"])
                print("marks:",rec["marks"])
                flag=True
        except EOFError:
            break
    if flag == False:
        print("No Records Found")
    f.close()

#updating a binary file
def updateMarks(r,m):
    f=open("D:/stud.dat","rb")
    reclst=[]
    while True:
        try:
            rec=pickle.load(f)
            reclst.append(rec)
        except EOFError:
            break
    f.close()

    for i in range(len(reclst)):
        if reclst[i]["rollno"]==r:
                   reclst[i]["marks"]==m

    f=open("D:/stud.dat","wb")
    for x in reclst:
            pickle.dump(x,f)
    f.close()

#deletion of binary file
def DeleteRec(r):
    f=open("D:/stud.dat","rb")
    reclst=[]
    while True:
        try:
            rec=pickle.load(f)
            reclst.append(rec)
        except EOFError:
            break
    f.close()
    f=open("D:/stud.dat","wb")
    for x in reclst:
        if x["rollno"]==r:
            continue
        pickle.dump(x,f)
    f.close()

while True:
    print("1 insert\n2 display\n3 search\n4 modify\n5 delete\n0 exit")
    ch=int(input("enter choice:"))
    if ch==0:
        break
    elif ch==1:
        insertRec()
    elif ch==2:
        readRec()
    elif ch==3:
        r=int(input("enter roll number to be searched:"))
        searchRollno(r)
    elif ch==4:
         r=int(input("enter roll no:"))
         m=int(input("enter the new mark:"))
         updateMarks(r,m)
    elif ch==5:
        r=int(input("enter roll number to be deleted:"))
        deleteRec()





    


                
