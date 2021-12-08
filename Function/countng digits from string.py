str=input("enter the string: ")
sum_digit = 0
num=0
for x in str:
    if x.isdigit() == True:
        z = int(x)
        num=num*10+ z
        sum_digit = sum_digit + z
print("the Sum of Digits is:",sum_digit)
print("Original String is:",str)
print("Digits are:",num)

if x.isdigit()==False:
    print("Original String :",str,", Has No Digit!!!!!")
