import csv
#writting in csv
with open("a.csv","w")as newfile:
    newfilewriter=csv.writer(newfile)
    newfilewriter.writerow(["user_id","beneficary"])
    newfilewriter.writerow([1621 ,'Sarang S Nair'])
    newfilewriter.writerow([2001 ,'Swathi Sanjay'])
    newfile.close()

#csv file reading code
with open("a.csv","r")as newfile:
    newfilereader=csv.reader(newfile)
    for row in newfilereader:
        print(row)
newfile.close()
