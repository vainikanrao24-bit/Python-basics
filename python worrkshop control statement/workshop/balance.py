balance=10000
amount=int(input("enter the amount"))
if(amount>balance):
    print("you have insufficient balance")
else:
    print("your amount has been debited")
    balance=balance-amount
    print(balance)