import math
def arclen():
    dia =float(input("enter the dia:"))
    angle=float(input("enter the angle:"))
    if angle>=360:
        print("angle not possible:")
        return
    else:
        arc_len=(math.pi*dia)*(angle/360)
        print("arc length is:",arc_len)
arclen()
    
