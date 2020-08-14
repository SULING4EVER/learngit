'''let the user input an integer and keep calling the collaz()
on that integer until the return vaue is 1.
print the collaz sequence.'''

while True:
    temp=input('Input an integer and I\'ll show you the collaz sequence.     ')
    if temp=='':
        break
    
    try:
        ans=int(temp)
    except ValueError:
        print('Your input is neither an integer nor a float.')

    def collaz(number):
        global ans
        if ans%2==0:
            ans//=2
            print(ans)
            return ans
        else:
            ans=ans*3+1
            print(ans)
            return ans
        
    if ans==1:
        print(ans)
        
    while ans!=1:
        collaz(ans)
            
        
