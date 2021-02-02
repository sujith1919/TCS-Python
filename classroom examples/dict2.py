#working with dictionary

colors  = {"night":"black",
"day":"white",
"sky":"blue",
"sea":"blue"
}

#how to look up a dictionary
print(colors["sky"])
print(colors.get("day"))
#how to add to a dictionary
#dict[key]=value
colors["blood"] = "red"
print(colors)
#how to modify a dictionary
colors["day"] = "bright"
#how to delete a dictionary element
del colors["sea"]


