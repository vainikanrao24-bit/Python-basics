class Aadhar:

    def __init__(self,name,aadhar_no,dob,finger_print,retina):
        self.name=name
        self.aadhar_no=aadhar_no
        self.dob=dob
        self._finger_print=finger_print
        self.__retina=retina

    def display_userData(self):
        print(f"The Aadhar number is:{self.aadhar_no} ")
        print(f"The Aadhar holder name is:{self.name} ")
        print(f"The Aadhar holder date of birth is:{self.dob} ")
        print(f"The Aadhar holder finger print is:{self._finger_print} ")
        print(f"The Aadhar holder retina details is:{self.__retina} ")

details=Aadhar("Vainika",23447578,"24-dec-2002","f112345","black")
details.display_userData()




