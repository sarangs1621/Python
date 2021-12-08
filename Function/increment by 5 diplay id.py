def incrvalue(num):
    print("parameter num has value:",num,"\nid=",id(num))
    num=num+5
    print("num increment by 5 is",num,"\n Now id is",id(num))
number = int(input("enter a number:"))
print("id of argument num is:",id(number))
incrvalue(number)
