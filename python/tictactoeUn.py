'''TIC TAC TOE'''

print('*********Tic Tac Toe, here we GO!*********')

theBoard={'top-l':' ','top-m':' ','top-r':' ',
          'mid-l':' ','mid-m':' ','mid-r':' ',
          'low-l':' ','low-m':' ','low-r':' '}

def printBoard(board):
    print(theBoard['top-l']+'|'+theBoard['top-m']+'|'+theBoard['top-r'])
    print("-+-+-")
    print(theBoard['mid-l']+'|'+theBoard['mid-m']+'|'+theBoard['mid-r'])
    print("-+-+-")
    print(theBoard['low-l']+'|'+theBoard['low-m']+'|'+theBoard['low-r'])

turn='X'
while True:
    printBoard(theBoard)
    move=input('Turn for '+turn+'. Move on which space?     ')
    if theBoard[move]==' ':
        theBoard[move]=turn
        
        if theBoard['top-l']==theBoard['top-m']==theBoard['top-r']and theBoard['top-l']!=' '\
        or theBoard['mid-l']==theBoard['mid-m']==theBoard['mid-r']and theBoard['mid-l']!=' '\
        or theBoard['low-l']==theBoard['low-m']==theBoard['low-r']and theBoard['low-l']!=' '\
        or theBoard['top-l']==theBoard['mid-l']==theBoard['low-l']and theBoard['top-l']!=' '\
        or theBoard['top-m']==theBoard['mid-m']==theBoard['low-m']and theBoard['top-m']!=' '\
        or theBoard['top-r']==theBoard['mid-r']==theBoard['low-r']and theBoard['top-r']!=' '\
        or theBoard['top-l']==theBoard['mid-m']==theBoard['low-r']and theBoard['top-l']!=' '\
        or theBoard['top-r']==theBoard['mid-m']==theBoard['low-l']and theBoard['top-r']!=' ':
            print('Congratulations '+turn+'!!You win!')
            break
        
        if turn=='X':
            turn='O'
        else:
            turn='X'
    else:
        print('Slot occupied! ')


printBoard(theBoard)



   
