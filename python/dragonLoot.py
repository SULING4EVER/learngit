'''Dragon loot inventory.'''

inventory={'arrow':12,'gold coin':42,'rope':1,'torch':6,'dagger':1}
           
def display_inventory(invent):
    num_stuff=0
    for k,v in invent.items():
        print(str(v)+' '+k)
        num_stuff+=v
    print('Total items: '+str(num_stuff))

#loot=['gold coin','dagger','gold coin','gold coin','ruby']
loot=[]
while True:
    temp=input('Enter your vanquished dragon\'s loot.Enter nothing to break.  ')
    if temp=='':
        break
    loot+=[temp]

def addItemsToInt(inven,addItems):
    for i in addItems:
        inven.setdefault(i,0)
        inven[i]+=1

addItemsToInt(inventory,loot)
display_inventory(inventory)
