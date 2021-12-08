def sumsquares(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
        print("sum of first ",n,"natural no. is",sum)
num=int(input("enter the no.:"))
sumsquares(num)
