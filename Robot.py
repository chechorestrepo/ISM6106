"""
The Following is the Robot Class
"""
"""
Attributes of the class
"""
class robot:
    def __init__(self, color, model):
        self.color=color #This is the Attributes of the Robot
        self.model=model #This is the Attributes of the Robot
"""The following are the functions of the Robot class"""
    def moveForward(self):
        print("The Robot Moves Forward")
    def moveBack(self):
        print("The Robot Moves Back")
    def moveLeft(self):
        print("The Robot Moves Left")
    def moveRight(self):
        print("The Robot Moves Right")
    def spin(self):
        print("The Robot will spin")
    def trayUp(self):
        print("The Tray will go up")
    def trayDown(self):
        print("The Tray will go Down")
    def enableCamera(self):
        print("The camera will take an action")
    def statusCheck(self):
        print("The Camera will perform a status check of all its functions")
    def receiveInfo(self):
        print("The Robot will receive Information")
    def receiveCommand(self):
        print("the Robot will receive a command")