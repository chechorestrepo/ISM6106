"""
The Following the is the Class object for battery
""""

class battery:
    def __init__(self, type, charge) -> None:
        self.type = type
        """Defines the type of Battery"""
        self.charge = charge
        """Defines the type of charge being used"""

"""States if the battery needs to be charged"""

    def charge(self):
        print("Charge Y/N")

"""Sates current % charge"""

    def currentcharge(self):
        print("% charge")