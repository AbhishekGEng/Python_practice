# #BUILT IN FUNCTIONS:
# lst=['python','java','django','spring']
# s=''
# for i in lst:
#     s=s+i
# print(s)


# #JOIN JOIN JOIN JOIN function
# #############################
# s1=''.join(lst)             #
# print(s1)                   #
#                             #
# #############################
# a='a'
# print(ord(a))
# print(chr(97))
# print(chr(65))

# url=['https://www.google.com','https://www.amazon.com','https://www.youtube.com','https://www.googl.com']
# for i in url:
#     if i[0:5:1]=='https':
#         print(i)
#     else:
#         print("not")


# link=['https://www.google.com','https://www.amazon.com','https://www.youtube.com','https://www.googl.com']
# for i in link:
#     if i.startswith("https"):
#         print(i)

# lnk=['https://www.google.com','https://www.amazon.com','https://www.youtube.org','https://www.googl.com']
# for i in lnk:
#     if i[len(i)-3::]=="com" and i[len(i)-4::]=="com":
#         print(i)


# lmk=['https://www.google.com','https://www.amazon.com','https://www.youtube.org','https://www.googl.com']
# for i in lmk:
#     if i.endswith(("com","com/")):
#         print(i)





#COUNTING TOTAL LETTERS(UPPER CASE,LOWER CASE),numbers,special character
#Using  islower(),isupper(),isnumeric()
# n=input("Enter a string:")
# low,up,sp,num,=0,0,0,0
# for i in n:
#     if i.islower():
#         low+=1
#     elif i.isupper():
#         up+=1
#     elif i.isnumeric():
#         num+=1
#     else:
#         sp+=1
# print("lowercase=",low)
# print('uppercase:',up)
# print("numbers:",num)
# print("special:",sp)



#swapcase(),title(),capitalize()
# s='STAY HOME stay safe'
# print(s.swapcase())   #or print("stay home stay happy".swapcase())
# print(s.title())      #or print("stay home stay happy".title())
# print(s.capitalize()) #or print("stay home stay happy".capitalize())



#string Translation
#using maketrans(),translate()
s="Error 404 page not found"
table=s.maketrans("aeiou","AEIOU","0123456789")
n=s.translate(table)
print(n)