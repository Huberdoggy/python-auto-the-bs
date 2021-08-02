import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    elif response != 'exit':
        print('Not what I\'m looking for...')
        continue
    print('You typed ' + response + '.')


# PRACTICE Stuff...

# for i in range(1, 11):
#     print(i)
# i = 1
# while i <= 10:
#     print(str(i) + ' ', end='')
#     i = i + 1
