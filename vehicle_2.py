#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sham
#
# Created:     24-01-2017
# Copyright:   (c) Sham 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from vehicle import *

if __name__ == '__main__':

   print "From Vehicle_2"

   car1 = Car("Sham's vehicle","Four Wheeler","Blue", "20") # Instance of class Car
   car1.setData("Dark Blue", "20", "400K")
   #car1.displayData()


   '''
   print hasattr(car1, 'colour')
   print hasattr(car1, 'name')
   print hasattr(car1, 'nameVehicle')

   print getattr(car1, 'name')
   setattr(car1, 'name',"Sham's car")
   print getattr(car1, 'name')

   delattr(car1, 'name')
   #print getattr(car1, 'name')
   '''

   #print car1.__doc__
   #print Car.__name__
   #print car1.__name__
   #print car1.__module__
   #print Car.__bases__
   #print car1.__bases__
   print Car.__dict__
   print "\n\n"
   print car1.__dict__

