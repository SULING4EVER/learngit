'''regex version of strip()'''

import re
conn=input('enter your text to be modified~   ')
print(conn)

argB=input('enter character you want to strip~  ')
if argB==None:
    print(argB)
    dan=conn.strip()
    print(dan)
else: 
    dne=re.compile(r'[argB]+')
    dee=dne.sub('',conn)
    print(dee)


