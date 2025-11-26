age=int(input("enter the age"))
def vote(age):
    if age>=18:
        print("you are eligible to vote")
    else:
        print("you are not eligible to vote")

vote(age)