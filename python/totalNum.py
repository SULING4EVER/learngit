house={'ling':{'chair':3,'desk':1,'pot':4},
       'jiamin':{'chair':5,'book':18,'cup':20},
       'soo':{'car':1,'chair':9,'desk':1}}

def allHouse(houses,item):
    numItems=0
    for p,i in houses.items():
        numItems+=i.get(item,0)
#        print(p+str(i.get(item,0)))
    return numItems

print('Number of properties:')
print('-chair: '+str(allHouse(house,'chair')))
print('--desk: '+str(allHouse(house,'desk')))
print('---car: '+str(allHouse(house,'car')))
