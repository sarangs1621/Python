fp= open("me.txt")
line = fp.readline()
cnt = 1
while line:
    print("Line {}: {}".format(cnt, line.strip()))
    line = fp.readline()
    cnt += 1


# programm to read line by line
f = open ("me.txt", "r")
while True:
    line = f.readline()
    if not line :
        break
    print(line.strip())
f.close()   
