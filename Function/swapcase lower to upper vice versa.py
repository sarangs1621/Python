def swap_case_string(str1):
    result=" "
    for item in str1:
        if item.isupper():
            result+=item.lower()
        else:
            result+=item.upper()
    return result
print(swap_case_string('StInG Is VeRy GoOd'))
