# create a function named 'collatz' which accepts 1 argument - 'number'
import sys


def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 != 0:
        odd_result = 3 * number + 1
        print(odd_result)
        return odd_result


try:
    value = int(input('Enter a number -> '))
    if value <= 1:
        print('The integer must be a non-negative number AND greater than 1.')
        sys.exit()
    while value > 1:
        value = collatz(value)
except ValueError:
    print('You must enter an integer.')
