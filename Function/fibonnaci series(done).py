def fibonnaci():
    i=int(input('enter a number:'))
    x=0
    y=1
    z=1
    print("Fibonnaci Series are -->")
    print(x,y,end=" ")
    while z<i:
        print(z,end=" ")
        x=y
        y=z
        z=x+y
fibonnaci()
