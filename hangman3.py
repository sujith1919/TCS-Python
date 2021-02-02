import sys
if __name__!='__main__':
	print "run this directly. don't import"
	sys.exit()


def getword():
	import random
	f=open('words.txt','r')
	words=f.readlines()
	f.close()
	return random.choice(words).rstrip()
def getindices(word,char):
	indices=[]
	for x in range(len(word)):
		if word[x]==char:indices.append(x)
	return indices
word=getword()
guessword=list(len(word)*'_'	)
lives=5
while True:
	print ' '.join(guessword)
	print "lives=",lives
	guesschar=raw_input('Enter your guess..')
	matched=getindices(word,guesschar)
	if matched:
		for i in matched:
			guessword[i]=guesschar
		if guessword==list(word):
			print 'You got it'
			break
	else:
		lives-=1
		if lives==0:
			print 'Sorry I have to hang you'
			break