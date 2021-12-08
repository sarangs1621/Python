def mixedfraction(num,deno=1):
    reminder=num%deno
    if reminder!=0:
        quotient=int(num/deno)
        print("the mixed fraction =",quotient,"(",reminder,"/",deno,")")
    else:
        print("the given fraction eveluates to a whole number")
num=int(input("enter a no:"))
deno=int(input("enter a no:"))
print("you entered:",num,"/",deno)
if num>deno:
    mixedfraction(num,deno)
else:
    print("it is proper fraction")
