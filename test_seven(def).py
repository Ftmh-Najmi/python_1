#تبدیل تاریخ

def converter(day, month, year):
    if month>10 or day>10 and month==10:
        birthday = year + 622
    else:
        birthday = year + 621

    print(f'Your year of birthday is {birthday}')


day= int(input('Enter day:'))
month= int(input('Enter month:'))
year= int(input('Enter year:'))

converter(day, month, year)