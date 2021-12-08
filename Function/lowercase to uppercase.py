def swap_case_string(str1):                                       #defining fuction
        str=" "                                                             #adding empty string
        for item in str1:                                                #creating for loop
                if item.isupper():                                       # check whether the item in string is uppercase or lower case
                        str+=item.lower()                             # if  it is in uppercase then it will be converted into lower case with lower()
                else:                                                         # else it will not be changed to lower case
                        str+=item.upper()
        return str                                                         # returning the string 
print(swap_case_string("String Module in"))            #calling the function
print(swap_case_string("python"))                           # inputting the string  to be converted from lowercase to uppercase
print(swap_case_string("Matplot Library"))
