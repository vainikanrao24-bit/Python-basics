def User():
    num1 = int(input("enter the first number :"))
    num2 = int(input("enter the second number :"))
    return num1, num2


def add(a=0, b=0):
    return a + b


def sub(a=0, b=0):
    return a - b


def multiply(a=0, b=0):
    return a * b

print("WELCOME TO CALCULATOR")
while True:
    print("Select the choice :\n 1:Add\n 2:Sub \n 3:Multiply\n 4:Stop")
    choice=int(input("Enter your choice"))
    if choice==1:
        x,y=User()
        print(f"addition of two numbers is: {add(x,y)}")
    elif choice==2:
        x,y=User()
        print(f"subtraction of two numbers is:{sub(x,y)}")
    elif choice==3:
        x,y=User()
        print(f"multiplication of two numbers is :{multiply(x,y)}")
    elif choice==4:
        print("thank you for using calculator")
        break



