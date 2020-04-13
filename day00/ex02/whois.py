# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/13 09:52:01 by anolivei          #+#    #+#              #
#    Updated: 2020/04/13 10:50:30 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def function():
    if (len(sys.argv) != 2 or not sys.argv[1].isdigit()):
        print("ERROR")
        return (0)
    n = int(sys.argv[1])
    if (n == 0):
        print("I'm Zero.")
        return (0)
    if (n % 2 == 0):
        print("I'm Even.")
        return (0)
    else:
        print("I'm Odd.")
        return (0)

if __name__ == '__main__':
    function()
