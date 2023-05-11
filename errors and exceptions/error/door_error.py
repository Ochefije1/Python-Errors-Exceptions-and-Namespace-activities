import time
network_status = 400
trial = 0
opened = False

class Biometrics:
    fingerPrints = ['@13344)^jf']

    def login(cls, fingerPrint=None):
        if fingerPrint in cls.fingerPrints:
            return True
        return False
    
def openDoor(**kwargs):
    biometric = Biometrics()
    feedBack = biometric.login(**kwargs)
    return feedBack

def hasOpened():
    global opened
    return True if opened else False

class doorNotOpenedError(Exception):
    def __init__(self, message="Invalid credentials"):
        super().__init__(message)
        self.message = message

try:
    sensor_reading = '@13344)--dd'  # sendor.read()
    if not openDoor(fingerPrint=sensor_reading):
        raise doorNotOpenedError()
    
except doorNotOpenedError:
    while trial < 3:
        if openDoor(fingerPrint=sensor_reading):
            print('Door opened successfully')
        print("Try again", 3 - (trial + 1), 'remaining')
        trial += 1
        time.sleep(3)
        if trial >= 2:
            sensor_reading = '@13344)^jf'

else:
    print('No errror occured')

finally:
    print('Runs with or withouth error')