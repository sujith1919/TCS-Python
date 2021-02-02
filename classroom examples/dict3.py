#working with dictionary
#printing

colors  = {"night":"black",
"day":"white",
"sky":"blue",
"sea":"blue"
}

for x in colors:
	print(x)
	
for x in colors:
	print(x,colors[x])

for key,value in colors.items():
	print(key,value)
		
