class notification:
    def get_notification(self):
        pass

class Instagram(notification):

    def get_notification(self):
        print("Anusha has sent you a reel")

class Facebook(notification):

    def get_notification(self):
        print("Anusha has sent you a request")

notify=Instagram()
notify.get_notification()
notify1=Facebook()
notify1.get_notification()






