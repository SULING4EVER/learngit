import pprint

temp=input('Enter whatever you want...      ')
cal={}

for data in temp:
    cal.setdefault(data,0)#add key-value pair to the dictionary
    cal[data]+=1

print(pprint.pformat(cal))
print(cal)
    
