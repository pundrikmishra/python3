import re

exmpleString='''
Kajal is 0 year old, and Poojan is 27 year old.
Pundrik is 23, and his friend, Jani, is 102.
''' 

# ages =re.findall(r'\d{1,3}', exmpleString)
# names=re.findall(r'[a-z][a-z]*', exmpleString)
# print(ages)
# print(names)

# names=re.findall(r'[a-z][a-z]', exmpleString)
# print(names)

# names=re.findall(r'[a-z]', exmpleString)
# print(names)

# names=re.findall(r'[a-z]*', exmpleString)
# print(names)

# names=re.findall(r'[A-Z][a-z]', exmpleString)
# print(names)

ages =re.findall(r'\d{1,3}', exmpleString)
names=re.findall(r'[A-Z][a-z]*', exmpleString)
print(ages)
print(names)

# print(ages[0])
# print(names[0])

dictionary={}
y=0
for i in range(len(names)):
    dictionary[i]=ages[y]
    y+=1

print(dictionary)
