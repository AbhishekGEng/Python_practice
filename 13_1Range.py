# print(list(range(5)))
# print(list(range(1,5)))
# print(list(range(2,10,2)))


# balance=15500
# min_balance=500
# print("Before transaction:",balance)
# while min_balance<balance:
#     balance=balance-1000
#     print(balance)
#     if balance==500:
#         print("We cant deduct more")
# print("after transaction:",balance)


balance=15500
min_balance=500
print("Before transaction:",balance)
for i in range(5):
    balance=balance-1000
    print(balance)
    if balance==500:
        print("We cant deduct more")
print("after transaction:",balance)