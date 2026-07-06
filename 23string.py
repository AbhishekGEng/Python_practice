#string replication
# s='python'
# print(s*3)


#string formatting conversion
# a=70
# print(a)
# print("{0:b}".format(a))
# print("{0:o}".format(a))
# print("{0:x}".format(a))


#f-string
name='abhi'
place='sagar'
print("{} {}".format(name,place)) #using format()
print(f"{name} {place}")          #using f-string

print("{1} {0}".format(name,place))  #using format()
print(f"{place} {name}")          #using f-string

import math
print("{0:.4f}".format(math.pi))    #using format()
print(f"{math.pi:.4f}")

import timeit
print(timeit.timeit(stmt="{0:.2f}".format(3.1416),number=10000))
print(timeit.timeit(stmt=f"{3.1416:.2f}",number=10000))



#raw string literal
nam="Ro\nhit"
print(nam)
nam=r"Ro\nhit"
print(nam)