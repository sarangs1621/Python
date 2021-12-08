import pickle
employee=[ ]
f=open("employee.dat","wb")
eno=int(input("enter employeee no:"))
name=input("enter the employee name:")
salary=int(input("enter salary:"))
employee.append([eno,name,salary])
pickle.dump(employee,f)
f.close()
f=open("employee.dat","rb")
print(" _ _ _ _ _ _ _ _ _ _  _ SEARCHING FROM EMPLOYEE DATA_ _ _ _ _ _ _ _ _ _ _ _ _ _ _  ")
en=int(input("enter employee number to be searched:"))
found=False
while True:
    try:
        emp=pickle.load(f)
    except EOFError:
        break
print("%10s" % "EMPLOYEE NO  " , "%10s" % " EMPLOYEE NAME " ," %10s"%"EMPLOYEE SALARY")
print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
for e in employee:
    if (e[0]==en):
        print("%10s"%e[0],"%20s"%e[1],"%10s"%e[2])
        fount=True
        break
    if found==False:
        print("## SORRY EMPLOYEE NUMBER NOT FOUND##")
f.close()
      
