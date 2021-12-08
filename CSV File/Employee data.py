import csv
with open('myfile.csv',mode='a') as csvfile:
    mywriter = csv.writer(csvfile, delimiter = ',')
    ans='y'
    while ans.lower()=='y':
        eno=int(input("enter ther employ number:"))
        name=input("enter ther employ name:")
        salary=int(input("enter ther employ salary:"))
        mywriter.writerow([eno,name,salary])
        print(" data saved" )
        ans=input("add more?:")
        
    
        
