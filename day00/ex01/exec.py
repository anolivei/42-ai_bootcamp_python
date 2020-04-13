# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/13 07:44:10 by anolivei          #+#    #+#              #
#    Updated: 2020/04/13 09:03:04 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def function():
	phrase = sys.argv
	del phrase[0]
	phrase = ' '.join(phrase)
	phrase = phrase.swapcase()
	print(phrase[::-1])

if __name__ == '__main__':
    function()
