# ساخت پسوورد

def passValidation(password):
    if len(password) < 8:
        print('Your password must be at least 8 char')
    elif password.isnumeric():
        print('Your password must have at least one letter')
    elif password.isalpha():
        print('Your password must have at least one number')
    else:
        print('Your password has been successfully registered')
        quit()


while True:
    password = input('Enter your password:')
    passValidation(password)

