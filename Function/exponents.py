def calcpow(number,power):
    result=1
    for i in range(1,power+1):
        result=result*number
        return result
base=int(input("enter a no.:"))
expo=int(input("enter a no.:"))
answer=calcpow(base,expo)
print(base,"raised to power",expo,"is",answer)

        
    
