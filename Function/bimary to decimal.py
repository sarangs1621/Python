import math
b_num=list(input("enter the binary numbr:"))
value=0
for i in range(len(b_num)):
    digit=b_num.pop()
    if digit =='1':
        value=value+math.pow(2,i)
print("the decimal of the number is :",value)
