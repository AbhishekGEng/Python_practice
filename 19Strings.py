# s1=''
# print(s1)
# s2='P'
# print(s2)
# s3='python'
# print(s3)
# s4='''C
# Java
# Python'''
# print(s4)
# s5=str(99.9)
# print(s5)

# s6='Practice makes perfect'
# print(s6)
# s7='practice makes \'perfect\'' #OR s7='practice makes "perfect"'
# print(s7)
# s8="\"Practice\" makes 'perfect'"
# # or
# # s8='''"practice" makes 'perfect' '''
# print(s8)


# s9="Python"
# print(s9)
# print(s9[5])  #To get each element in string using its index value


# for i in s9:
#     print(i)

#String is immutable
# s9[4]='a'
# print(s9)


# s10="hello"
# s11="world"
# print(id(s10))
# print(id(s11))
# print(s10[4])
# print(s11[1])
# print(id(s10[4]))
# print(id(s11[1]))


# p1='p'
# p2='p'
# print(p1)
# print(p2)
# print(id(p1))
# print(id(p2))
# print(p1)
# print(type(p2))


#Interning of string
#the same element is assigned with same address
# p3='hello'
# p4='world'
# print(p3,p4)
# print(id(p3),id(p4))
# print(p3[2],p3[3],p4[3])
# print(id(p3[2]),id(p3[3]),id(p4[3]))


#String Slicing
a="Guido Van Rossum"
print(a)
print(a[10])
#Slicing Syntax Slicing Syntax Slicing Syntax
#>>>string_name[start:stop:step]
# print(a[::])
print(a[0:5:1])
print(a[0:9:2])
print(a[15:9:1])
print(a[15:9:-1])
print(a[-1:-7:-1])
print(a[::-1])