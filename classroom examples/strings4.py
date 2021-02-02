#string methods

name = "mohandas KARAmchand ganDHI"

print(name)

#finding

print(name.index("h"))
print(name.index("chand"))
print(name.rindex("h"))
print(name.rindex("chand"))
#print(name.index("hello")) # raises an exception

print(name.find("h"))
print(name.find("chand"))
print(name.rfind("h"))
print(name.rfind("chand"))
print(name.find("hello")) # returns -1

#counting
print(name.count("a"))


#case insensitive matches

mystring = "GOOD morning"

searchstring1 = "good"

searchstring2 = "MORNING"

print(mystring.find(searchstring1))
print(mystring.find(searchstring2))


print(mystring.lower().find(searchstring1.lower()))
print(mystring.lower().find(searchstring2.lower()))


#searching

string = "How are you doing today"

print("today" in string)

print(string.startswith("today"))
print(string.startswith("How"))

print(string.endswith("today"))
print(string.endswith("How"))





