#! /usr/bin/env python3

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
    if theBoard['top-l']!=' 'and theBoard['top-m']!=' 'and theBoard['top-r']!=' '\
    and theBoard['mid-l']!=' 'and theBoard['mid-m']!=' 'and theBoard['mid-r']!=' '\
    and theBoard['low-l']!=' 'and theBoard['low-m']!=' 'and theBoard['low-r']!=' ':
        print('Oops,tie game.')
        break
    printBoard(theBoard)
    move=input('Turn for '+turn+'. Move on which space?     ')
    try:
        if theBoard[move]==' ':
            theBoard[move]=turn
        else:
            print('Slot occupied! s')
    except KeyError:
        print('It\'s not a right slot name.')
        continue
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
printBoard(theBoard)



   
