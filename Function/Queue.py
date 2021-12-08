a=[ ]
c='y'
while (c=="y"):
   print("1. INSERT")
   print("2. DELETE")
   print("3. DISPLAY")
   choice=int(input("Enter your Choice:"))
   if (choice==1):
      b=input("Enter new number:")
      a.append(b)
   elif (choice==2):
      if(a==[ ]):
         print("Queue Empty")
      else:
         print("Deleted element is:",a[0])
         a.pop(0)
   elif (choice==3):
      l=len(a)
      for i in range(0,l):
         print(a[i])
   else:
      print("Wrong Input")
   c=input("Do you want to continue or not?")
               
               
