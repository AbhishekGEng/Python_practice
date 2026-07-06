#STRING FORMATTING
#using format(),f string literals

#i)format() method

#Syntax:>
#  str.format(*args)
# name=input("Enter the name:")
# place=input("Enter your place:")
# print("Hello {},how is the weather in {}?".format(name,place))


# s="{} {} {}".format(10,20,30)
# print(s)

# s="{2} {0} {1}".format(10,20,30)
# print(s)

#str----->"{position:format_specification}"
#format_specification types:
#*Alignment
#-right(>)
#-left(<)
#-center(^)

# s="{0:>10}".format(999)
# print(s)
# s="{0:*>10}".format(999)
# print(s)
# s="{0:<10}".format(999)
# print(s)
# s="{0:*<10}".format(999)
# print(s)
# s="{0:^10}".format(999)
# print(s)
# s="{0:*^10}".format(999)
# print(s)

#*presentation
#-f fixed point notation
#-e exponent notation

# import math
# print(math.pi)
# f="{}".format(math.pi)
# print(f)

# f="{0:.2f}".format(math.pi)
# print(f)

# f="{0:10.4f}".format(math.pi)
# print(f)

# f="{0:010.4f}".format(math.pi)
# print(f)


# #Exponent notation
# earth_weigh=597600000000000000000000
# e="{0:e}".format(earth_weigh)
# print(e)

# e="{0:.3e}".format(earth_weigh)
# print(e)


# # k="{} {} {}".format([10,20,30])
# # print(k)

# k="{}".format([10,20,30])
# print(k)

# k="{0[0]} {0[1]} {0[2]}".format([10,20,30])
# print(k)

# #using unpacking
# k="{} {} {}".format(*[10,20,30])
# print(k)



#Pgm to find the average of a given number

num=input("entr the number:").split()
print(num)
l=list(map(int,num))
print(l)
sum=0
for i in l:
    sum+=i
print(sum)
print("{0:.4f}".format(sum/len(l)))