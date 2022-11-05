"""
This is the Motherboard Class with Attributes and methods
"""


class RobotFrame:
    def __init__(self, color, material, weight) -> None:
        self.color = self.color
        """Defines the color of the frame of the Robot"""
        self.material = self.material
        """defines the material of the Frame of the Robot"""
        self.weight = self.weight
        """Defines the weight of the Frame of the Robot"""

    def consolidate(self):
        print("Brings the values from class battery, pickup tray, and motor")
