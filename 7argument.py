#ARGUMENTS ARGUMENTS ARGUMENTS ARGUMENTS

#i)Positional Arguments
def power_of(a,b):
    c=a**b
    print(c)
power_of(2,3)
power_of(3,2)
#power_of(3)         #ERROR 

#ii)Default Arguments
def power(a,b=0):
    c=a**b
    print(c)
power(2,3)
power(3,2)
power(2)

#iii)KeyWord Arguments
def pow(a,b):
    c=a*b
    print(c)
pow(a=2,b=5)
pow(b=5,a=2)

#iv)Variable length arguments
#The single argument cant accept all the
#parameters to make it possible use *
def pizza(*toppings):
    print(toppings)
pizza("cheese")
pizza("cheese","onion","olives","corn")

def piz(name,*top,crust):
    print(name)
    print(top)
    print(crust)
    
piz("abhi","cheese","onion","olives",crust="corn")

#v)Variable length keyword argument
#To accept the values with their key add **
def std(**data):
    print(data)
    print(type(data))
std(name="abhi",age=23,weight=57.87,sex="M")