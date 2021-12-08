def UpperLower():
    myfile=open('STORY.TXT','r')
    filecontent=myfile.read()
    uppercount=0
    lowercount=0
    
    for i in filecontent:
        if(i.islower()):
            lowercount=lowercount+1
        if(i.isupper()):
            uppercount=uppercount+1
    print("number of uppercount:",uppercount)
    print("number of lowercount:",lowercount)
UpperLower()

