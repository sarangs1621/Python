
import csv
while True:
   print("1. for WRITING INTO THE FILE")
   print("2. for READING FROM THE FILE")
   ch=int(input("enter your choice: "))
   if ch==1:
       with open('student.csv','a') as file:
           w = csv.writer(file)
           choice='y'
           while choice=='y':
               rollno=int(input("enter roll number:"))
               name=input("enter name:")
               stream=input("enter the stream:")
               marks=eval(input("enter the mark:"))
               w.writerow([rollno,name,stream,marks])
               choice=input("is there any more students?:")
   elif ch==2:
      with open("student.csv","r")as newfile:
         newfilereader=csv.reader(newfile)
         for row in newfilereader:
            print(row)
         newfile.close()
   else:
      print("invalid value")




      
        
