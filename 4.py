#Strings

#Besides numbers, Python can also manipulate strings,
#which can be expressed in several ways.
#They can be enclosed in single quotes or double quotes:

>>> 'spam eggs'
'spam eggs'
>>> 'doesn\'t'
"doesn't"
>>> "doesn't"
"doesn't"
>>> '"Yes," he said.'
'"Yes," he said.'
>>> "\"Yes,\" he said."
'"Yes," he said.'
>>> '"Isn\'t," she said.'
'"Isn\'t," she said.'

#String literals can span multiple lines in several ways.
#Continuation lines can be used, with a backslash as the last character
#on the line indicating that the next line is a logical continuation of the line:


hello = "This is a rather long string containing\n\
several lines of text just as you would do in C.\n\
    Note that whitespace at the beginning of the line is\
 significant."

print hello

#tripple quotting (""" or ''')

print """
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
"""

#raw string

hello = r"This is a rather long string containing\n\
several lines of text much as you would do in C."

print hello


