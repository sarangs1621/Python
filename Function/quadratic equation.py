from math import sqrt
a=float(input("enter value of a :"))
b=float(input("enter value of b :"))
c=float(input("enter value of c :"))
r=b**2 - 4*a*c
if r>0:
    num_roots=2
    x1=(((-b) + sqrt(r))/(2*a))
    x2=(((-b) - sqrt(r))/(2*a))
    print("the two roots are:",x1)
    print("and",x2)

elif r==0:
    num_roots=1
    x=(-b)/2*a
    print("there is one root:",x)
else:
    num_root=0
    print("no root, discriminant<0")

