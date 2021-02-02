#Lists
#List is  the most versatile compound data type.
#It is written as a list of comma-separated values (items) between square brackets.
#List items need not all have the same type.

>>> a = ['spam', 'eggs', 100, 1234]
>>> a
['spam', 'eggs', 100, 1234]

#Like string indices, list indices start at 0, and lists can be sliced, concatenated and so on:



>>> a[0]
'spam'
>>> a[3]
1234
>>> a[-2]
100
>>> a[1:-1]
['eggs', 100]
>>> a[:2] + ['bacon', 2*2]
['spam', 'eggs', 'bacon', 4]
>>> 3*a[:3] + ['Boo!']
['spam', 'eggs', 100, 'spam', 'eggs', 100, 'spam', 'eggs', 100, 'Boo!']

#slicing lists

>>> a[:]
['spam', 'eggs', 100, 1234]

#Unlike strings, it is possible to change individual elements of a list:


>>> a
['spam', 'eggs', 100, 1234]
>>> a[2] = a[2] + 23
>>> a
['spam', 'eggs', 123, 1234]


#Assignment to slices is also possible,
#and this can even change the size of the list or clear it entirely:

>>> # Replace some items:
... a[0:2] = [1, 12]
>>> a
[1, 12, 123, 1234]
>>> # Remove some:
... a[0:2] = []
>>> a
[123, 1234]
>>> # Insert some:
... a[1:1] = ['bletch', 'xyzzy']
>>> a
[123, 'bletch', 'xyzzy', 1234]
>>> # Insert (a copy of) itself at the beginning
>>> a[:0] = a
>>> a
[123, 'bletch', 'xyzzy', 1234, 123, 'bletch', 'xyzzy', 1234]
>>> # Clear the list: replace all items with an empty list
>>> a[:] = []
>>> a
[]

#finding length of a list

>>> a = ['a', 'b', 'c', 'd']
>>> len(a)
4

#nesting lists

>>> q = [2, 3]
>>> p = [1, q, 4]
>>> len(p)
3
>>> p[1]
[2, 3]
>>> p[1][0]
2
>>> p[1].append('xtra')     
>>> p
[1, [2, 3, 'xtra'], 4]
>>> q
[2, 3, 'xtra']

# try this

a.insert(0, 'Python')



