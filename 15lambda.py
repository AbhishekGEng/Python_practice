#Syntax 
# lambda arguments : expression


n=(lambda num,p : num**p)(3,2)
print(n)

m=(lambda n,d : n/d)(10,2)
print(m)
b=(lambda n,d : n/d)(100,2)
print(b)

#REuse it ✅
fun=lambda n,d : n/d
res=fun(30,3)
print(res)