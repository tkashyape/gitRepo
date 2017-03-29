#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sham
#
# Created:     19-01-2017
# Copyright:   (c) Sham 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class Vehicle:
   """
   From class Vehicle.
   Base class of all vehicles.
   """

   nameVehicle = "Vehicle"

   def __init__(self, name, vehicleType):
      self.name = name
      self.vehicleType = vehicleType

   def displayData(self):

      print "\n"
      print "From class Vehicle from Module: ", __name__
      print "Name of my vehicle: ", self.name
      print "Type of my vehicle: ", self.vehicleType


class Car(Vehicle):
   """
   From class Car.
   Base class of all cars.
   """

   nameCar = "Car"

   def __init__(self, name, vehicleType, colour, mileage):

      Vehicle.__init__(self,name,vehicleType)   # Constructor of class Vehicle

      self.colour = colour
      self.mileage = mileage

   def setData(self, colour, mileage, rangeKm):
      self.colour = colour
      self.mileage = mileage
      self.rangeKm = rangeKm

   def displayData(self):

      print "\n"
      print "My car's name: ", self.name
      print "My car's type", self.vehicleType
      print "My car's colour: ", self.colour
      print "My car's mileage: ", self.mileage
      print "My car's range in KM: ", self.rangeKm


if __name__ == '__main__':

   vehicle1 = Vehicle("Sham's Vehicle", "Transport")  # Instance of class Vehicle
   vehicle1.displayData()
   print vehicle1.nameVehicle    # Global variable from class Vehicle

   car1 = Car("Sham's vehicle","Four Wheeler","Blue", "20") # Instance of class Car
   car1.setData("Dark Blue", "20", "400K")
   car1.displayData()

   print "From Module: ", __name__
