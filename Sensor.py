"""
The Following script contains the steps when the self-driving robot encounters an obstacle
"""
"""
In the following line I will define the sensor class
"""
class Sensor:
    def __init__(self, type, model):
            self.type = type
            self.model = model

"""
In the following line I will define the Obstacle class that will be detected by the sensor
"""
class Obstacle:
    def __init__(self, objectType, color):
            self.objectType = objectType
            self.color = color
"""
The following class will detect the obstacle, does not matter is if is static or it moves
"""
class Type(Sensor):
    def __init__(self, detectObstacle):
        self.detectObstacle = detectObstacle
            if self.detectObstacle() == 1
                print("Object has been detected and robot will change course")

"""
The following command will avoid the object by changing course 
"""

    def __int__(self, avoidObstacle):
        self.avoidObstacle = avoidObstacle
        print("Object has been detected and the robot will change course")
"""
The following condition will trigger the move of the robot if the sensor detects an abstacle
"""

    def move(self):
        if self.detectObstacle(1) > self.avoidObstacle
            print("The Robot will change course")
