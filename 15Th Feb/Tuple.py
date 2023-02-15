# #creating tuple
#
# tuple1=('apple','banana','kiwi')
# print(tuple1)
#
# tuple4=()
#
# #Individual items access
#
# tuple2=('apple','banana','kiwi')
#
# print(tuple2[2])
#
# #Range of indexes
#
# tuple5 = ('banana','cherry','kiwi','badhela','dates','lemon',"prunes")
# print(tuple5[2:6])
# print(tuple5[-4:-1])
#
# #Change tuple values
#
# # tuple5[2]='Kochi'
# # print(tuple5)
#
# #In tuple we cannot change/modify/append/remove values as its immutable Hence tuples are more secure then list
#
# #There is one way-- WHere we can change a tuple to list change the values & then convert back to a tuple
#
# #tuple-- List(modify) -- tuple
#
# list5=list(tuple5)
# list5[2]='CLoves'
# tuple5=tuple(list5)
# print(tuple5)
# tuple6=('asa',9,99.00,"swere")
# print(tuple6)

#REading tuple using loops
# tuple5 = ('banana','cherry','kiwi','badhela','dates','lemon',"prunes")
# for l in tuple5:
#     print(l)

#Check existance of an item
tuple5 = ('banana','cherry','kiwi','badhela','dates','lemon',"prunes")
# if input("Enter the name TBS") in tuple5:
#     print("Present")
# else:
#     print("Not present")

#Find total items in tuple
# print(len(tuple5))

#add items to tuple - Not possible as its immutable

#copying of tuples

tuple6=tuple5
print(tuple6)

#deletion of tuples
# del tuple6
# print(tuple6)

#joining 2 tuples
tuple66 = ('nana','erry','wi','hela','es','lemon',"prunes")
tuple7=tuple66+tuple5
print(tuple7)

#Comparing tuples

if tuple66!=tuple5:
    print("Equals")
else:
    print("not equal")
