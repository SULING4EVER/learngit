'''Tic Tac Toe'''

theBoard={'top-l':' ','top-m':' ','top-r':' ',
          'mid-l':' ','mid-m':' ','mid-r':' ',
          'low-l':' ','low-m':' ','low-r':' '}

def printBoard(board):
    print(theBoard['top-l']+'|'+theBoard['top-m']+'|'+theBoard['top-r'])
    print("-+-+-")
    print(theBoard['mid-l']+'|'+theBoard['mid-m']+'|'+theBoard['mid-r'])
    print("-+-+-")
    print(theBoard['low-l']+'|'+theBoard['low-m']+'|'+theBoard['low-r'])

printBoard(theBoard)
    
