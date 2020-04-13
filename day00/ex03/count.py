# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/13 11:01:02 by anolivei          #+#    #+#              #
#    Updated: 2020/04/13 14:17:33 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import string

def text_analyzer(text = None):
    if text is None:
        text = input("Please prompt a text to analyze\n")
        upper = sum(c.isupper() for c in text)
        lower = sum(c.islower() for c in text)
        punct = sum((c in string.punctuation) for c in text)
        space = sum(c.isspace() for c in text)

    print(f"The text contains {len(text)} characters:\n\n"
            f"- {upper} upper letters\n\n"
            f"- {lower} lower letters\n\n"
            f"- {punct} punctuation marks\n\n"
            f"- {space} spaces")

if __name__ == '__main__':
    text_analyzer()
