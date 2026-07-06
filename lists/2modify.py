# #ADD ADD ADD ADD ADD ADD ADD ADD ADD ADD
# lst=[10,20,30,40,50]
# print(lst)
# lst.append(60)
# print(lst)


# #ADDING MULTIPLE TO THE LIST
#     #aproach 1
# #lst.append([70,80,90])  #NOT GOOD WAY
# print(lst+[100])
# lst=lst+[70,80,90]
# print(lst)

#     #2nd approach
# lst.extend([1,2,3])
# print(lst)


# #INSERTING ELEMENT IN MIDDLE using insert()
# lst.insert(2,99)
# print(lst)

# #CHANGING ELEMENT IN THE EXISTING
# lst[3]=300
# print(lst)

# lst[8:]=[999]
# print(lst)

# lst[8:]=[999,888,777]
# print(lst)

# l=[10,20,30,40,50]
# print(l)
# l[::2]=[99,99,99]
# print(l)


# #REMOVE REMOVE REMOVE REMOVE
# ls=[10,20,30,40,50,60]
# print(ls)
# ls.remove(30)
# print(ls)

# #REMOVE ALL OCCURANCE
# ll=[10,20,30,40,50,30]
# print(ll)
# print(30 in ll)
# print(30 not in ll)
# while 30 in ll:
#     ll.remove(30)
#     print(ll)


#POP POP POP POP POP POP
#it will automatically pop the last element
# r=[1,2,3,4,5,6,7]
# print(r)
# r.pop()
# print(r)

#POP our wish element
# r.pop(3)
# print(r)


#DEL DEL DEL DEL DEL DEL
e=[1,2,3,4,5,6,7]
print(e[-6:-1])
print(e)
# del e[3]
# print(e)

# del e[2:6]
# print(e)

del e[::2]
print(e)