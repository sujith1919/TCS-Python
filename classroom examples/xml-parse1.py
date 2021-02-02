from xml.dom import minidom

a=minidom.parse("sample.xml")

print(a.childNodes)

print(dir(a))

for node  in a.getElementsByTagName('price'):
    print( node.firstChild.data)

	
for node  in a.getElementsByTagName('food'):
	for x in node.childNodes:
		print(x.)
