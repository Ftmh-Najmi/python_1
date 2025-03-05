# ورود با پسوورد

users={ 
    'ali':'1234',
    'maryam':'www001',
    'fatemeh':'ftmh2',
    'shayan':'5843432671'
}

enter_username = input('Enter your username:')
enter_password = input('Enter your password:')

while enter_username not in users or users[enter_username]!= enter_password:
    print('Your username or password is wrong')
    enter_username = input('Enter your username:')
    enter_password = input('Enter your password:')

print('You loged in!')
