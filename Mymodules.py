def add():
    a=10
    b=20
    c=a+b
    print(c)
def sub():
    a=10
    b=20
    c=b-a
    print(c)
def mul():
    a=10
    b=20
    c=a*b
    print(c)

#To avoid unnecessary execution while we running in imported file
if __name__=='__main':
    add()
    sub()
    mul()