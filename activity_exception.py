import time 
network_status = 400
trial = 0
opened = False

class Biometrics:
    fingerPrints = ['@13440)^jd']

    def login(cls, fingerPrint=None):
        if fingerPrint in cls.fingerPrints:
            return True
        return False

def openDoor(**kwargs):
    biometric = Biometrics()
    feedback = biometric.login(**kwargs)
    return feedback

def hasOpened():
    global opened
    return True if opened else False
    

class doorNotOpenedError(Exception):
    def __init__(self, message="Invalid credentials"):
        super().__init__(message)
        self.message = message

try:
    sensor_reading = '@13440)^jd' #sensor.read()
    if not openDoor(fingerPrint=sensor_reading):
        raise doorNotOpenedError()
    
except doorNotOpenedError: 
    while trial < 3:
        if openDoor(fingerPrint=sensor_reading):
            print('Try again', 3- (trial +1), 'remaining')
            trial += 1
            time.sleep(3)
            if trial >= 2:
                sensor_reading= '@13440)^jd'

else:
    print('No error occurred')

finally:
    print('Runs with ot without error')

