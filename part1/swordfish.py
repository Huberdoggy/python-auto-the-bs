while True:
    name = input('Enter your name -> ')
    if name != 'Kyle':
        continue
    print('Hola ' + name, 'what\'s the password? (HINT: It\'s a fish...)')
    password = input('-> ')
    if password == 'swordfish':
        break
print('Access granted.')
