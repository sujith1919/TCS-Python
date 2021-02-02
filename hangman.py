#this is a simple implementation of hangman game

pictures=[]
pictures.append("")
pictures.append("""
	( o o )
	   -
""")

pictures.append("""
	( o o )
	   -
	   |
	   |
           |
	   |
	   |	   
""")

pictures.append("""
	( o o )
	   -
	   |
	   |
       ----|
	   |
	   |
""")

pictures.append("""
	( o o )
	   -
	   |
	   |
       ----|----
	   |
	   |
""")

pictures.append("""
	( o o )
	   -
	   |
	   |
       ----|----
	   |
	   |
	  / 
	 /   
""")

pictures.append("""
	( o o )
	   -
	   |
	   |
       ----|----
	   |
	   |
	  / \\
	 /   \\
""")
pictures.append("""
	( o o )
	  /-\\
	   |
	   |
       ----|----
	   |
	   |
	  / \\
	 /   \\
""")


def getWord():
	return "encyclopedia"
	
def getLetter():
	return raw_input("Enter your guess: ")

tmpword=[]
lifes=7
word=getWord()

for i in word:
	tmpword.append('_') #create tmpword with '_' chars

def buildTmpWord():
	"""this function build the clue word"""
	global word,tmpword,lifes,misses
	l=getLetter()
	if (l not in word):
		lifes=lifes-1
	for i in range(len(word)):
		if word[i]==l:
			tmpword[i]=l

for i in tmpword:
	print '_ ',
	
print "\n\nLifes left :",lifes,"\n"
			
while(lifes>0):
	buildTmpWord()
	c=' '.join(tmpword) #converts the array tmpword into string
	print c
	if word==c.replace(' ',''):
		print "Congratulations"
		break
	
	print pictures[7-lifes]
	print "Lifes left :",lifes
	