def vowel_replace(str1):
        str= " "
        for letter in str1:
                if letter in ('a','e','i','o','u','A','E','I','O','U'):
                        str += " * "
                else:
                        str+=letter
        return str
str1=input("Enter the String:")
str2=vowel_replace(str1)
print("String with Vowels is:",str1)
print("String without Vowels is:",str2)





# program using replace fuction ( .replace() )
def vowel_removal( ):
        s = input("Enter any string to remove all vowels from it: ")
        vowels = ('a','e','i','o','u','A','E','I','O','U')
        for x in s:
                if x in vowels:
                        s = s.replace(x, " * ")
        print(s)
vowel_removal( )


