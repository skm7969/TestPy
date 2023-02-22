#creating dictionaries
dict1={2:'x',3:'y','sweet':"x"}
print(dict1)

#accessing items from dictionary

dict2={
    'brand':'Hyundai',
    "model": 'i10',
    "price": 20000
}

print(dict2['price'])

#using get() function

s=dict2.get('model')
print(s)

#change values in dictionary
dict2['year']=2023
dict2['price']=200
print(dict2)


# for i in dict2:
#     print(dict2[i])

for i in dict2.values():
    print(i)

for a,l in dict2.items():
    print(a,l)

#check a key is present in dictionary or not
if "modl" in dict2:
    print("yes")
else:
    print("no")

print('year' in dict2)

#find number of items in a dictionary

print(len(dict2))

#adding items to dictionary

dict2['engine']='snappy'
print(dict2)


#remove items from dict

dict2.pop('year')
print(dict2)

del dict2['engine']
print(dict2)

# del dict1
# print(dict1)

# dict2.clear()
# print(dict2)

#copy one to another dict

# dict3=dict2
# print(dict3)

#using copy()
dict6=dict2.copy()
print(dict6
      )