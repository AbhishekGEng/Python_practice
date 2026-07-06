#COPY

#1st approach
lst1=[10,20,30,40,50]
lst2=lst1[:]
print(lst1)
print(lst2)
print(id(lst1))
print(id(lst2))

print(lst1 is lst2)

#2nd approach
l1=[1,2,3,4,5]
l2=list(l1)
print(l1)
print(l2)
print(id(l1))
print(id(l2))

print(l1 is l2)


ls1=[[10,20],[30,40]]
ls2=list(ls1)
print(ls1)
print(ls2)
print(id(ls1))
print(id(ls2))

print(ls1 is ls2)
ls1.append([50,60])
print(ls1)
print(ls2)