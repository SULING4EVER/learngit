#! /usr/bin/env python3

import pyperclip
text=pyperclip.paste()
textt=text.split('\n')
for i in range(0,len(textt)):
    textt[i]='* '+textt[i]
tex='\n'.join(textt)
pyperclip.copy(tex)
print(tex)
