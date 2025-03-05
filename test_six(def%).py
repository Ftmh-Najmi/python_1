#عدد زوج و فرد

def numberType(number):
    if number % 2 == 0:
        print('This is an even number')
    else:
        print('This is an odd number')

while True:
    number = int(input('Enter a number:'))
    numberType(number)