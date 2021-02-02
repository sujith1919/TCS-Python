b=[3,5,4,1,0,2,6,7,8]
while True:
	print b[0],b[1],b[2],'\n',b[3],b[4],b[5],'\n',b[6],b[7],b[8]
	Move=int(raw_input("\n Enter move : "))
	MovePosition= b.index(Move)
	ZeroPosition= b.index(0)
	b[ZeroPosition]=Move
	b[MovePosition]=0

#this program implements sliding puzzle without move validation