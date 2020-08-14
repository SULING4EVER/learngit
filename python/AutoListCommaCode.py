spam=[]
while True:
    temp=input('Enter argument'+str(len(spam)+1)+\
               ' to constitue a list and enter nothing to break.    ')
    if temp=='':
        break
    spam+=[temp]
    
ans=''
def comma(list):
    global ans
    for i in range(0,len(list)-1):
        ans+=list[i]+', '
    ans+='and '+list[-1]
    ans
    return ans

print(comma(spam))

        
