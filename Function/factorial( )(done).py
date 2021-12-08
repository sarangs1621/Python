#1 simple meathord 
n=int(input("enter the number:")) #int is used becoz no. are integer
factorial = 1 #giving variable name factorial and value=1
if n<0: #if else statement
    print("does not exist")
elif n==0: #elif is used if more than one option comes
    print("factorial of 0 is 1")
else:
    for i in range(1,n+1): #for loop with range 1(becoze factorial=1) and n is inputed number
        factorial = factorial*i #factorial * i is the retured factorial number
print("The factorial of",n,"is:",factorial) #printing the result

"#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _#"
print() #Just for space
"#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _#"
def fact(n): #defining a variable fact with parameter n
    f=1 #giving variable name factorial and value=1
    for i in range(1,n+1): #for loop
        f=f*i
    return f #returning the factorial

x=int(input("enter the number:")) #input a value
result=fact(x) #function calling and making it a variable name(result)
print(result)#printing the result

