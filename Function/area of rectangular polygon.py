from math import tan,pi
side=int(input("enter the sides no:"))
length=eval(input("enter the length:"))
area=side*(length**2)/(4*tan(pi/side))
print("area is :",area)
               
