print("WELCOME")
balance=10000
type=input("enter your type")
amount = int(input("enter the amount"))
if(type== "credit"):
     print("the amount is credited successfully")
    balance=balance+amount
    print(balance)
else(type=="debit"):
   print(" transaction completed")
    balance=balance-amount
    print(balance)
if(amount>balance):
    print("insufficient balance")
else:
     print(balance)