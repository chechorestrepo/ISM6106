"""
This is the Camera Object
"""

class Camera:
    def __init__(self, pixels, color, resolution):
        self.pixels = pixels  # Attribute of Camera
        self.color = color  # Attribute of Camera
        self.resolution = resolution  # Attribute of Camera

"""The following are the fucntions of the camera"""

    def scanbarcode(self):
        print("Scans the Barcode")

    def takePic(self):
        print("Takes Picture")

    def takeVid(self):
        print("Takes a Video")

    def status(self):
        print("Reports Current Status")
