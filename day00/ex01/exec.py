import sys
phrase = sys.argv
del phrase[0]
phrase = ' '.join(phrase)
phrase = phrase.swapcase()
print(phrase[::-1])
