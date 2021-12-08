str1=input("enter a string:")
vowels="a,e,i,o,u,A,E,I,O,U"
count=0
for letter in str1:
        if letter in ('a','e','i','o','u'):
         count=count+1
print("no. of vowels in string is:",count)
