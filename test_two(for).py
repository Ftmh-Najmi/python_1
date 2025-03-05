# دسته بندی با حرف آخر اسم

a=['mohammadi','shafie','mosavi','najmi','mohsenian','mohandesian','asadi']
b=[]

for i in a:
    if i[-1] == 'i':
        b.append(i)

print(b)