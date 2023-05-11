
from activity_namespace_2 import *
num = 5
#Global name space

def checkNum():
    #Local name space

    global num 
    
    num += 1

    return num

print(checkNum)