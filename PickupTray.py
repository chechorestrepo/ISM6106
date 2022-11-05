"""
File that contains PickupTray and Tray1 as a subclass
"""

class PickupTray:
    def __init__(self, type, color) None:
        self.type = type """This is the attribute of the pickup tray"""
        self.color = color """This is the Color attribute of pickup tray"""

"""This are the 2 functions of the tray"""
        def goUp(self):
            print("Tray Goes Up")
        def goDown(self):
            print("Tray Goes Down")

"""The following is a subclass of PickupTray"""

class Tray1(PickupTray):
    def __init__(self, type, color):
        super().__init__(type,color)
        self.texture = 0
"""The following is the method to select the type of texture to be used in the pickup tray"""
    def picktexture(self,texture):
        print("Pick the type of texture to be used in the Tray")
        self._texture = texture
