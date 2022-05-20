class car(object):
    """docstring"""

    def __init__(self, color, doors, tires):
        """Constructor"""
        self.color = color
        self.doors = doors
        self.tires = tires

    def brake(self):
        """
        stop he car
        """
        return "Braking"

    def drive(self):
        """
        Drive the car
        """

        return "I'm driving!"


# How to create a subclass
class Car(Vehicle):
    """
    The Car Class
    """

    def brake(self):
        """
        Override brake method
        """
        return "The car class is breaking slowly!"


if __name__ == "__main__":
    car = Car("yellow", 2, 4, "car")
    car.brake()
    'The car class is breaking slowly!'
    car.drive()
    "I'm driving a yellow car!"
