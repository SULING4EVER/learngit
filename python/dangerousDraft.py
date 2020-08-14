'''Tic Tac Toe''

print('*********Tic Tac Toe, here we GO!*********')

theBoard={'top-l':' ','top-m':' ','top-r':' ',
          'mid-l':' ','mid-m':' ','mid-r':' ',
          'low-l':' ','low-m':' ','low-r':' '}

theBoard['top-l']='X'

def printBoard(board):
    print(theBoard['top-l']+'|'+theBoard['top-m']+'|'+theBoard['top-r'])
    print("-+-+-")
    print(theBoard['mid-l']+'|'+theBoard['mid-m']+'|'+theBoard['mid-r'])
    print("-+-+-")
    print(theBoard['low-l']+'|'+theBoard['low-m']+'|'+theBoard['low-r'])

turn='X'
move=input


printBoard(theBoard)
    
