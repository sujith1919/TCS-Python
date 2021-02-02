import doctest

def add(a,b):
    """
>>> add(3,4)
7
>>> add(0,0)
0
>>> add(-1,1)
0
>>> add(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: add() missing 1 required positional argument: 'b'
>>> add("b","a")
'ba'
>>> add("b",9)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in add
TypeError: must be str, not int
"""
    return a+b

doctest.testmod()
