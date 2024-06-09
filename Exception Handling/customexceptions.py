

class MachineNotWorking(Exception):
    pass

try:
    raise MachineNotWorking()
except ValueError:
    print("Occured")


