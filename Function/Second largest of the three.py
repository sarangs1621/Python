a,b,c = map(eval, input().split())
if (a >= b) and (a >= c):
    if (b > c):
        second = b
    else:
        second = c
elif (b >= a) and (b >= c):
    if (a > c):
        second = a
    else:
        second = c
elif (c >= a) and (c >=b):
    if (a > b):
        second = a
    else:
        second = b
print("second largest:",second)
