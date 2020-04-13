# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/13 14:26:20 by anolivei          #+#    #+#              #
#    Updated: 2020/04/13 15:22:43 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def sum(a, b):
    a = int(a)
    b = int(b)
    return a + b

def dif(a, b):
    a = int(a)
    b = int(b)
    return a - b

def pro(a, b):
    a = int(a)
    b = int(b)
    return a * b

def quo(a, b):
    a = int(a)
    b = int(b)
    if b == 0:
        return "ERROR (div by zero)"
    return a / b

def rem(a, b):
    a = int(a)
    b = int(b)
    if b == 0:
        return "ERROR (modulo by zero)"
    return a % b

def operation(arg):
    if len(arg) == 0:
        print("Usage: python operations.py <number1> <number2>\n"
        "Example:\n"
        "\tpython operations.py 10 3")
        return 0
    elif len(arg) > 2:
        print("InputError: too many arguments\n\n"
        "Usage: python operations.py <number1> <number2>\n"
        "Example:\n"
        "\tpython operations.py 10 3")
        return 0
    elif not arg[0].isnumeric() or not arg[1].isnumeric():
        print("InputError: only numbers\n\n"
        "Usage: python operations.py <number1> <number2>\n"
        "Example:\n"
        "\tpython operations.py 10 3\n")
        return 0
    print(f'Sum:\t\t {sum(arg[0],arg[1])}')
    print(f'Difference:\t {dif(arg[0],arg[1])}')
    print(f'Product:\t {pro(arg[0],arg[1])}')
    print(f'Quotient:\t {quo(arg[0],arg[1])}')
    print(f'Remainder:\t {rem(arg[0],arg[1])}')

if __name__ == '__main__':
    operation(sys.argv[1:])
