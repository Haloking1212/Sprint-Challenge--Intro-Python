# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class VehicleType:

    def __init__(self, vehicle, flight_vehicle, star_ship):
        self.flight_vehicle = flight_vehicle
        self.star_ship = star_ship
        self.vehicle = vehicle

# Base Class


class GroundVehicle(VehicleType):

    def __init__(self, vehicle, car, motorcycle):
        super().__init__(vehicle)
        self.car = car
        self.motorcycle = motorcycle

    def __str__(self):
        return f'{self.vehicle}, {self.car}, {self.motorcycle}'


# Base Class


class AirVehicle(VehicleType):

    def __init__(self, airplane, flight_vehicle, star_ship):
        super().__init__(flight_vehicle, star_ship)
        self.airplane = airplane

    def __str__(self):
        return f'{self.airplane}, {self.flight_vehicle}, {self.star_ship}'


