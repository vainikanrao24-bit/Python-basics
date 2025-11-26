class app:


    def __init__(self,application_name,categories,Company,Size,no_of_users,ratings):
        self.application_name=application_name
        self.categories=categories
        self.Company=Company
        self.Size=Size
        self.no_of_users=no_of_users
        self.ratings=ratings
    def sign_up(self):
        print(f"Sign up done,{self.application_name}")
    def login(self):
        print(f"Sign in successfull . welcome to {self.application_name}")
    def log_out(self):
        print("Thank you for using")
    def details(self):
        print(f"The {self.application_name} is {self.categories} developed by {self.Company} and its size is {self.Size} and  {self.no_of_users} are using this app it has {self.ratings} ratings")

application1= app("Instagram","Social media","Meta",42.47,10000,4.4)
application2= app("Linkedin","professional site","Microsoft",45,100000,4.5)
application3= app("Facebook","Social media","Meta",45,1000090,4)
application4= app("Meesho","E commerce site","Fashnear",42.47,1000000,4.8)
application1.sign_up()
application1.login()
application1.log_out()
application1.details()
application2.sign_up()
application2.login()
application2.log_out()
application3.details()
application3.sign_up()
application3.login()
application3.log_out()
application3.details()
application4.sign_up()
application4.login()
application4.log_out()
application4.details()








