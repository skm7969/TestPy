#List

# mylist=[10, 20,30,40]
# mylist1=['cherry','banana','twist']
# mylist3=['apple',30,'eel',50]
# mylist4=[]
#
# print(mylist,mylist4,mylist3,mylist1)

#Accessing items from list
#
# mylist=["apple",'banana','cherry']
# print(mylist[2])
# print(mylist[-2])

#range of indexes

# mylistee2=["apple",'banana','cherry','kiwi','badhela','dates','lemon']
# print(mylistee2[1:-3])
# print(mylistee2[-4:-1])

# #change items in a list
# mylistee2=["apple",'banana','cherry','kiwi','badhela','dates','lemon']
# print(mylistee2)
# mylistee2[2]='apricot'
# print(mylistee2)
#
# #read items from a list using loop
# myliste2=["apple",'banana','cherry','kiwi','badhela','dates','lemon']
# for j in myliste2:
#     print(j)

#check if item exists in list or not

# myliste2=["apple",'banana','cherry','kiwi','badhela','dates','lemon']
# if "bdhela" in myliste2:
#     print('present')
# else:
#     print('not present')

#find length of list

# mylistee2=["apple",'banana','cherry','kiwi','badhela','dates','lemon']
# print(len(mylistee2))

#Adding new items append() & insert()

# mylistee2=["apple",'banana','cherry','kiwi','badhela','dates','lemon']
# mylistee2.append('prunes')
# print(mylistee2)
#
# mylistee2.insert(-2,'almonds')
# print(mylistee2)
# mylistee2.insert(2,'Balmonds')
# print(mylistee2)

#remove items from list
#
# mylistee2=["apple",'banana','cherry','kiwi','badhela','dates','lemon']
# mylistee2.pop(-3)
# mylistee2.pop(3)
# print(mylistee2)
# #del
# del mylistee2[2]
# print(mylistee2)
#
# del mylistee2[-1]
# print(mylistee2)
#
# #clear
# mylistee2.clear()
# print(mylistee2)

#copy a list
# mylist22= ["apple",'banana','cherry','kiwi','badhela','dates','lemon']
# mylist32=list(mylist22)
# print(mylist32)
#
# mylist42=mylist32.copy()
# print(mylist42)

#using + operator
# dollar4=['a','b','c']
# dollare5=[1,2,3,'a']
# dollar1=dollar4+dollare5
# print(dollar1)

#using append()

# List1=['v','f','x']
# List2=['2','3','4']
# List3=[99,88,77]
#
# for j in List1:
#     List2.append(j)
#     List3.append(j)
#
# print(List2)
# print(List3)

#Using extend()

List1=['v','f','x']
List2=['2','3','4']
List3=[99,88,77]

List1.extend(List2)
List1.extend(List3)

print(List1,List3)