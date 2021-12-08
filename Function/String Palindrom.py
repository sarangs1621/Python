def palindrome():
   x =input("enter a string:")
   if(x==x[::-1]):
      print("Yes, it is palindrome")
   else:
      print("No, it is not Palindrome")
palindrome()
