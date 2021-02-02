import doctest

def Hello():
        """
         >>> import HelloWorld
         >>> Hello()
        "Hello, World"
        """
        print( "Hello, World")

		
doctest.main()