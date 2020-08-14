#! /usr/bin/env python3.


'''let the user input an integer and keep calling the collaz()
on that integer until the return vaue is 1.
print the collaz sequence.'''

while True:

    temp=input('Input an integer and I\'ll show you the collaz sequence.     ')

    try:
        ans=int(temp)
    except ValueError:
        print('Your input is not an integer or a float.')

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
          
    while ans!=1:
        collaz(ans)
            
        
