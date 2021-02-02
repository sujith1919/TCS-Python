#Strings

#Strings can be concatenated with the + operator, and repeated with *:

>>> word = 'Help' + 'A'
>>> word
'HelpA'
>>> '<' + word*5 + '>'
'<HelpAHelpAHelpAHelpAHelpA>'

#string index

>>> word[4]
'A'
>>> word[0:2]
'He'
>>> word[2:4]
'lp'

>>> word[:2]    # The first two characters
'He'
>>> word[2:]    # Everything except the first two characters
'lpA'

#Assigning to an indexed position in the string results in an error:

>>> word[0] = 'x'
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
TypeError: object does not support item assignment
>>> word[:1] = 'Splat'
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
TypeError: object does not support slice assignment

#create new strings with index

>>> 'x' + word[1:]
'xelpA'
>>> 'Splat' + word[4]
'SplatA'

#string math
s[:i] + s[i:] equals s.

>>> word[:2] + word[2:]
'HelpA'
>>> word[:3] + word[3:]
'HelpA'

#Try out these

>>> word[1:100]

>>> word[10:]

>>> word[2:1]




# Answers
>>> word[1:100]
'elpA'
>>> word[10:]
''
>>> word[2:1]
''

# Negative indexes

>>> word[-1]     # The last character
'A'
>>> word[-2]     # The last-but-one character
'p'
>>> word[-2:]    # The last two characters
'pA'
>>> word[:-2]    # Everything except the last two characters
'Hel'


#index representation

  H  e  l  p  A
  0  1  2  3  4 
 -5 -4 -3 -2 -1
 
#finding string length

>>> s = 'vegetables are good for health'
>>> len(s)
30



