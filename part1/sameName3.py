def spam():
    global eggs
    eggs = 'spam' # this is global

def bacon():
    eggs = 'bacon' # this is a loc

def ham():
    print(eggs) # reference to the global

eggs = 42 # this is global
spam()
print(eggs)