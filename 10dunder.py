import Mymodules
def fun():
    a=10
    b=2
    c=a**b
    print(c)
fun()

#if we do so,as we imported the Mymodules 
#the functions from the mymodules executes automatically
#This is because as we create a file the python automatically
#assign it a variable called __name__ and the value is __main__
#in its script mode,if we are importing it as a module it will be the
#module name ,so wehave to cross check with if statement,
#syntax:>if __name__==_'__main__'