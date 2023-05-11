from namespace_activity_2 import *


num = 5

# Global name space

def checkNum(self):
    # Local name space
    global num
    num += 1
    y = 0
    return num

print(checkNum())