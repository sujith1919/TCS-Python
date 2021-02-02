#write a function which returns all the indices of a char in a string

def getindices(word,char):
	indices=[]
	for x in range(len(word)):
		if word[x]==char:
			indices.append(x)
	return indices
	
print getindices('cisco','c')