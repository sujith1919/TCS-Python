from xml.etree import ElementTree

f=open('sample.xml','r')
tree=ElementTree.parse(f)


for node in tree.iter():
    print(node.tag,node.attrib,node.text)
	
f.close()