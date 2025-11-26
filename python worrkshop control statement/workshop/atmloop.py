balance=1000
while True:
    type=input("enter the type credit/debit/stop")
    if(type=="stop"):
        break
    elif(type=="credit"):
        credit_amount=int(input("enter the credit Amount:"))
        balance=balance+credit_amount
        print(f"the current balance is{balance}")
    elif(type=="debit"):
        debit_amount=int(input("enter the debit amount:"))
        if(balance>debit_amount):
            balance=balance-debit_amount
            print(f"the current balance is{balance}")
        else:
            print("insuffient balance")
    else:
        print(f" balance is{balance}")