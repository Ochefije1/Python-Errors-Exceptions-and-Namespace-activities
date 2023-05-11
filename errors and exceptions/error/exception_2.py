import time

network_status = 200
trial = 0

def tansferFund():
    return network_status

def hasTransfer():
    if network_status == 200:
        return True
    return False

class TransferError(Exception):
    def __init__