class Mobile:

    def __init__(self):
        pass

    def calling(self):
        print("Invoking calling function")

    def SMS(self):
        print("Invoking the SMS function")

    def games(self):
        print("Invoking the games")


class Redmi(Mobile):
    def camera(self):
        print("Invoking the camera")

    def music(self):
        print("Invoking the music")

    def vedio_call(self):
        print("Invoking the vedio call")

mobile1=Redmi()
mobile1.music()
mobile1.camera()
mobile1.vedio_call()
mobile1.calling()
mobile1.SMS()
