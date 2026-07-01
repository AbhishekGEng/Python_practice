a=99
print(a)
print(type(a))
b=float(a)
print(b)
print(type(b))

c=99.9          #\
print(c)        # \
print(type(c))  #   }
d=int(c)        # /
print(d)        #/


# the a is assigned to a value and that value has an address that addres
a=10
print(a)
print(type(a))
print(id(a))
a=20
print(a)
print(type(a))
print(id(a))
print(a is a)

a=10
print(a)
print(type(a))
print(id(a))
b=10
print(a)
print(type(a))
print(id(a))
print(a is b)
