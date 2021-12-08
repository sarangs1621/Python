VALUES=[]
n=int(input('enter total no:'))
i=0
while i<n:
    x=int(input('enter a number:'))
    VALUES.append(x)
    i=i+1
print("The List is:",VALUES)

def AddOddEven(VALUES):
    so=0
    se=0
    for i in VALUES:
        if i%2==0:
            se=se+i
        else:
            so=so+i
    print("Sum of Even:",se)
    print("Sum of Odd:",so)
AddOddEven(VALUES)
        
        
