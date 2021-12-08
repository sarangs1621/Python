def capitailize_first_letter(str1):                                                #definig a function
        str1 = result = str1.title()                                                  # title() method returns a string where the first character in every word is upper case                  
        result= " "                                                                        # creating a empty string
        for word in str1.split():                                                      #creating a for loop and spliting the str1
                result+= word[ :-1] + word[-1].upper() + "  "           # taking the index of the word and making it into uppercase with uppercase()    
        return result[ :-1]                                                             # returning the resulted string by capitalizing first and last letters into empty string
print(capitailize_first_letter("python string library function"))   # calling the function and printing the string to capitalize its first and last letters
print(capitailize_first_letter("implementation"))            
