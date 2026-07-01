# def add(a,b):
#     c=a+b
#     print(a)
#     print(b)
#     print(c)
# a=int(input("Enter a:"))
# b=int(input("Enter b:"))
# add(b,a)

#  user defined Function

# i)no input no return output
def mul():
    a=10
    b=20
    c=a*b
    print(c)
mul()

#ii)input no return output
def mul(a,b):
    c=a*b
    print(c)
x=10
y=30
mul(x,y)

#iii)no input but return output
def mul():
    a=20
    b=25
    c=a*b
    return c
res=mul()
print(res)

#iv)input and return output
def mul(a,b):
    c=a*b
    return c
res1=mul(21,23)
print(res1)