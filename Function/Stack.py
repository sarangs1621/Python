Employee=[ ]
c='y'
while (c=="y"):
   print("1. PUSH")
   print("2. POP")
   print("3. DISPLAY")
   choice=int(input("Enter your Choice:"))
   if (choice==1):
      e_id=input("Enter Employee no:")
      ename=input("Enter Employee name:")
      emp=(e_id,ename)
      Employee.append(emp)
   elif (choice==2):
      if(Employee==[ ]):
         print("Stack Empty")
      else:
         e_id,name=Employee.pop()
         print("Deleted element is:",e_id,ename)
   elif (choice==3):
      i=len(Employee)
      while i>0:
         print(Employee[i-1])
         i=i-1
   else:
      print("Wrong Input")
   c=input("Do you want to continue or not?")
               
               
