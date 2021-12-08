def count():
    f=open("me.txt")
    count=0
    for line in f:
        words=line.split()
        for w in words:
            if w =="this" or w=="that":
                count+=1
    print("no of times  word occured:",count)
count()
            
