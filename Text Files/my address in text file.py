with open("sample.txt",'w') as f:
    f.write('address is: swaralaya chethukadavu')
    f.close()
f=open("sample.txt",'r')
print(f.readlines())
f.close
