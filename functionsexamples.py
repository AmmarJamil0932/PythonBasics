def convert_temperature(temp,unit):
    '''The function comverts temperature between Celsius and Fahrenheit'''
    if unit=='C':
        return temp *(9/5)+32
    elif unit=='F':
        return (temp-32)*5/9
    else:
        return None
    
print(convert_temperature(25,'C'))
print(convert_temperature(77,'F'))


#Password Checker 
def is_strong_password(password):
    '''This function checks if the password is strong or not'''
    if len(password)<8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '!@#$%^&*()_+' for char in password):
        return False
    return True

print(is_strong_password("Wekapassword"))
print(is_strong_password("!AmmarJ3amil"))


