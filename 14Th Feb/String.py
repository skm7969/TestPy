#assigning sting to a variable
str1="Hello"
str2='Hello'

#creating a empty string
str3=''
str4=""

# Mutable & immutable -_______ Strings are immutable which means we can change the value later
#
# immutable means data once assigned cannot be changed later

# #concatenation/Joining + & *
# str5= "Welcome"
# print(id(str5))
#
# str5="Bala"+str5
# print(id(str5))
#
# print(str5)
#
# print(str5*3)

#Slicing []
# str6 = "BalaWelcomeBalaWelcomeBalaWelcome"
# print(str6[2:9])
# print(str6[:10])
# print(str6[2:])
# print(str6[9:2])
#
# str7= 'Subrat'
# print(str7[1:-2])
# print(str7[-2:9])

#ord() & Chr()

# print(ord('s'))
# print(chr(899))

## max() min() len()
#
# print(max("SKM"))
# print(min("SKM"))
# print(len('SMKKK))'))
#
# #In & Not In operatora
#
# d="DEVTA"
# print('DEV' in d)
# print('dev' in d)
# print('ETA' not in d)
# print('VTA' not in d)

#Testing strings

 #b= 'Welcome to Terra'
#
# print(b.isalnum())
# print(b.isalpha())
# print('akm'.isalpha())
# print(b.islower())
# print(b.isupper())
# print(b.isidentifier())
# print(b.isdigit())
# print(b.isspace())

#Search for substring

# b="Where is Naleee"
# print(b.endswith('alu'))
# print(b.startswith('Where'))
# print(b.find('Nalu'))
# print(b.find('IS'))
# print(b.count('e'))

#Conversion of strings

x='namma BENgaluru'
s1=x.capitalize() #Captalises only 1st char & rest all are converted to small
print(s1)

s2=x.title() #Capitalises everything after space
print(s2)

s3=x.lower()
print(s3)

s4=x.swapcase()
print(s4)

s5=x.replace('gal', 'ele')
print(s5)


#Reverse a string

# p='always'
# rev_str=''
# for k in p:
#     rev_str=k+rev_str
# print("reverse string is ", rev_str)

#method 2

qa="Salimar"
rev_astr=qa[::-1]
print(rev_astr)