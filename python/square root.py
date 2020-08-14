x=input("Enter a umber of which you want to know the square root.")
x=int(x)
g=x/2
while (g*g-x)*(g*g-x)>0.00000000001:
    g=(g+x/g)/2
    print(g)
print(g)
