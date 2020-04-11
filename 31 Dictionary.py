exDict={'Kajal':0, 'Pundrik':23, 'Vrinda':1, 'Dhruv':22, 'Poojan':21}
print(exDict)
print(exDict['Kajal'])
exDict['Mehata Ji']=0
print(exDict)
exDict['Mehata Ji']=00
print(exDict)
#exDict['Mehata Ji']=01
print(exDict)
exDict['Mehata Ji']=1
print(exDict)
del exDict['Pundrik']
print(exDict)
exDict={'Kajal':[0,'blonde'], 'Pundrik':[23,'black'], 'Vrinda':[1,'brown'], 'Dhruv':[22,'red'], 'Poojan':[21,'green']}
print(exDict)
print(exDict['Kajal'])
print(exDict['Kajal'][1])
exDict={'Kajal':[0,'blonde','Total mad'], 'Pundrik':[23,'black','Thoda mad'], 'Vrinda':[1,'brown','mad'], 'Dhruv':[22,'red','smart'], 'Poojan':[21,'green','very smart']}
print(exDict)
print(exDict['Kajal'][2])
