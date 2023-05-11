

class Trigger:
    def trigger_error():
        def inner():
            return 3/10
        return inner()
    