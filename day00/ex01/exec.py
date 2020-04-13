# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/13 07:44:10 by anolivei          #+#    #+#              #
#    Updated: 2020/04/13 09:37:28 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
phrase = sys.argv
del phrase[0]
phrase = ' '.join(phrase)
phrase = phrase.swapcase()
print(phrase[::-1])
