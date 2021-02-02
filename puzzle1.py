board=[3,5,4,1,0,2,6,7,8]
validmoves={0:(1,3),
			1:(0,2,4),
			2:(1,5),
			3:(0,4,6),
			4:(1,3,5,7),
			5:(4,2,8),
			6:(3,7),
			7:(4,6,8),
			8:(5,7)}
def PrintBoard():
	print board[0],board[1],board[2]
	print board[3],board[4],board[5]
	print board[6],board[7],board[8]

def GetMove():
	return int(raw_input("\n Enter move : "))
	
def GetPosition(num):
	return (board.index(num))
	
while True:
	PrintBoard()
	Move=GetMove()
	MovePosition= GetPosition(Move)
	ZeroPosition= GetPosition(0)
	#check for valid move
	if MovePosition in validmoves[ZeroPosition]:
		#swap positions
		board[ZeroPosition]=Move
		board[MovePosition]=0
	