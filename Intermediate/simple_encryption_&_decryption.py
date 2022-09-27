while True:
    print("1. for Encryption")
    print("2. for Decryption")
    ch=int(input("enter your choice: "))
    
    if ch==1:
        str=input("enter a string to be encrypted:")
        encrypted_text = ""
        for c in str:
            x = ord(c)
            x = x + 1
            c2 = chr(x)
            encrypted_text = encrypted_text + c2
            print(encrypted_text)

    if ch==2:
        str = input("enter th text to be decrypted:")
        plain_text = ""
        for c in encrypted_text:
            x = ord(c)
            x = x - 1
            c2 = chr(x)
            plain_text = plain_text + c2
            print(plain_text)
