#String Operations

#i)Concatination
# s='hello'+'world'
# print(s)

#ASCII ASCII ASCII ASCII
# c="a"
# print(chr(ord(c)-32))

#converting the string to uppercase
# s=input("Enter a string:")
# u=''
# for i in s:
#     if ord(i)>=97 and ord(i)<=122:
#         u=u+chr(ord(i)-32)
#     else:
#         u=u+i
# print(u)

#USing built in function upper()
# s=input("Enter a string")
# u=s.upper()
# print(u)

#USing built in function lower()
# s=input("Enter a string")
# u=s.lower()
# print(u)


#String Comparison
s1='python'
s2='java'
if s1==s2:
    print("equal")
else:
    print("not equal")

#reverse second half of string
# s=input("Enter a string:")
# print(s[:len(s)//2:]+s[len(s)-1:(len(s)//2)-1:-1])