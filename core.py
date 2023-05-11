from helpers.sms import SMS as sms, SMS_API_KEY
from helpers.video import StreamVideo as video


class Main:
    def __init__(self, video, sms, customer) -> None:
        self.video = video
        self.sms = sms
        self.customer = customer

    def stream(self):
        if self.video.isComplete:
            print(self.sms.send())


    def start(self):
        self.stream()
        return 'streaming started'
    
if __name__=="__main__":
    main = Main(video, sms, None)
    main.start()
