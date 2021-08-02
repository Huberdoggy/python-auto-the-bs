name = input("Enter your name -> ")
age = input("Enter your age -> ")
age = int(age)
if name == 'Kyle' and age == 29:
    print('You must be ' + name + ' because that info is correct.')
elif name != 'Kyle' and age == 29:
    print('You must be someone else.')
elif name != 'Kyle' and age != 29:
    print('So ' + name, ', you\'re ' + str(age))


