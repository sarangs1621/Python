def uppercase():
    f=open('me.txt')
    count=0
    for line in f:
        if line[0].isupper():
            count+=1
    print("there are",count,"letters starting with Capitals")
uppercase()
