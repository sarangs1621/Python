def countH():
    f=open("para.txt
           ","r")
    line=0
    l=f.readlines()
    for i in l:
        if i[0]=="h":
            line+=1
    print("no. of lines are:",line)
countH()
