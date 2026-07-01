s={10,20,30,40,50}
print(s)
print(type(s))
#print(s[10])   #ERROR

#adding the value/element using add
s.add(200)
print(s)

#remove the element from the set using remove()
s.remove(200)
print(s)

#Set will not allow the duplicate of set
s.add(50)
print(s)