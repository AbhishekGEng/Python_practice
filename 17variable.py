# #Global variables
# x=99
# def fun():
#     y=999  #Local variable
#     print(y)
#     print(x)
#     print(globals())  #To get the inbuilt global variables which are default present in the script file
#     print(locals())   #To get the local variables in the script
# fun()
# print(x)



x=99
def fun():
    global x
    x=999
    print(x)
fun()
print(x)