import csv
with open('text.csv','a') as file:
    w = csv.writer(file)
    choice='y'
    while choice=='y':
        no=int(input("enter ther employee number:"))
        nm=input("enter the employee name:")
        desig=input("enter the designation:")
        slry=int(input("enter the employee salary:"))
        w.writerow([no,nm,desig,slry])
        print(" Data is saved sucessfully!!!!!" )
        choice=input("is there any more employies?:")
        
        
    
        
